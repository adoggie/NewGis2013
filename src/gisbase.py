# -- coding:utf-8 --

import socket,traceback,os,os.path,sys,time,struct,base64,gzip,array,threading
import json,zlib

class ErrorCode:
	OK 	= 0 		#无错误
	
	NETWORK_LOSTCONNECTION = 1 #网络
	DECODE_FAILED = 2 #消息解码错误
	EXCEPTION = 3
	PACKETSIZE_LIMITED = 4 	#消息包过大
	MsgUnknown = 5

class MediaDataType:	
	GPS   = 1
	AUDIO = 2
	VIDEO = 3
	IMAGE = 4
	TEXT = 5
	IODATA =6
	RAWBLOB = 10
	UNDEFINED = 0xff

class MediaData_Base:
	def __init__(self,mst):
		self.mst = mst
	
	def getType(self):
		return self.mst
	
	def getId(self):
		#这里是获得的module id,subclass必须支持
		return ''
	
	def  encode(self):
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
	
	def getId(self):
		return self.hwid
	
	def __str__(self):
		return self.hwid,self.lon,self.lat,self.speed,self.angle,self.satenum,self.sateused,self.time
	
	#encode to json
	def encode(self):
		s ={'hwid':self.hwid}
		return s
		
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
		
		
class AlarmType:
	SpeedOver = 'speedover' 			#高速报警
	SpeedLower ='speedlower'			#低速报警
	BarrierLimitIn = 'barrier_in'		#入区域报警
	BarrierLimitOut = 'barrier_out'		#出报警
	GpsModuleKeyPress= 'modulekeypress' 				#ao模块触发紧急报警
	SOS ='sos'							#车辆劫警（SOS求助）
	ROB ='rob'							#车辆防盗器警报,
	MilesUpLimit = 'milesuplimit' 		#里程超标
	GpsLost = 'gpslost'					#不能定位报警
	Offline = 'offline'					#设备掉线报警 ，长时间与中心失去联系
	PowerLost ='powerlost'				#设备掉电报警
	value ={
		SpeedOver: 1,
		SpeedLower:2,
		BarrierLimitIn: 3,
		BarrierLimitOut:4,
		SOS:5,
		ROB:6,
		GpsLost:7,
		Offline:8,
		PowerLost:9
	}
	reverse = {
		1:SpeedOver,
		2:SpeedLower,
		3:BarrierLimitIn,
		4:BarrierLimitOut,
		5:SOS,
		6:ROB,
		7:GpsLost,
		8:Offline,
		9:PowerLost
	}

class TaskActionType_t:
	Sleep = 'sleep' 	#等待一定时间，单位：秒 , freq - 指定睡眠值
	Mail = 'mail'    #发送邮件
	SMS = 'sms' 	#发送短信
	NAMES={'sms':u'短信通知',
	       'mail':u'邮件通知',
	       'asi_detach':u'取消报警设防',
	       'poweroff':u'切断电源',
	       'oiloff':u'断油'
	       }
	
	
class ModuleMsgType:
	SYS2DEV = 1 #系统到设备
	DEV2SYS = 2 #设备到系统
	
	

class Alarm_BarrierTriggerType:
	IN=1
	OUT=2

