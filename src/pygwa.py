#--coding:utf-8--


import os,os.path,sys,struct,time,traceback,signal,threading
sys.path.insert(0,'../tce/python')

import tcelib as tce
#from tce2 import *
from newgis import *
import uuid,copy
import cipher
import gevent
import utils

'''
记录每个合法登陆用户连接的活动信息 heartbeat
心跳超时则剔除
'''

HEARTBEAT_TIMEOUT = 20 # 20s之内必须接收到一个心跳

class GatewayAdatper(IGatewayAdapter):
	def __init__(self):
		IGatewayAdapter.__init__(self)
		self.mtxusers = threading.Lock()
		self.users={}   # {userid:heartbeat_time}
		gevent.spawn(self._workTask)

	def _workTask(self):
		while True:
			gevent.sleep(5)
#			print 'check user connection..'
			userids = []
			with self.mtxusers:
				for userid,tick in self.users.items():
					if int(time.time()) - tick > HEARTBEAT_TIMEOUT:
						userids.append(userid)
				for userid in userids:
					del self.users[userid]

			for userid in userids:
				self._userReject(userid)

	def _onLostConnection(self,conn):
		self._userReject(conn.userid)


	def login(self,token_,ctx):
		userinfo = cipher.decryptToken(token_)

		userid = userinfo['id']
		ctx.conn.setUserId(userid)

		prx  = IUserServicePrx.createWithEpName('mq_cts_1')
		serverid = tce.RpcCommunicator.instance().currentServer().getId()

		prx.userLogin_oneway(str(userid),str(serverid))

		print 'gwa login:',userinfo, prx,serverid
		with self.mtxusers:
			self.users[userid] =int(time.time())
		ctx.conn.cb_disconnect = self._onLostConnection

		return CallReturn_t(Error_t(True),value='login succ')

	def logout(self,ctx):
		userid = ctx.conn.userid
		if not userid:
			return
		self._userReject(userid)

	def _userReject(self,userid):

		prx  = IUserServicePrx.createWithEpName('mq_cts_1')
		serverid = tce.RpcCommunicator.instance().currentServer().getId()
		prx.userLogout_oneway(str(userid),str(serverid))


	def heartbeat(self,ctx):
		print 'GatewayAdatper::heartbeat',time.asctime()
		if not ctx.conn.userid:
			return -1

		userid = ctx.conn.userid
		with self.mtxusers:
			self.users[userid] =int(time.time())
		return 0


class DirectServer(GatewayAdatper):
	def __init__(self):
		GatewayAdatper.__init__(self)





def usage():
	print ' pygwa.py -type [gwa|direct] -name gwa1 -config services.xml -eps gwa1_socket,..'



def main():
	argv = copy.deepcopy(sys.argv)
	name = ''
	cfg =''
	eps=[]
	type='gwa' # or direct
	try:
		while argv:
			p = argv.pop(0)
			if p=='-type':
				type = argv.pop(0)
				if type not in ('gwa','direct'):
					usage()
					return
			if p =='-name':
				name = argv.pop(0)
			if p=='-config':
				cfg = argv.pop(0)
			if p == '-eps':
				eps = argv.pop(0)
				eps = eps.split(',')
	except:
		usage()
		return

	if not name or not cfg or not eps:
		usage()
		return


	tce.RpcCommunicator.instance().init(name,cfg)
	servant = None
	servant = GatewayAdatper()

	for ep in eps:
		id = uuid.uuid4()
		adapter = tce.RpcCommunicator.instance().createAdapter(id,ep)
		adapter.addServant(servant)
#		print adapter



#	print name,cfg,eps,type
	print 'service:',name,' started,waiting for shutdown..'
	tce.RpcCommunicator.instance().waitForShutdown()
	print 'service end.'

if __name__ == '__main__':
	utils.app_kill('pygwa')
	utils.app_init('pygwa')



	cmd = 'pygwa.py -type gwa -name gwa_1 -config ./services.xml -eps gwa_socket'
	sys.argv = cmd.split(' ')

	sys.exit( main())


#'''
#1.必须用户验证的gateway
#	pygwa.py -type gwa -name gwa_2 -config ./services.xml -eps gwa_websocket
#	pygwa.py -type gwa -name gwa_1 -config ./services.xml -eps gwa_socket
#2.无需认证的gateway
#	pygwa.py -type direct -name direct_2 -config ./services.xml -eps direct_websocket
#	pygwa.py -type direct -name direct_1 -config ./services.xml -eps direct_socket
#'''
