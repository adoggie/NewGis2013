# -- coding:utf-8 --
#解码器定义

from aobject import *
import os,os.path,sys,time,datetime,copy,threading,json,traceback
import codec
#from pycomm.message import *
import utils
from gisbase import *
#from gismsg import *
#from dbconn import *

from gevent.coros import Semaphore
import gevent

#MediaCodecType = MediaDataType
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
	

#AOCTRL_CMD_SHAKE_ACK =1 	#应答握手信号信息
#AOCTRL_CMD_REG_ACK= 2	#终端注册响应消息
#AOCTRL_CMD_SAMPLING_TIMESET = 3 	#等时连续回传设置
#AOCTRL_CMD_ALARM_ACK = 4	#应答报警消息
#AOCTRL_CMD_NAMED = 5 	#一次点名消息
#AOCTRL_CMD_SPEEDSET = 6 #设置车速上下限
#AOCTRL_CMD_POWER_ONOFF = 7 #电路控制信号
#AOCTRL_CMD_OIL_ONOFF = 8  #油路控制信号
#AOCTRL_CMD_REBOOT = 9 		#控制设备重启消息
#AOCTRL_CMD_ACC_ON_TIME = 10 #设置ACC开发送数据间隔
#AOCTRL_CMD_ACC_OFF_TIME = 11 #设置ACC关发送数据间隔
#AOCTRL_CMD_BARRIER_SET = 12 	#设置电子围栏消息
#AOCTRL_CMD_GETLOCATION = 13 		#应答获取终端所在位置消息
#AOCTRL_CMD_LISTEN_START = 14 		#监听命令
#AOCTRL_CMD_COMMADDR_SET = 15 	#设置终端IP地址和端口
#AOCTRL_CMD_APN_SET = 16			# 设置APN消息
#AOCTRL_CMD_GET_VERSION = 17 	# 读取终端版本消息
#AOCTRL_CMD_CLEAR_ALARMS = 18 	#取消所有报警消息
#AOCTRL_CMD_CLEAR_MILES = 19 	#里程清零消息
#AOCTRL_CMD_INIT_MILES = 20 		#里程初始化消息
#AOCTRL_CMD_UPDATING = 21 		#启动升级消息
#
#AOCTRL_CMD_SHACK_REQ =31 #握手信号消息
#AOCTRL_CMD_REG_REQ =32 	#终端注册信息
#AOCTRL_CMD_SAMPLING_TIMESET_ACK = 32 #应答等时连续回传设置
#AOCTRL_CMD_ALARM_REQ = 33 		#警报消息
#AOCTRL_CMD_NAMED_ACK = 34 		#应答点名信息
#AOCTRL_CMD_SIMPLING_GPSDATA = 35 		#等时连续回传消息
#AOCTRL_CMD_SIMPLING_END = 36 	#连续回传结束消息
#AOCTRL_CMD_SPEEDSET_ACK = 37 	#应答设置车速上下限
#AOCTRL_CMD_POWERCTRL_ACK = 38   #应答电路控制
#AOCTRL_CMD_OILCTRL_ACK = 39 	#应答油路控制
#AOCTRL_CMD_REBOOT_ACK = 40 		#应答设备重启消息
#AOCTRL_CMD_ACCON_TIMESET_ACK = 41 #应答设置ACC开发送数据间隔
#AOCTRL_CMD_ACCOFF_TIMESET_ACK=42 #应答设置ACC关发送数据间隔
#AOCTRL_CMD_BARRIER_SET_ACK =  43 #应答设置电子围栏消息
#AOCTRL_CMD_GETLOCATION_ACK = 44  #获取终端所在位置消息
#AOCTRL_CMD_LISTEN_ACK = 45 		#应答监听命令
#AOCTRL_CMD_COMMADDR_SET_ACK=46	#应答设置终端IP地址和端口
#AOCTRL_CMD_APN_SET_ACK=47		#应答设置APN消息
#AOCTRL_CMD_GETVERSION_ACK=48	#应答读取终端版本消息
#AOCTRL_CMD_CLEAR_ALARMS_ACK=49	#应答取消所有报警消息
#AOCTRL_CMD_CLEAR_MILES_ACK=50 	#应答里程清零消息
#AOCTRL_CMD_UPDATING_ACK = 61 	#应答启动升级消息
#AOCTRL_CMD_INIT_MILES_ACK = 62	#应答初始化里程消息
#
#AOCTRL_CMD_LIST={
#	AOCTRL_CMD_SHAKE_ACK:u'应答握手信号信息',
#	AOCTRL_CMD_REG_ACK:u'终端注册响应消息',
#	AOCTRL_CMD_SAMPLING_TIMESET:u'等时连续回传设置',
#	AOCTRL_CMD_ALARM_ACK:u'应答报警消息',
#	AOCTRL_CMD_NAMED:u'一次点名消息',
#	AOCTRL_CMD_SPEEDSET:u'设置车速上下限',
#
#	AOCTRL_CMD_POWER_ONOFF:u'电路控制信号',
#	AOCTRL_CMD_OIL_ONOFF:u'油路控制信号',
#	AOCTRL_CMD_REBOOT:u'控制设备重启消息',
#	AOCTRL_CMD_ACC_ON_TIME :u'设置ACC开发送数据间隔',
#	AOCTRL_CMD_ACC_OFF_TIME :u'设置ACC关发送数据间隔',
#	AOCTRL_CMD_BARRIER_SET :u'设置电子围栏消息',
#	AOCTRL_CMD_GETLOCATION :u'应答获取终端所在位置消息',
#	AOCTRL_CMD_LISTEN_START :u'监听命令',
#	AOCTRL_CMD_COMMADDR_SET :u'设置终端IP地址和端口',
#	AOCTRL_CMD_APN_SET :u'设置APN消息',
#	AOCTRL_CMD_GET_VERSION :u'读取终端版本消息',
#	AOCTRL_CMD_CLEAR_ALARMS :u'取消所有报警消息',
#	AOCTRL_CMD_CLEAR_MILES :u'里程清零消息',
#	AOCTRL_CMD_INIT_MILES :u'里程初始化消息',
#	AOCTRL_CMD_UPDATING :u'启动升级消息',
#
#	AOCTRL_CMD_SHACK_REQ :u'握手信号消息',
#	AOCTRL_CMD_REG_REQ :u'终端注册信息',
#	AOCTRL_CMD_SAMPLING_TIMESET_ACK :u'应答等时连续回传设置',
#	AOCTRL_CMD_ALARM_REQ :u'警报消息',
#	AOCTRL_CMD_NAMED_ACK :u'应答点名信息',
#	AOCTRL_CMD_SIMPLING_GPSDATA :u'等时连续回传消息',
#	AOCTRL_CMD_SIMPLING_END :u'连续回传结束消息',
#	AOCTRL_CMD_SPEEDSET_ACK :u'应答设置车速上下限',
#	AOCTRL_CMD_POWERCTRL_ACK :u'应答电路控制',
#	AOCTRL_CMD_OILCTRL_ACK :u'应答油路控制',
#	AOCTRL_CMD_REBOOT_ACK :u'应答设备重启消息',
#	AOCTRL_CMD_ACCON_TIMESET_ACK :u'应答设置ACC开发送数据间隔',
#	AOCTRL_CMD_ACCOFF_TIMESET_ACK:u'应答设置ACC关发送数据间隔',
#	AOCTRL_CMD_BARRIER_SET_ACK :u'应答设置电子围栏消息',
#	AOCTRL_CMD_GETLOCATION_ACK :u'获取终端所在位置消息',
#	AOCTRL_CMD_LISTEN_ACK :u'应答监听命令',
#	AOCTRL_CMD_COMMADDR_SET_ACK:u'应答设置终端IP地址和端口',
#	AOCTRL_CMD_APN_SET_ACK:u'应答设置APN消息',
#	AOCTRL_CMD_GETVERSION_ACK:u'应答读取终端版本消息',
#	AOCTRL_CMD_CLEAR_ALARMS_ACK:u'应答取消所有报警消息',
#	AOCTRL_CMD_CLEAR_MILES_ACK:u'应答里程清零消息',
#	AOCTRL_CMD_UPDATING_ACK :u'应答启动升级消息',
#	AOCTRL_CMD_INIT_MILES_ACK :u'应答初始化里程消息',
#}
	
	
ALARM_TYPELIST={
	0:u'车辆断电',
	1:u'电子围栏入界报警',
	2:u'车辆劫警（SOS求助）',
	3:u'车辆防盗器警报',
	4:u'车辆低速报警',
	5:u'车辆超速报警',
	6:u'电子围栏出界报警'
}

