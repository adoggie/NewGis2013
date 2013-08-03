# -- coding:utf-8 --


import sys,os

import socket,traceback,os,os.path,sys,time,struct,base64,gzip,array,threading
import string
from xml.dom.minidom import  parseString as xmlParseString

import gevent
import gevent.event

def init_PYTHONPATH(xmlfile,tag='env'):
	f = open(xmlfile)
	d = f.read()
	f.close()
	doc = xmlParseString(d)
	r = doc.documentElement
	rs = r.getElementsByTagName(tag)
	if rs:
		e = rs[0]
		pathes = e.getAttribute('pythonpath').split(',')
		for p in pathes:
			sys.path.insert(0,p)

init_PYTHONPATH('config.xml')

import utils

os.environ['DJANGO_SETTINGS_MODULE'] = 'webservice.settings'

#from django.db import transaction
import webservice.giscore.models as CM
import tcelib as tce

from service import *
from aobject  import *

import newgis



##############################################################



#服务类型
class ServiceEntry:
	def __init__(self,name,proto,host,port,codecCLS):
		self.name = name
		self.proto = proto
		self.host = host
		self.port = port
		self.codec =codecCLS



class AoModuleCtrlImpl(newgis.IAoModuleCtrl):
	def __init__(self,app):
		newgis.IAoModuleCtrl.__init__(self)
		self.app = app


	def openListen(self,aoid_,phone_,ctx):
		ao = self.app.getActiveObject(aoid_)
		if not ao:
			return
		m = {'type':'aom_listen','phone':phone_}
		ao.sendData(m)

	def closeListen(self,aoid_,ctx):
		pass

	def getVersion(self,aoid_,ctx):
		return ''

	def onceNamed(self,aoid_,ctx):
		ao = self.app.getActiveObject(aoid_)
		if not ao:
			return
		m = {'type':'aom_oncenamed'}
		ao.sendData(m)


	def speedLimit(self,aoid_,high_,low_,ctx):
		ao = self.app.getActiveObject(aoid_)
		if not ao:
			return
		m = {'type':'aom_speedlimit_set','high':high_,'low':high_}
		ao.sendData(m)

	def oilCtrl(self,aoid_,onoff_,ctx):
		ao = self.app.getActiveObject(aoid_)
		if not ao:
			return
		m = {'type':'aom_oil_set','value':onoff_}
		ao.sendData(m)

	def reset(self,aoid_,ctx):
		ao = self.app.getActiveObject(aoid_)
		if not ao:
			return
		m = {'type':'aom_reset'}
		ao.sendData(m)

	def setFreqAccOn(self,aoid_,freq_,ctx):
		ao = self.app.getActiveObject(aoid_)
		if not ao:
			return
		m = {'type':'aom_accon_continued','value':freq_}
		ao.sendData(m)

	def setFreqAccOff(self,aoid_,freq_,ctx):
		ao = self.app.getActiveObject(aoid_)
		if not ao:
			return
		m = {'type':'aom_accoff_continued','value':freq_}
		ao.sendData(m)

	def setBarrierLeave(self,aoid_,x1_,y1_,x2_,y2_,ctx):
		pass

	def setBarrierEnter(self,aoid_,x1_,y1_,x2_,y2_,ctx):
		pass

	def clearAlarms(self,aoid_,ctx):
		ao = self.app.getActiveObject(aoid_)
		if not ao:
			return
		m = {'type':'aom_clear_alarms'}
		ao.sendData(m)

	def clearMiles(self,aoid_,miles,ctx):
		ao = self.app.getActiveObject(aoid_)
		if not ao:
			return
		m = {'type':'aom_init_miles','miles':miles}
		ao.sendData(m)

class DtuServiceImpl(newgis.IDtuService):
	def __init__(self,app):
		newgis.IDtuService.__init__(self)
		self.app = app


