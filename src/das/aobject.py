# -- coding:utf-8 --


import socket,traceback,os,os.path,sys,time,struct,base64,gzip,array,threading,zlib,json
import datetime


class ModuleMsgType:
	SYS2DEV = 1
	DEV2SYS = 2


class MediaDataType:	
	GPS   = 1<<0
	AUDIO = 1<<1
	VIDEO = 1<<2
	IMAGE = 1<<3
	TEXT =  1<<4
	IODATA = 1<<5
	RAWBLOB = 1<<6	
	COMMAND = 1<<7	#通用命令
	ALARM =  1<<8  #报警信息
	UNDEFINED = 0xff

class MediaData_Base:
	def __init__(self,mst):
		self.mst = mst
		self.isdispatch = True #标示此消息是否要进行分派到 cacheserver
	
	def getType(self):
		return self.mst
	
	def getId(self):
		#这里是获得的module id,subclass必须支持
		return ''
	
#MediaData_Gps
#基础的Gps属性
class MediaData_Gps(MediaData_Base):
	def __init__(self):
		MediaData_Base.__init__(self,MediaDataType.GPS)
		self.hwid =''
		self.lon = 0
		self.lat = 0
		self.speed = 0
		self.angle = 0
		self.satenum = 0
		self.sateused = 0
		self.time = 0
		self.power = 0	#电源状态
		self.acc = 0	#点火状态
		self.miles=0	#里程计数
	
	def getId(self):
		return self.hwid #模块的硬件标示
	
	def __unicode__(self):
		return "%s,%s,%s,%s,%s,%s,%s,%s"%(self.hwid,self.lon,self.lat,self.speed,self.angle,self.satenum,self.sateused,self.time)
	
	#编码传输数据(未压缩,未json)
	def hash(self,enctype='json'):
		t = time.mktime(self.time.timetuple())
		s = {'type':MediaDataType.GPS,'hwid':self.hwid,
			 'lon':self.lon,'lat':self.lat,
			 'speed':self.speed,'angle':self.angle,
			 'satenum':self.satenum,'sateused':self.sateused,
			 'time':t,
			 'power':self.power,
			 'acc':self.acc,
			 'miles':self.miles}		
		return s

class MediaData_Command(MediaData_Base):
	def __init__(self,cmd):
		MediaData_Base.__init__(self,MediaDataType.COMMAND)
		MediaData_Base.isdispatch = False 	#默认不需要分派
		self.aoid = 0	#ao对象数据库编号
		self.cmd = cmd #AOCTRL_CMD_XXX
		self.time = time.time() #datetime.datetime.now()
		self.params='' 			#命令控制的参数
		
	
class MediaData_Audio(MediaData_Base):
	G7231 = 1
	GSM610 = 2
	PCM8 = 3
	PCM16 = 4
	
	def __init__(self):
		MediaData_Base.__init__(self,MediaDataType.AUDIO)		

class MediaData_Video(MediaData_Base):
	H264 = 1
	JMPEG = 2
	H263 = 3
	MPEG1 = 4
	MPEG2 = 5
	def __init__(self):
		MediaData_Base.__init__(self)
		self.mst = MediaDataType.VIDEO
	
class MediaData_Image(MediaData_Base):
	PNG = 1
	JPEG = 2
	GIF = 3
	BMP = 4
	UNDEFINE = 0xff
	def __init__(self):
		MediaData_Base.__init__(self)
		self.mst = MediaDataType.IMAGE


class ActiveObject_Module:
	def __init__(self,ao,dbobj):
		self.ao = ao
		#self.type  = type 	#MediaType.*
		self.conn = None	#

		self.sid = dbobj.sid 		       #模块对象的硬件标示
		self.url = None 	            #连接信息
		self.svcname = dbobj.svcname    #服务名称 对于向外连接的情况有效
		self.r = dbobj
		self.id = dbobj.id
	
	def __str__(self):
		return "<%s>.id=%s,url=%s,svcname=%s"%(self.type,self.id,self.url,self.svcname)
	
	#目前禁止对外连接的情况，设备都是主动连接到中心平台
	#def connect(self):
	#	#向外主动连接,如果是被动连接则无需
	#	s = service.DaemonService_Manager.instance().getService(self.svcname)
	#	if s and self.url:
	#		self.conn = s.newline(self,self.url) #需要主动连接外部设备
	#
	
	# data  - MsgAoModule_Base
	#从连接上接收数据包上来

