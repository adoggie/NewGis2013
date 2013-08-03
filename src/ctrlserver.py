#--coding:utf-8--


import os,os.path,sys,struct,time,traceback,signal,threading


sys.path.insert(0,'../tce/python')
os.environ['DJANGO_SETTINGS_MODULE'] = 'webservice.settings'

from django.db import transaction
import webservice.giscore.models as cm
import tcelib as tce
from newgis import *
import cipher
from dbconn import *
from django.db import connection
import alarmserver
import gevent.coros
import utils

from xml.dom.minidom import  parseString as xmlParseString
import gevent.event

class UserInfo:
	def __init__(self):
		pass


class UserServiceImpl(IUserService):
	def __init__(self,app = None):
		IUserService.__init__(self)
		self.app = app
		self.users={}   # { userid:{gwaid,..}}
		self.mtxusers =  gevent.coros.Semaphore()


	def userLogin(self,userid,gwaid,ctx):
		print 'user login..'
		print 'gwa mq:',tce.RpcCommunicator.instance().getServiceReadMQName(gwaid),gwaid
		info={'gwaid':gwaid}
		self.mtxusers.acquire()
		self.users[userid] = info
		self.mtxusers.release()



	def userLogout(self,userid,gwaid,ctx):
		print 'user logout',userid,gwaid
		self.mtxusers.acquire()
		if self.users.has_key(userid):
			del self.users[userid]
		self.mtxusers.release()


	def sendLocationToUser(self,userid,aoid,loc):
		import geotools
		user = None
		userid = str(userid)

		self.mtxusers.acquire()
		user = self.users.get(userid)
		self.mtxusers.release()
#		print user,userid,aoid,loc
		print 'sendLocationToUser..',user,userid
		print self.users
		if not user:
			return


		loc.gps.lon,loc.gps.lat = geotools.point_g2m(loc.gps.lon,loc.gps.lat)

		gwaid = user['gwaid']
		mqname = tce.RpcCommunicator.instance().getServiceReadMQName(gwaid)
		prx = self.app.getUserClientProxy(mqname)
		print gwaid,mqname,prx
		if not prx:
			return
		extra = tce.Shortcuts.CALL_USER_ID(userid)

		prx.onGetLocation_oneway(aoid,loc,extra)

	def sendAlarmToUser(self,userid,aoid,alarm): # alarm - AlarmInfo_t
		user = None
		self.mtxusers.acquire()
		user = self.users.get(userid)
		self.mtxusers.release()
		if not user:
			return
		gwaid = user['gwaid']
		mqname = tce.RpcCommunicator.instance().getServiceReadMQName(gwaid)
		prx = self.app.getUserClientProxy(mqname)
		if not prx:
			return
		extra = tce.Shortcuts.CALL_USER_ID(userid)
		prx.onGetDeviceAlarm_oneway(aoid,alarm,extra)

class AuthServiceImpl(IAuthService):
	def __init__(self,app = None):
		IAuthService.__init__(self)
		self.app = app

	def userAuth(self,user_,passwd_,loginType_,ctx):
		token=''
		rs = cm.AppUser.objects.filter(sid=user_,passwd = passwd_)
		if rs:
			r = rs[0]
			user = {'id':r.id,'user':r.user,'login_time':int(time.time())}
			token = cipher.encryptToken(user)
		return token


class AoModuleClientImpl(IAoModuleClient):
	def __init__(self,app=None):
		IAoModuleClient.__init__(self)
		self.app = app

	def onGetGpsData(self,aoid,gps,ctx):
#		print 'onGetGpsData:',aoid,gps

		cur = connection.cursor()
		sql = 'select distinct appuser_id as userid from giscore_appuser_aos where activeobject_id=%s'%aoid
		cur.execute(sql)
		rs = fetchallDict(cur)
		loc = LocationInfo_t()
		loc.gps = gps
		for r in rs:
			self.app.usersvc.sendLocationToUser(r['userid'],aoid,loc)

		d = alarmserver.AoData(aoid,alarmserver.AoData.GPSDATA,gps)
		self.app.alarmsvc.onAoData(aoid,d)

class AlarmServiceImpl(IAlarmService,alarmserver.AlarmServer):
	'''
		报警服务器
	'''

	def __init__(self,app=None):
		IAlarmService.__init__(self)
		alarmserver.AlarmServer.__init__(self,app)
		self.app = app
		alarmserver.AlarmServer.start(self)

	def addItem(self,aoid_,asid,ctx):
		self.asi_add(asid,aoid_)

	def removeItem(self,aoid,asid,ctx):
		self.asi_remove(asid,aoid)

class NotiServiceImpl(INotificationService):
	'''
		消息通知服务器
	'''
	def __init__(self,app = None):
		INotificationService.__init__(self)


import taskserver
class TaskServiceImpl(ITaskService,taskserver.TaskServer):
	'''
		任务服务器
	'''

	def __init__(self,app=None):
		ITaskService.__init__(self)
		taskserver.TaskServer.__init__(self,app)
		self.app = app
		taskserver.TaskServer.start(self)