class AppServer:
	def __init__(self):
		self.services=[]

		self.sid='' #das id
		self.GM = None
		self.ctrlconn=None #与控制服务器的连接
		self.dbconn = None
		self.aos ={}	# {id:{ao,[module1,..]},..}
		self.mtxaos = threading.Lock()

		self.amoctrl = AoModuleCtrlImpl(self)
		self.svc = DtuServiceImpl(self)


	_handle = None
	@staticmethod
	def instance():
		if not AppServer._handle:
			AppServer._handle = AppServer()
		return AppServer._handle

	def join(self):
		self.stopmtx.wait()

	def _join_wait(self):

		while True:
			gevent.sleep(0.1)

	def main(self):
		self.init()
		self.stopmtx = gevent.event.Event()
		gevent.spawn(self._join_wait)
		self.join()
		#tce.RpcCommunicator.instance().waitForShutdown()
		#不能threading.Event()::wait()


	#初始化配置信息 
	def _initConfigs(self):
		f = open('config.xml')
		d = f.read()
		f.close()
		doc = xmlParseString(d)
		r = doc.documentElement

		e = r.getElementsByTagName('config')[0]
		name = e.getAttribute("name")
		file = e.getAttribute("file")

		# -- init rpc service --

		tce.RpcCommunicator.instance().init(name,file)
		self.adapter = tce.RpcCommunicator.instance().createAdapter('das','mq_dtu_1')
		self.server = DtuServiceImpl(self)
		self.adapter.addServant(self.server)
		self.aomctrl = AoModuleCtrlImpl(self)
		self.adapter.addServant(self.aomctrl)

		# -- begin adapter service ---
		e = r.getElementsByTagName('services')
		if not e:
			return False
		svcs = e[0].getElementsByTagName('service')

		for e in svcs:
			name = e.getAttribute('name')
			prot = e.getAttribute('proto')
			host = e.getAttribute('host')
			port = e.getAttribute('port')
			cls  = e.getAttribute('codec')
			enable = e.getAttribute('enable')
			if enable!='true':
				continue
			se = ServiceEntry(name,prot,host,port,cls)
			self.services.append(se)


	#初始化所有ao对象	
	def _initData(self):
		sid = tce.RpcCommunicator.instance().server.getId()
		print hex(sid)
		rs = self.getDbModule().ActiveObject.objects.filter(dasid='%04x'%sid)
		for r in rs:
			ao = ActiveObject_Base(r,self)
			self.aos[r.id] = ao



	def aoLoad(self,aoid):
		try:
			self.mtxaos.acquire()
			r = self.getDbModule().ActiveObject.objects.get(id=int(aoid))
			ao = ActiveObject_Base(r,self)
			self.aos[r.id] = ao

		except :
			traceback.print_exc()
			return False
		finally:
			self.mtxaos.release()
		return  True

#	由于系统运行管理中对ao进行增删改操作，需要及时通知到das服务器
	def aoUnload(self,aoid):
		try:
			self.mtxaos.acquire()
			if self.aos.has_key(aoid):
				ao = self.aos[aoid]
				del self.aos[aoid]
				ao.destroy()
			print 'unload ao:',aoid,' ok!'
		except:
			traceback.print_exc()
		finally:
			self.mtxaos.release()


	def init(self):
		r = self._initConfigs()	#配置信息
		r = self._initData()	#加载所有ao对象
		self.prx_aomclients = newgis.IAoModuleClientPrx.createWithEpName('mq_aom_clients')
		services = self.services
		self.services =[]
		for s in services:
			m = __import__(s.codec) #导入解码模块
			codecCLS = getattr(m,'MediaCodec') #动态获取 解码类
			svc = DaemonService_Tcp(self,(s.host,int(s.port)),self.aom_event,codecCLS)
			self.services.append(svc)

#		self.getLog().debug('dtuserver','started',time.asctime())

		
	#设备连接事件处理
	def aom_event(self,e):
		if e.type == DeviceEvent.INCOMMING_CONNECTED:
			pass
		elif e.type == DeviceEvent.DISCONNECTED:
			pass
		elif e.type == DeviceEvent.RECVED_DATA:
			print repr(e)
			m = e.data # 解析出来的消息包, codec.parseMessage()
			conn = e.conn
			if conn.aom:    #conn 已经与设备关联
				conn.aom.ao.readData(m,conn)
			else:
				print 'aom is null',m
				self.mtxaos.acquire()

				for ao in self.aos.values():
					if ao.readData(m,conn):#连接与AcitiveObject关联上了，之后的数据接收 将直接传递到ActiveObject.readData()
						break
				self.mtxaos.release()
			#next.将gps消息和报警消息传递给ctrlserver
	

	def getActiveObject(self,aoid):
		ao = None
		self.mtxaos.acquire()
		ao = self.aos.get(aoid,None)
		self.mtxaos.release()
		return ao

	def getDbModule(self):
		return CM

	def sendToModuleClient(self,aoid,m):
		'''
			发送给接收者
			解析消息类型到对应的
		'''

		if m.gps : #gps数据 保存
			gps = m.gps
			d = newgis.GpsData_t()
			d.lon = gps.lon
			d.lat = gps.lat
			d.speed = gps.speed
			d.direction = gps.angle
			d.time = gps.gpstime
			d.extra.power = gps.power
			d.extra.acc = gps.acc
			d.extra.miles = gps.miles
			d.extra.av = gps.av
			if self.prx_aomclients:
				print 'send prx_aomclients.onGetGpsData_oneway()',aoid,d
				self.prx_aomclients.onGetGpsData_oneway(aoid,d)   #发送到ctlrserver


appname ='das'
utils.app_kill(appname)
utils.app_init(appname)

if __name__=='__main__':
	AppServer().main()


					
	