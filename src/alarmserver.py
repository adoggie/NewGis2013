# -*- coding:utf-8 -*-

# revisions:


import sys,os,traceback,threading,time,datetime,json
from gisbase import *
from taskserver  import *
import dbconn
import psycopg2

#from pycomm import utils


'''
系统运行现象解释:
1. 报警项配置触发维持时间10s，加入barrier_in条件，围栏条件始终成立时，报警产生记录相隔20s
  -- 由于第一次触发报警之后，asi清除了gps数据，导致围栏检测结果不成立，设备的gps采样时间间隔设置了10秒，所以
     围栏检测成功将在20秒之后被触发


'''

'''
报警配置项被触发，创建报警执行任务，任务被分解到多个action被执行;
报警配置项触发之后直到任务执行完毕才放回到报警检查项队列,意味着一个报警项触发联动
之后，在未联动完毕之前是被忽略的，或者不会再次触发的


'''

#报警数据
# 数据类型 见 MsgAoModule_GpsData ， ks108.py:filter_msg()产生包装消息
# ctrlserver.py: dispatch()再次封装为AoData
class AoData:
	GPSDATA='gpsdata'
	ALARMDATA ='alarmdata'
	def __init__(self,aoid,type=GPSDATA,d=None):
		# d - 具体的数据解释数据
		self.type = type
		self.aoid = aoid
		self.d = d #如为报警 d['type'] =  指定报警类型


class AlarmFilterItem:
	def __init__(self,asi,type):
		self.asi = asi
		self.type = type

#	是否已经触发
	def triggered(self):
		return False

#	数据进入
	def dataIn(self,d):
		pass

	def reset(self):
		pass

	def getText(self):
		return ''

	def getType(self):
		return self.type

	def getLog(self):
		return self.asi.getLog()

#报警检测项 - 速度检测靠gps采点，而不是靠设备发送报警消息
class AFI_SpeedOver(AlarmFilterItem):
	def __init__(self,min,max,asi):
		AlarmFilterItem.__init__(self,asi,'speedover')
		self.min,self.max = min,max # (from,to)

	def triggered(self):
		if not self.asi.gps:
			return False

		speed = self.asi.gps['speed']
		if speed >= self.min and speed <= self.max:
			return True
		return False

	def getText(self):
		return u'速度限制:%s km - %s km'%(self.min,self.max)

#报警检测项 - 时间
class AFI_Time(AlarmFilterItem):
	def __init__(self,filter,asi):
		AlarmFilterItem.__init__(self,asi,'time')
		self.timerange = filter['timerange'] #时间范围  (from,to )  unix 1970 secs
		self.daytimes = filter['daytimes'] #[()]
		self.weekdays = filter['weekdays'] #
#		    timerange,daytimes,weekdays = None,表示都不限定

	def triggered(self):
		tick = int(time.time()) #gps['gpstime']
		mask = 0b111
		if self.timerange:
			if not utils.between( tick,self.timerange[0],self.timerange[1]):
				mask &= ~0b01

		if self.daytimes:
			dt = utils.mk_datetime( tick)
			if not utils.between(dt.hour ,self.daytimes[0],self.daytimes[1]):
				mask &= ~0b10
		if self.weekdays:
			dt = utils.mk_datetime( tick)
			if self.weekdays[dt.weekday()] == 0: #指定的周日上无效
				mask &= ~0b100
		if mask == 0b111:
			return True
		return False

	def getText(self):
#		text = ''
#		if self.timerange:
#			f,t = self.timerange
#			dt = utils.mk_datetime(f)
#			text+= u''%utils.formatDateTime_ymd2(f)
		return ''

#gps信号丢失或者无法定位 av = 0
#检测gpslost必须第一次加载最近的gps定位消息
class AFI_GpsLost(AlarmFilterItem):
	def __init__(self,timeout,asi):
		AlarmFilterItem.__init__(self,asi,'gpslost')
		self.timeout = timeout #超时接收,这个值可以配置为系统参数,比如: 60s
		self.av_ok_time = int(time.time()) #有效的收星时间

	def dataIn(self,d):
		if d.type == AoData.GPSDATA:
			gps = d.d['gps']
			if gps['av'] == 1:
				self.av_ok_time = int(time.time()) #记录最近一次av有效时间


	def triggered(self):
		if not self.asi.gps:
			return False #gps数据从来没有
		if int(time.time()) - self.asi.gps['gpstime'] >= self.timeout:
			return True

		if int(time.time()) - self.av_ok_time >= self.timeout:
			return True #连续不能接收到av=1的gps信号视为报警触发

		return False