class AoModuleCtrlImpl(IAoModuleCtrl):
	def __init__(self,app):
		IAoModuleCtrl.__init__(self)
		self.app = app


	def openListen(self,aoid_,phone_,ctx):
		prx = self.app.getDtuServerProxy(aoid_)
		if not prx:return
		prx = IAoModuleClientPrx.createWithProxy(prx)
		prx.openListen_oneway(aoid_,phone_)

	def closeListen(self,aoid_,ctx):
		prx = self.app.getDtuServerProxy(aoid_)
		if not prx:return
		prx = IAoModuleClientPrx.createWithProxy(prx)

	def getVersion(self,aoid_,ctx):
		return ''

	def onceNamed(self,aoid_,ctx):
		prx = self.app.getDtuServerProxy(aoid_)
		if not prx:return
		prx = IAoModuleClientPrx.createWithProxy(prx)
		prx.onceNamded(aoid_)

	def speedLimit(self,aoid_,high_,low_,ctx):
		prx = self.app.getDtuServerProxy(aoid_)
		if not prx:return
		prx = IAoModuleClientPrx.createWithProxy(prx)
		prx.speedLimit(aoid_,high_,low_)

	def oilCtrl(self,aoid_,onoff_,ctx):
		prx = self.app.getDtuServerProxy(aoid_)
		if not prx:return
		prx = IAoModuleClientPrx.createWithProxy(prx)
		prx.oilCtrl(aoid_,onoff_)

	def reset(self,aoid_,ctx):
		prx = self.app.getDtuServerProxy(aoid_)
		if not prx:return
		prx = IAoModuleClientPrx.createWithProxy(prx)
		prx.reset(aoid_)

	def setFreqAccOn(self,aoid_,freq_,ctx):
		prx = self.app.getDtuServerProxy(aoid_)
		if not prx:return
		prx = IAoModuleClientPrx.createWithProxy(prx)
		prx.setFreqAccOn(aoid_,freq_)

	def setFreqAccOff(self,aoid_,freq_,ctx):
		prx = self.app.getDtuServerProxy(aoid_)
		if not prx:return
		prx = IAoModuleClientPrx.createWithProxy(prx)
		prx.setFreqAccOff(aoid_,freq_)

	def setBarrierLeave(self,aoid_,x1_,y1_,x2_,y2_,ctx):
		prx = self.app.getDtuServerProxy(aoid_)
		if not prx:return
		prx = IAoModuleClientPrx.createWithProxy(prx)

	def setBarrierEnter(self,aoid_,x1_,y1_,x2_,y2_,ctx):
		prx = self.app.getDtuServerProxy(aoid_)
		if not prx:return
		prx = IAoModuleClientPrx.createWithProxy(prx)

	def clearAlarms(self,aoid_,ctx):
		prx = self.app.getDtuServerProxy(aoid_)
		if not prx:return
		prx = IAoModuleClientPrx.createWithProxy(prx)
		prx.clearAlarms(aoid_)

	def clearMiles(self,aoid_,miles,ctx):
		prx = self.app.getDtuServerProxy(aoid_)
		if not prx:return
		prx = IAoModuleClientPrx.createWithProxy(prx)
		prx.clearMiles(aoid_,miles)

class AppServer:
	def __init__(self):
		self.clientproxies = {}
		self.dtuserver_proxies ={}

	_handle = None

	@staticmethod
	def instance():
		if not AppServer._handle:
			AppServer._handle = AppServer()
		return AppServer._handle

	def main(self):
		tce.RpcCommunicator.instance().init('cts_1','./services.xml')

		adapter = tce.RpcCommunicator.instance().createAdapter('first_server','mq_cts_1')
		print 'adapter:',adapter
		self.usersvc = UserServiceImpl(self)
		adapter.addServant(self.usersvc)
		self.authsvr = AuthServiceImpl(self)
		adapter.addServant(self.authsvr)


		self.aomctrl = AoModuleCtrlImpl(self)
		adapter.addServant(self.aomctrl)


		self.alarmsvc = AlarmServiceImpl(self)
		adapter.addServant(self.alarmsvc)
		self.tasksvc = TaskServiceImpl(self)
		adapter.addServant(self.tasksvc)

		#-- second adatper --
		adapter = tce.RpcCommunicator.instance().createAdapter('2','mq_aom_clients')
		self.aomclient = AoModuleClientImpl(self)
		adapter.addServant(self.aomclient)

		print 'ctlrserver launched..'
		tce.RpcCommunicator.instance().waitForShutdown()

	def getUserClientProxy(self,mqname):
		prx = IUserClientPrx.createWithEpName(mqname)
		return prx

	def getDtuServerProxy(self,aoid):
		aoid = int(aoid)
		rs = cm.ActiveObject.objects.filter(id=aoid)
		if not rs:
			return None
		dasid = rs[0].dasid
		dasid = int(dasid,16) # db中存储的das的id，以16进制保存
		mq = tce.RpcCommunicator.instance().getServiceReadMQName(dasid)
		prx = self.dtuserver_proxies.get(mq)
		if not prx:
			prx = IDtuServicePrx.createWithEpName(mq)
		return prx

	def getDBModule(self):
		return cm


	def getDBConn(self):
		return connection

appname ='ctrlserver'
utils.app_kill(appname)
utils.app_init(appname)



if __name__ == '__main__':
	sys.exit( AppServer.instance().main())