#	模块设备断开当前的网络连接
	def destroy(self):
		try:
			if self.conn:
				self.conn.close()
		except:
			traceback.print_exc()

	def readData(self,m,conn,db=None):		
		if m.mid != self.sid:     #硬件编号
			return False

		try:
			conn.aom = self # bind 这里很重要，一个连接与设备模块关联起来了
			self.conn = conn	#保存了便于之后发送消息到设备

			conn.codec.command(self,m) #执行一些必要的反馈
			conn.codec.save(self,m) #接收的数据写入数据库

			#分拣出gps数据和报警数据传递到控制服务器
			ms = conn.codec.filter_msg(m,self)
			for m in ms:
				self.saveData(m)
				self.ao.app.sendToModuleClient(self.ao.r.id,m)
		except:
			print traceback.format_exc().decode('utf-8').encode('gbk')
			return False
		return True


	def saveData(self,m):
#		print repr(m)
		if m.gps:
			d = self.ao.cm.AOMData_Gps()
			d.aom = self.r
			d.ao = self.ao.r
			d.savetime = m.systime
			d.satenum = m.gps.satenum
			d.sateused = m.gps.sateused
			d.lon = m.gps.lon
			d.lat = m.gps.lat
			d.speed = m.gps.speed
			d.angle = m.gps.angle
			d.power = m.gps.power
			d.acc = m.gps.acc
			d.miles = m.gps.miles
			d.av = m.gps.av
			d.save()

		#----- alarm logging ----------------------------
#		if m['type'] == 'aom_alarm': #保存报警消息
#			pass
#		'''
#			if d['msg'] == 'BO01': #报警
#			alarm = aom.gm.AO_AlarmLog()
#			alarm.ao = aom.ao.dbobj
#			alarm.time = datetime.datetime.now()
#			alarm.type = d['alarm']
#			alarm.save()
#			#分派报警
#			t = time.mktime(alarm.time.timetuple())
#			s = {'type':MediaDataType.ALARM,
#			 'alarm':alarm.type,
#			 'comment':ALARM_TYPELIST[alarm.type]
#			 }
#			aom.dispatch(s) #分派到 cached server
#		'''
	
	def sendData(self,d):
		try:
			if self.conn == None:
				print 'device is offline!'
				return
			self.conn.codec.command(self,d)
		except:
			traceback.print_exc()

	
#active object是个应用概念上的设备对象，运行过程中它将缓存此对象的所有
#接收到的数据，等待其它系统访问、冲刷; 但在对实时性要求比较高的情况下
#ActiveObject要主动提交数据到其它的子系统去 
class ActiveObject_Base:
	#系统对象
	def __init__(self,dbobj,app=None):
		#codecCLS 编解码器类
		self.app = app
		self.modules = [] #通道集合
		self.mtxthis = threading.Lock()
		self.id = dbobj.id  #数据库对象唯一标示
		self.r = dbobj #giscore.models.ActiveObject
		self.cm = app.getDbModule()
		self._initModules()
	
	#连接设备或者初始化
	def _initModules(self):
		#1.加载所有modules
		rs = self.cm.AO_Module.objects.filter(ao__id=self.id)
		for r in rs:
			aom = ActiveObject_Module(self,r)
			self.modules.append(aom)

	def addModule(self,m):
		self.modules.append(m)
		
	def getModule(self,type):
		m = None
		try:
			m = self.modules[0]
		except:pass
		return m

	def destroy(self):
		self.mtxthis.acquire()
		for m in self.modules:
			m.disconnect()
		self.mtxthis.release()



	def readData(self,d,conn):
		#@return True - 数据匹配到具体的module设备.else False
		# d - codec解码出来的统一的设备消息,这些消息被分派到module去识别
		r = False
		self.mtxthis.acquire()
		print 'ao readData..'
		for m in self.modules:
			if m.readData(d,conn):
				r = True
				break
		self.mtxthis.release()
		return r
	
	def sendData(self,d):
		'''
			module - module idx
		'''
		self.mtxthis.acquire()
		for aom in self.modules:
			aom.sendData(d)
		self.mtxthis.release()

#
#	#执行命令道ao对象
#	def cmdExc(self,module,jsondata):
#		for m in self.modules:
#			if m.type & module: #判断正确的模块类型
#				m.cmdExc(jsondata)