#设备离线， 长时间接收不到gsm消息
#根据接收上一次gps时间为准
class AFI_Offline(AlarmFilterItem):
	def __init__(self,timeout,asi):
		AlarmFilterItem.__init__(self,asi,'offline')
		self.timeout = timeout #超时接收,这个值可以配置为系统参数,比如: 60s
		self.lasttick = int(time.time())

	def dataIn(self,d):
		self.lasttick = int(time.time())


	def triggered(self):
		if int(time.time()) - self.lasttick > self.timeout:
			return True
		return False

class AFI_AccOn(AlarmFilterItem):
	def __init__(self,asi):
		AlarmFilterItem.__init__(self,asi,'acc_on')

	def triggered(self):
		if not self.asi.gps:
			return False    #gps数据从来没有
		return self.asi.gps['acc'] == 1


class AFI_AccOff(AlarmFilterItem):
	def __init__(self,asi):
		AlarmFilterItem.__init__(self,asi,'acc_off')

	def triggered(self):
		if not self.asi.gps:
			return False    #gps数据从来没有
		return self.asi.gps['acc'] == 0


#class AFI_AccOn(AlarmFilterItem):
#	def __init__(self,asi):
#		AlarmFilterItem.__init__(self,asi)
#
#	def triggered(self):
#		if not self.asi.gps:
#			return False    #gps数据从来没有
#		return self.asi.gps['acc'] == 1

#电源丢失，设备将发送电源被切断的消息包上来
#电源被切断，但设备还会连续工作一段时间
class AFI_PowerLost(AlarmFilterItem):
	def __init__(self,asi):
		AlarmFilterItem.__init__(self,asi,'powerlost')
		self.powerlost = False

	def dataIn(self,d):
		if d.type == AoData.ALARMDATA:
			type = d.d['type'] #报警类型
			if type == AlarmType.PowerLost:
				self.powerlost = True #电源丢失了

	def triggered(self):
#		return self.powerlost
		if not self.asi.gps:
			return False    #gps数据从来没有
		return self.asi.gps['power'] == 0

	def reset(self):
		self.powerlost = False

#求救
class AFI_SOS(AlarmFilterItem):
	def __init__(self,asi):
		AlarmFilterItem.__init__(self,asi,'sos')
		self.sos = False

	def dataIn(self,d):
		if d.type == AoData.ALARMDATA:
			type = d.d['type'] #报警类型
			if type == AlarmType.SOS:
				self.sos = True

	def triggered(self):
		return self.sos

	def reset(self):
		self.sos = False

#围栏进入
class AFI_BarrierIn(AlarmFilterItem):
	def __init__(self,name,rclist,asi):
		"""
			name  - 围栏名称
			rclist - 可以是单个围栏，也可以是多个围栏区域构成的围栏组
		"""
		AlarmFilterItem.__init__(self,asi,'barrier_in')
		self.name = name
		self.rclist = rclist

	def triggered(self):
		if not self.asi.gps:
			return False
		gps = self.asi.gps
		x,y = gps['lon'],gps['lat']
		self.getLog().debug('check barrier_in:',gps, self.rclist)
		for rc  in self.rclist:
			x1,y1,w,h = rc
			x2 = x1+w
			y2 = y1+h
			self.getLog().debug( x,y,x1,y1,x2,y2)
			if x >= x1 and x<=x2 and y>=y1 and y<=y2:

				return True

		return False

#围栏出去
class AFI_BarrierOut(AlarmFilterItem):
	def __init__(self,name,rclist,asi):
		AlarmFilterItem.__init__(self,asi,'barrier_out')
		self.name = name
		self.rclist = rclist

	def triggered(self):
		if not self.asi.gps:
			return False
		gps = self.asi.gps
		x,y = gps['lon'],gps['lat']
		#扫描都不在所有的rc里面
		trig = False
		for rc in self.rclist:
			x1,y1,w,h = rc
			x2 = x1+w
			y2 = y1+h
			if x >= x1 and x<=x2 and y>=y1 and y<=y2:
				trig = True
		return not trig


