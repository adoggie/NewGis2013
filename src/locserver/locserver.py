#--coding:utf-8--


import os,os.path,sys,struct,time,traceback,signal

from base import *
from snsbase import geotools

import tcelib as tce
from sns_service import *
import map

from pymongo import MongoClient
from django.db import connection
from django.db.models import Sum
from django.db import transaction
import sns.core.models as cm

#struct LocationCachedObjectInfo_t{
#	string user_id;
#string user_type;
#LocationInfo_t loc;
#};

class LocationCachedObjectInfo_t:
	def __init__(self):
		self.user_id = ''
		self.user_type =''
		self.loc = None
		self.shared = False # default user hide location

class LocationRecieverImpl(ILocationReciever):
	def __init__(self,app):
		ILocationReciever.__init__(self)
		self.app = app

	def updateLocation(self,userid,loc,ctx):
#		loc = LocationCachedObjectInfo_t()
#		loc.user_id = int(userid)
#		loc.loc = loc
		userid = int(userid)
		self.app.locserver.update(userid,loc)

class LocationServerImpl(ILocationServer):
	def __init__(self,app):
		ILocationServer.__init__(self)
		self.app = app
		self.map = map.GlobalMap()
		self.mtxlocs = tce.utils.ReadWriteLock()
		self.locs ={}

	def searchNearestStrangers(self,case,ctx):
		#LocationCachedObjectInfo_t
		result =[]
		try:
			locs = self.map.spatialQuery(case)
			for loc in locs: # loc - LocationCachedObjectInfo_t
				r = StrangerInfo_t()
				r.userid =  loc.user_id
				r.usertype = loc.user_type
				r.loc = loc.loc
				result.append(r)
		except:
			print traceback.format_exc()

		return result

	def getLocations(self,user_ids,ctx):
		'''@return:
			LocationInfoList_t
			'''
		ids = map(int,user_ids)
		res =[]
		self.mtxlocs.acquire_read()
		for id  in ids:
			d = self.locs.get(id)
			if not loc: continue
			res.append(d.loc)
		self.mtxlocs.release_read()
		return res

	def shareLocation(self,show,ctx):
		userid = USER_ID(ctx)
		self.mtxlocs.acquire_write()
		d = self.locs.get(userid)
		if d:
			d.shared = show
		self.mtxlocs.release_write()

	def getMySettings(self,ctx):
		userid = USER_ID(ctx)
		info = UserLocationSettings_t()
		self.mtxlocs.acquire_read()
		d = self.locs.get(userid)
		if d:
			info.userid = d.user_id
			info.shared = d.shared
			info.type = d.user_type
		self.mtxlocs.release_read()
		return info


	def g2m(self,pt,ctx):
		x,y = geotools.point_g2m(pt.lon,pt.lat)
		print 'g2m: from(%s,%s) to(%s,%s)'%(pt.lon,pt.lat,x,y)
		return GeoPoint_t(x,y)
	#---------------------------------------------
	#following  local methods
	def update(self,userid,loc):

		self.mtxlocs.acquire_write()
		d = self.locs.get(userid)
		if not d :
			d = LocationCachedObjectInfo_t()
			d.user_id = userid
		d.loc = loc
		self.mtxlocs.release_write()
		self.map.update(d)


class MainApp():
	def __init__(self,confile=''):
		self.locserver = LocationServerImpl(self)
		self.locrecv = LocationRecieverImpl(self)

		self.adapter = None
		self.dbconn = None

		if not confile: confile='server.conf'
		self.conf = tce.utils.SimpleConfig()
		self.conf.load(confile)

	def getConfig(self):
		return self.conf

	def getNosqlDb(self):
		if not self.dbconn:
			host,port = self.getConfig().get('mongo.db.host'),int(self.getConfig().get('mongo.db.port'))
			self.dbconn = MongoClient(host, port)
		return self.dbconn

	def run(self):
		tce.RpcCommunicator.instance().init()
		if not tce.RpcMqSet.instance().init('loc1',file=GLOBAL_SERVICE_FILE):
			return -1
		self.adapter = tce.RpcCommunicator.instance().createAdapter('locs','mq_loc')
		self.adapter.addServant(self.locserver)
		self.adapter.addServant(self.locrecv)

		tce.RpcCommunicator.instance().run()



if __name__ == '__main__':
#	x,y = geotools.point_g2m(121.3445,31.3345)
#	print x,y
#	sys.exit()
	sys.exit( MainApp().run())