ALARM_TYPELIST={
	0:AlarmType.PowerLost ,# u'车辆断电',
	1:AlarmType.BarrierLimitIn, #u'电子围栏入界报警',
	2:AlarmType.SOS, #u'车辆劫警（SOS求助）',
	3:AlarmType.ROB, #u'车辆防盗器警报',
	4:AlarmType.SpeedLower, #u'车辆低速报警',
	5:AlarmType.SpeedOver, #u'车辆超速报警',
	6:AlarmType.BarrierLimitOut #u'电子围栏出界报警'
}



def parseTime(dmy,hms):
	d,mon,y = map(int, map(float,[dmy[:2],dmy[2:4],dmy[4:]]) )
	h,min,s = map(int, map(float,[hms[:2],hms[2:4],hms[4:]]) )
	#print d,mon,y,h,min,s
	return time.mktime((2000+y,mon,d,h,min,s,0,0,0))

#简单的模拟gps接收解码器
#gps接收程序解析之后连接本地的TcpService端口，并传送过来
#只有简单的gps数据，模拟端口打开
'''
MediaCodec
可以开启工作线程来处理解码工作，令socket服务线程可专注在接收数据处理

'''
class MediaCodec(codec.MediaCodec_Base):
	def __init__(self,svc):
		codec.MediaCodec_Base.__init__(self,svc)
	
	def getLog(self):
		return self.svc.app.getLog()
	
	def parse_gps(self,msg,s):
		# gps 数据长度62个字符
		msg['gps'] = None #AOCTRL_CMD_SIMPLING_GPSDATA
		if len(s)!=62:
			return
		try:
			yy = int(s[:2])
			mm = int(s[2:4])
			dd = int(s[4:6])
			av = s[6]	#是否有效
			lat = int(s[7:9])+ float( s[9:16]) / 60.
			ns = s[16] #维度标志 N/S
			lon = int(s[17:20]) + float( s[20:27]) /60.
			ew = s[27]
			speed = float(s[28:33])
			HH = int(s[33:35])
			MM = int(s[35:37])
			SS = int(s[37:39])
			angle = float(s[39:45])
			power = int(s[45])
			if power==1:
				power=0
			else:
				power=1

			acc = int(s[46])
			mileflag = s[53]
			miles = int(s[54:],16)/1000.00
			miles = round(miles,3)
			#print 2000+yy,mm,dd,HH,MM,SS
			gpstime = datetime.datetime(2000+yy,mm,dd,HH,MM,SS)
			#GMT+8
			gpstime = gpstime + datetime.timedelta(hours=8)
			if av =='A':
				av = 1
			else:
				av = 0
			msg['gps'] = {
				#'time':gpstime,
			    'system':datetime.datetime.now(),
				'gpstime':utils.mk_timestamp(gpstime),
				'satenum':0,
				'sateused':0,
				'lon':lon,
				'lat':lat,
				'speed':speed,
				'angle':angle,
				'power':power,
				'acc':acc,
				'miles':miles,
				'av':av,
				'systime':int(time.time())
			}
		except:
			traceback.print_exc()
			msg['gps'] = None
		
	def parseMessage(self,s):
		# @return:  MsgAoModule_Base()		
		#msg={'mid':self.conn.mid,'cmd':0,'seq':'','params':'','gps':None}	# mid - 模块硬件编号

		msg = codec.ModuleData_Meta()

		cmd = s[12:16]
		msg.msg = cmd
		msg.seq = s[:12]
		msg.rawmsg = s
		msg.devtype ='ks168'
		msg.cmd = cmd
		msg.gps = None
		msg.alarm =None

		msg.mid = msg.seq
		
		if cmd == 'BP00' : #握手信号消息
			pass
		
		elif cmd =='BP05':	#注册信息			
			#msg['mid'] = s[16:31] #			
			#self.conn.mid = msg['mid'] #设备连接上来这个是第一个消息包			
			self.parse_gps(msg,s[31:])
		elif cmd =='BS08': #应答等时连续回传设置			
			freq = int(s[16:20],16)			
			hours = int(s[20:22],16)
			minutes = int(s[22:24],16)
			duration = hours*3600 + minutes * 60
			msg.params = {'freq':freq,'duration':duration} #写入配置参数
			#此参数可以写入 activeobject属性字段，回去再想想
		elif cmd == 'BO01': #报警消息
			v = int(s[16])
			#msg['alarm'] = int(s[16]) #报警类型
			alarm = ''
			if v == 0:
				alarm = AlarmType.PowerLost
			if v == 1:
				alarm = AlarmType.BarrierLimitIn
			if v == 2:
				alarm = AlarmType.SOS
			if v == 3:
				alarm = AlarmType.ROB
			if v == 4:
				alarm = AlarmType.SpeedLower
			if v == 5:
				alarm = AlarmType.SpeedOver
			if v == 6:
				alarm = AlarmType.BarrierLimitOut
			msg.alarm = alarm
			self.parse_gps(msg,s[17:])
		elif cmd =='BP04' : #点名应答			
			self.parse_gps(msg,s[16:])
		elif cmd == 'BR00' : #等时连续回传消息			
			self.parse_gps(msg,s[16:])
		elif cmd == 'BR02' : #连续回传结束消息			
			self.parse_gps(msg,s[16:])
		elif cmd == 'BP12': #应答设置车速上下限			
			high = int(s[17:20])
			low = int(s[21:24]) #低速限制
			msg.params = {'high':high,'low':low}
		elif cmd == 'BV00': #应答电路控制
			value = int(len(s[17]))						
			msg.params = {'value':value}
		elif cmd =='BV01':#应答油路控制
			value = int(len(s[17]))						
			msg.params = {'value':value}
		elif cmd =='BT00':  #应答设备重启消息
			pass			
		elif cmd =='BR05':#应答设置ACC开发送数据间隔
			pass
		elif cmd =='BR06':#应答设置ACC关发送数据间隔
			pass
		elif cmd == 'BU00': #电子围栏设置回应
			pass
		elif cmd == 'BR03':		#获取终端所在位置消息			
			#self.parse_gps(msg,s[16:])
			pass
		elif cmd =='BS20' : #应答监听命令
			pass
		elif cmd =='BP02': #应答设置终端IP地址和端口
			pass
		elif cmd =='BP03':#应答设置APN消息
			pass
		elif cmd == 'BP01': #应答读取终端版本消息
			msg.params = s[16:]
		elif cmd == 'BS21': #应答取消所有报警消息
			pass
		elif cmd == 'BS04': #应答里程清零消息
			pass
		elif cmd == 'BS05': #应答启动升级消息
			pass
		elif cmd == 'BS06': #应答初始化里程消息			
			pass
		else:
			msg = None
		#print 'decode:',msg
		if msg:
			if msg.mid:
				self.conn.mid = msg['mid'] #设备编码关联		
		return msg	
	


		
		
	def decode(self):			
		#@return: 	packets,retry		
		#解码出多个消息包，并返回是否
		msglist=[]
		retry = True
		try:
			self.mtx.acquire()
			while True:
				p1 = self.buf.find('(')
				if p1 == -1:    #起始标识不存在
					self.buf=''
					break #注意，这里有容错功能
				self.buf = self.buf[p1:]

				p2 = self.buf.find(')')
				if p2 == -1:    #结束标示未存在
					if len(self.buf) > 1024:    #包过大
						self.buf=''
						return (),False # please break socket connection
					break	# push in more data
				msg = None
				try:
					msg = self.parseMessage(self.buf[1:p2])
				except:
					traceback.print_exc()
					msg = None
				if msg:
					msglist.append(msg)
				self.buf = self.buf[p2+1:]
			return msglist,retry
		finally:
			self.mtx.release()



	#执行设备命令
	'''
			响应：	中心回应AS01	
			说明：	本消息适用于所有终端。本消息最多发送10次，每次间隔30秒，收到平台响应后不再上发。	
	'''
	def command(self,aom,m):
		# cmd - object (json decoded)
		#@return:  返回命令控制消息
		if not m: return
		code=''
		params=''
		
		msg = m.get('type','')
		#seq =  m.attrs.get('seq','0'*12)
		seq =  m.get('seq',aom.sid)

		if msg =='BP00': #应答握手信号信息
			code = 'AP01HSO'
		elif msg =='BP05': #终端注册信息
			code = 'AP05'
		elif msg =='BO01':	#应答报警消息
			pass  #应答了之后设备不再产生新的报警
		
		elif msg == 'aom_oncenamed':	#一次点名消息
			code ='AP00'
			
		elif msg =='aom_speedlimit_set': #高速或低速报警设置
			hi = m['high']
			lo = m['low']
			code = "AP12H%03dL%03d"%(hi,lo)
			
		elif msg =='aom_continuedset_5': #AR00 等时持续回传设置			
			duration = m['duration'] 	#总时长
			hh = int(duration/3600)
			mm = (duration - hh*3600)/60
			mm = int(mm)			
			code = "AR00%04x%02x%02x"%(m['freq'],hh,mm)
			
		elif msg =='aom_power_set': #电路控制信号
			onoff = m['value']
			code = "AV00%d"%onoff #
		
		elif msg =='aom_oil_set': #油路控制
			onoff = m['value']
			code = "AV01%d"%onoff #
			
		elif msg  == 'aom_reset': #1控制设备重启消息
			code = "AT00"
			
		elif msg =='aom_accon_continued': #设置ACC开发送数据间隔
			interval = m['value']
			code = "AR05%04x"%interval
		elif msg =='aom_accoff_continued':
			interval = m['value']
			code = "AR06%04x"%interval
			
			
		elif msg =='aom_barrier_set': #设置电子围栏消息
			pass
		
		elif msg=='aom_listen': #监听命令
			code = 'AP15%s'%m['phone']

		elif msg == 'aom_getversion': #读取终端版本消息
			code = 'AP07'
			
		elif msg =='aom_clear_alarms': #取消所有报警消息
			code = 'AV02'
			
		elif msg =='aom_clear_miles': #里程清零消息
			code  ='AX03'
		
		elif msg =='aom_init_miles': #里程初始化消息
			meters = m['miles']
			code = "AX03%08x"%meters
			
		if not code:
			return
		
		code='(%s%s)'%(seq,code)
		code = code.upper()
		try:
			cm = aom.ao.cm
			log = cm.AO_ModuleLog()
			log.ao = aom.ao.r
			log.aom = aom.r
			log.type = ModuleMsgType.SYS2DEV
			log.time = datetime.datetime.now()
			log.msgtype = msg
			log.params = ''
			log.rawmsg = code
			log.seq = 0
			log.save()
			self.conn.write(code)   #写入设备的连接
#			self.getLog().debug('>>'+str(code))
		except:
			traceback.print_exc()
			
	#发送module的配置参数到设备
	#设备连接建立，发送系统配置参数给设备
	def initSettings(self,aom):
		try:
			cm = aom.ao.cm
			r = cm.AO_Module.objects.filter(id=aom.id)
			settings = json.loads(r.settings)
			for k,v in settings.items():
				m = {}
				if k=='acc_on_freq':
					m['value'] = v
				if k=='acc_off_freq':
					m['value'] = v
				if k=='sample_contined': #等时回传
					m['freq'] = v.get('freq',0)
					m['duration'] = v.get('duration',0)
				if m:
					gevent.sleep(5) #必须等待，连续发送将导致不处理，很有可能设备的缓存区过小，或者没有硬件握手，导致数据接收失败
					m['type'] = k
					self.command(aom,m)
						
		except:
			traceback.print_exc()

	def save(self,aom,m):
		#如果是连接进入的第一个消息包，读取modle的settings参数，发送到设备
		if self.msgcnt==0:
			self.initSettings(aom)
		self.msgcnt+=1
		codec.MediaCodec_Base.save(self,aom,m)





		
	