#同一个ao只能配置相同的一项报警类型,不能重复配置
class AlarmSettingItem:
	def __init__(self,server):
		self.r = None #数据库表记录
		self.server = server
		
		self.aoid = None
		self.type = ''
		
		self.actions=None	#json格式编码
		self.filter = None	#json格式编码
		self.issue_time = time.time() 	#启动时间
		self.issue_times = 0 	#触发次数

		self.suppress_duration =0
		self.suppress_wait = 0 #报警产生之后抑制等待时间

		self.trigger_time = 0   #触发时间
		self.trigger_allow = 0 #

		self.task = None 		#执行中的任务对象，可以进行停止,报警执行完毕将清除task关联
		self.doexec = False

		self.gps = None #保存当前接收的数据
		self.alarm = None

		self.asfs=[] #检测项
		self.mtxthis = threading.Lock()

		self.reset()

	def getLog(self):
		return self.server.getLogger()

	def init(self,r):
		try:
			self.r = r
			self.aoid = r['aoid']
			self.filter = utils.loadjson_s(r['filter'])
			self.actions = utils.loadjson_s(r['actions'])
			self.suppress_duration = self.filter['suppress_duration']
			self.suppress_wait = self.filter['suppress_wait']*60 #单位: 分钟到秒转换

			asf = AFI_Time(self.filter['time'],self)
			self.asfs.append(asf)

			for p in self.filter['params']:
				name = p.get('name','')
				param = p.get('param')
				asf = None
#				if name == 'time':
#					asf = AFI_Time(param,self)
				if name == 'barrier_in':
					asf = AFI_BarrierIn(param[0],param[1:],self)
				elif name == 'barrier_out':
					asf = AFI_BarrierOut(param[0],param[1:],self)
				elif name =='speedover':
					asf = AFI_SpeedOver(param[0],param[1],self)
				elif name =='gpslost':
					asf = AFI_GpsLost(param,self)
				elif name =='powerlost':
					asf = AFI_PowerLost(self)
				elif name == 'acc_on':
					asf = AFI_AccOn(self)
				elif name =='acc_off':
					asf = AFI_AccOff(self)
				elif name =='sos':
					asf = AFI_SOS(self)

				if asf:
					self.asfs.append(asf)
		except:
			traceback.print_exc()
			return False
		return True

#	外部数据传递进入
	def dataIn(self,d):
		self.getLog().debug('asi dataIn:',d.d)
		if d.type == AoData.GPSDATA:
			self.gps = d.d['gps']
		if d.type == AoData.ALARMDATA:
			self.alarm = d.d

	#TaskServer将调用reset
	def reset(self):
		self.task = None
		self.issue_time = time.time()
		self.issue_times = 0
		self.doexec = False

		self.trigger_time = 0
		self.gps = None #清空数据
		self.alarm = None
#		报警检测项重置
		self.mtxthis.acquire()
		for asf in self.asfs:
			asf.reset()
		self.mtxthis.release()

	def triggered(self):
		now = int(time.time())
		if now <= self.trigger_allow:
			return False

		trig = True
		self.mtxthis.acquire()
		for asf in self.asfs:

			if not asf.triggered():
				trig = False
			self.getLog().debug('check asf:',asf.getType(), '  succ:',trig )

		self.mtxthis.release()
		if trig:
			self.getLog().debug('1. asi triggered')
		r = False
		if self.trigger_time==0:
			if trig:
				self.trigger_time = int(time.time())
				r = True
		else:
			if trig: #连续触发
				r = True
			else:#这一次消除了触发
				self.trigger_time = 0 #消除触发记录，重新计数
		if r == True:
			#超出连续触发成立的时间
			r = False
			if now - self.trigger_time >= self.suppress_duration:
				r = True
				self.trigger_allow = now + self.suppress_wait #触发产生要进行等待
				self.getLog().debug('2. asi triggerred final...')
		return r

#	获取报警触发描述
	def getText(self):
		return  ''

	
#报警服务器
#够复杂
class AlarmServer:
	def __init__(self,ctrlsvr):
		self.ctrlsvr = ctrlsvr
		self.barriers = []

		self.aodatas=[]	#报警消息队列
		self.mtxthis = threading.Lock()
		self.asis = []  #报警配置项集合
		self.db = psycopg2.connect( database="newgis", user='postgres', password='ffmpeg', host='127.0.0.1')
		
	def getDBConn(self):
		#return self.ctrlsvr.getDBConn()
		return self.db
		
	def getLogger(self):
		return self.ctrlsvr.getLogger()
	

	#所有的外部触发报警都进入此接口
	def onAoData(self,aoid,d):
		self.mtxthis.acquire()
		for asi in self.asis:
			self.getLogger().debug('onAoData:',aoid,'==',asi.aoid)
			if asi.aoid == aoid:
				asi.dataIn(d)
		self.mtxthis.release()
	

	'''
	加载所有的报警配置项到内存
	'''
	def start(self):

		#1.读取所有报警配置项
		db = self.getDBConn()
		cr = db.cursor()
