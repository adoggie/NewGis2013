# -- coding:utf-8 --
#解码器定义

from aobject import *
import os,os.path,sys,time,datetime
import codec
from gevent.coros import Semaphore
import gevent
MediaCodecType = MediaDataType

class MediaCodec(codec.MediaCodec_Base):
	def __init__(self,svc):
		codec.MediaCodec_Base.__init__(self,svc)


	def decode(self):
		'''
		消息包格式: hwid,gpstime,lon,lat,satenum,sateused,speed,angle\n
		@return: 	packets,retry
		'''
		#@return 解码出多个消息包，并返回是否

		msglist=[]
		self.mtx.acquire()
		p = self.buf.rfind('\n')
		ss = self.buf[:p]
		self.buf = self.buf[p+1:]
		self.mtx.release()
		msglist = ss.split('\n')
		return msglist,True

	
	#执行设备命令
	def command(self,aom,m):
		# cmd - object (json decoded)
		#@return:  返回命令串
		pass


	def parseMessage(self,s):
		msg = codec.ModuleData_Meta()
		msg.systime = datetime.datetime.now()
		msg.devtype = 'phone'

		try:
			s = s.strip()
			hwid,gpstime,lon,lat,satenum,sateused,speed,angle = s.split(',')
			msg.mid  = hwid
			gps = codec.ModuleData_Gps()
			gps.gpstime = int(float(gpstime))
			gps.satenum = 0
			gps.sateused  = 0
			gps.lon = float(lon)
			gps.lat = float(lat)
			gps.speed = float(speed)
			gps.angle = float(angle)
			msg.gps = gps
		except:
			traceback.print_exc()
			return None
		return msg



