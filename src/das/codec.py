# -- coding:utf-8 --
#解码器定义

from aobject import *
import os,os.path,sys,time,datetime
# import codec_ks108
#import codec_ks102

from gevent.coros import Semaphore
import gevent

MediaCodecType = MediaDataType

#MediaCodec_KS108 = codec_ks108.MediaCodec_KS108
#MediaCodec_KS102 = codec_ks102.MediaCodec_KS102

class MediaCodec_Base:	
	def __init__(self,svc):
		#maxsize - 最大缓存，超过限制将视为无效解码
		self.buf =''
		self.conn = None
		self.svc = svc
		self.mtx = Semaphore()
		self.msgcnt=0 #接收消息计数

	def parseMessage(self,s):
		pass


	#数据置入队列,应检查队列长度和数据合法性
	def queueIn(self,s,conn):
		self.mtx.acquire()
#		self.buflist.append(s)
		self.buf+=s
		self.mtx.release()
		return True


	
	def decode(self):
		#@return (packets,retry) retry表示解码遇到错误或者数据非法
		return (),False


	#根据传入的消息分拣出gps,alarm消息  MsgAoModule_Alarm(), MsgAoModule_GpsData()
	def filter_msg(self,m,aom):
		# GSP，ALARM 消息是关心的消息，需要反馈到客户端
		return (m,)
	
	def command(self,aom,m):
		pass

	def save(self,aom,m):
		'''
			保存设备所有信息，不区分是何类型
		'''
		try:
			cm = aom.ao.cm
			params= m.params
			if isinstance(m.params,dict):
				params = json.dumps(m.params)
			log = cm.AO_ModuleLog()
			log.ao = aom.ao.r
			log.module = aom.r
			log.type = ModuleMsgType.DEV2SYS
			log.time = datetime.datetime.now()
			log.msgtype = 'N/A'
			log.params = params
			log.rawmsg = m.rawmsg
			log.seq = 0
			log.save()
			return True
		except:
			traceback.print_exc()
			return False


class MediaCodec_Null(MediaCodec_Base):
	#Null解码器，只是为了支持接口
	def __init__(self):
		MediaCodec_Base.__init__(self,None)

	def encode(self,s):
		return s

	def decode(self,s,conn=None):
		return s

	#@save: 对象存储
	def save(self,store):
		pass


class ModuleData_Gps:
	gpstime = 0
	satenum  = 0
	sateused = 0
	lon = 0
	lat = 0
	speed = 0
	angle = 0
	power = 0
	acc = 0
	miles = 0
	av = 0

class ModuleData_Meta:
	mid = ''
	msg =''
	seq = 0
	rawmsg =''
	devtype = ''
	cmd = ''
	params ={}
	systime = datetime.datetime.now()
	gps = None
	alarm = None




# class MediaCodec_Gps(MediaCodec_Base):
# 	def __init__(self):
# 		MediaCodec_Base.__init__(self,MediaCodecType.GPS)
#
# 	def decode(self,s,conn=None):
# 		#@return MediaData_Gps or None
# 		pass
#
#
# class MediaCodec_Audio(MediaCodec_Base):
# 	def __init__(self):
# 		MediaCodec_Base.__init__(self,MediaCodecType.AUDIO)
#
# 	def decode(self,s,conn=None):
# 		#@return MediaData_Audio or None
# 		pass
#
#
#
#
# #简单的模拟gps接收解码器
# #gps接收程序解析之后连接本地的TcpService端口，并传送过来
# #只有简单的gps数据，模拟端口打开
# class MediaCodec_SimpleGps(MediaCodec_Base):
# 	def __init__(self):
# 		MediaCodec_Base.__init__(self,MediaCodecType.GPS)
#
# 	def decode(self,s,conn):
# 		'''
# 		消息包格式: hwid,gpstime,lon,lat,satenum,sateused,speed,angle\n
# 		@return: 	packets,retry
# 		'''
# 		#@return 解码出多个消息包，并返回是否
# 		self.rbuf+=s
# 		segs = self.rbuf.split('\n')
# 		retry = True
# 		packets=[]
# 		if len(segs):
# 			self.rbuf = segs[-1] #最后一个不完整的包待下一次解析
# 			segs = segs[:-1]
# 			for s in segs:
# 				try:
# 					hwid,gpstime,lon,lat,satenum,sateused,speed,angle = s.split(',')
# 					d={'mid':hwid,
# 							'time':datetime.datetime.now(), #datetime.datetime.fromtimestamp(float(gpstime)),
# 							'lon':float(lon),
# 							'lat':float(lat),
# 							'speed':float(speed),
# 							'angle':float(angle),
# 							'type':MediaDataType.GPS,
# 							'power':0,
# 							'acc':0,
# 							'miles':0
#
# 					}
# 					packets.append(d) #单一的数据包类型
# 				except:
# 					traceback.print_exc()
# 		return packets,retry
#
# 	#执行设备命令
# 	def command(self,aom,msg):
# 		# cmd - object (json decoded)
# 		#@return:  返回命令串
# 		cmdstr = ''
# 		return cmdstr
#
# 	def save(self,aom,d):
# 		d['speed'] = d['speed'] * 1.852
# 		g = aom.gm.AOMData_Gps()
# 		g.ao = aom.ao.dbobj
# 		g.savetime = d['time']
# 		g.satenum = 0
# 		g.sateused =0
# 		g.lon = d['lon']
# 		g.lat = d['lat']
# 		g.speed = d['speed']
# 		g.angle = d['angle']
# 		g.save()
#
# 		t = time.mktime(g.savetime.timetuple())
# 		d['time'] = t
# 		print d,g.id
# 		#此数据需要分派出去
# 		aom.dispatch(d)
#
# 	def parse(self,aom,d):
# 		# do nothing
# 		#这里有些数据需要自动化处理反馈到设备的消息
# 		pass
#
#

if __name__=='__main__':
	d = ModuleData_Meta()
	print dir(d),d.seq