#		sql="select * from giscore_AO_UserAlarmSettings where enable=true order by ao_id"
		sql = "select * from giscore_activeobject"
		cr.execute(sql)
		aos = dbconn.fetchallDict(cr)

		for ao in aos:
			sql = "select a.*,b.activeobject_id as aoid,c.name as aoname from \
					giscore_AO_UserAlarmSettings a,\
					giscore_activeobject_alarmsettings b, \
					giscore_activeobject c \
					where \
					a.id = b.ao_useralarmsettings_id \
					and b.activeobject_id=%s and \
					b.activeobject_id= c.id and \
			        a.enable=true"%(ao['id'])
			cr.execute(sql)

			rs = dbconn.fetchallDict(cr)
			for r in rs: #每个报警配置项处理
				asi = AlarmSettingItem(self)
				if asi.init(r):
					self.asis.append( asi )
		###
#		thread = threading.Thread(target=self.thread_check)
#		thread.start()
		import gevent
		gevent.spawn(self.thread_check)


	def thread_check(self):
		while True:
			self.checkItems()
			time.sleep(1)
#

#   处理ctrlserver传递过来的消息
	def disptch(self,m):
		m = m.getMsg()
		#报警配置项改变

		pass

	def checkItems(self):
#		print int(time.time()),' alarmserver:: checkItems() , asis size:',len(self.asis)
		self.mtxthis.acquire()
		for asi in self.asis:
			r = asi.triggered()
			if r:
				print int(time.time()),' triggerd!'
				task = self.ctrlsvr.getTaskServer().createTaskWithASI(asi)
				asi.task = task #可用于中途退出
				asi.reset()
		self.mtxthis.release()

	#任务执行完毕,报警配置项重新加入队列			
	def onTaskExecEnd(self,asi):
		self.mqcheck.queueIn(asi)


	#修改报警设置项之后，将这些项放入队列，然后再checkItems的时候进行更新
	#add可以直接添加到mqcheck; delete和update必须放置到队列
	def asi_add(self,asid,aoid):
		'''
		id - 数据库表记录id
		'''
		print 'asi_add:',asid,aoid
		self.mtxthis.acquire()
		try:
			db = self.getDBConn()
			cr = db.cursor()
			sql = "select a.*,b.activeobject_id as aoid,c.name as aoname from \
					giscore_AO_UserAlarmSettings a,\
					giscore_activeobject_alarmsettings b, \
					giscore_activeobject c \
					where \
					a.id = b.ao_useralarmsettings_id \
					and b.activeobject_id=%s and \
					b.activeobject_id= c.id and \
					a.id = %s and \
					a.enable=true"%(aoid,asid)
			cr.execute(sql)
			r = dbconn.fetchoneDict(cr)
			if  r:
				asi = AlarmSettingItem(self)
				if asi.init(r):
					self.asis.append( asi )
		except:
			traceback.print_exc()
		print 'now asi size:',len(self.asis)
		self.mtxthis.release()

	def asi_remove(self,asid,aoid):
		print 'asi_remove:',asid,aoid
		self.mtxthis.acquire()
		for i,asi in enumerate(self.asis):
			if asi.aoid == aoid and asi.r['id'] == asid:
				if asi.task:
					asi.task.terminated = True
				del self.asis[i]
				break
		print 'now asi size:',len(self.asis)
		self.mtxthis.release()

	#重新读入报警配置项
#	def asi_reload(self,id):
#		self.asi_delete(id)
#		self.asi_add(id)
#
#		db = self.getDBConn()
#		cr = db.cursor()
#		sql="select * from giscore_AO_AlarmSettings where  ao_id =%s"%(asi.aoid)
#		cr.execute(sql)
#		r = dbconn.fetchoneDict(cr)
#		if r:
#			asi.filter = json.loads(r['filter'])
#			asi.actions = json.loads(r['actions'])
	
	

if __name__=='__main__':
	pass

	
		
	