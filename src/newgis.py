
# -- coding:utf-8 --

#---------------------------------
#  TCE
#  Tiny Communication Engine
#
#  sw2us.com copyright @2012
#  bin.zhang@sw2us.com / qq:24509826
#---------------------------------

import os,os.path,sys,struct,time,traceback,time
import tcelib as tce

	
class StringList_t:
	# -- SEQUENCE --
	def __init__(self,array):
		self.ds = array
		
	def marshall(self):
		d = '' 
		d += struct.pack('!I',len(self.ds))
		for o in self.ds:
			if type(o)==type(0) or type(o) == type(0.1): o=str(o)
			if not o: o=''
			try:
				o = o.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(o)))
			d += str(o)
		return d
		
	def unmarshall(self,d,idx_=0):
		idx = idx_
		try:
			size_,= struct.unpack('!I',d[idx:idx+4])
			idx += 4
			p = 0
			while p < size_:
				size, = struct.unpack('!I',d[idx:idx+4])
				idx+=4
				v = d[idx:idx+size]
				idx+=size
				self.ds.append(v)
				p+=1
		except:
			traceback.print_exc()
			return False,idx
		return True,idx

class IntList_t:
	# -- SEQUENCE --
	def __init__(self,array):
		self.ds = array
		
	def marshall(self):
		d = '' 
		d += struct.pack('!I',len(self.ds))
		for o in self.ds:
			d += struct.pack('!i',o)
		return d
		
	def unmarshall(self,d,idx_=0):
		idx = idx_
		try:
			size_,= struct.unpack('!I',d[idx:idx+4])
			idx += 4
			p = 0
			while p < size_:
				v, = struct.unpack('!i',d[idx:idx+4])
				idx+=4
				self.ds.append(v)
				p+=1
		except:
			traceback.print_exc()
			return False,idx
		return True,idx

class UserIdList_t:
	# -- SEQUENCE --
	def __init__(self,array):
		self.ds = array
		
	def marshall(self):
		d = '' 
		d += struct.pack('!I',len(self.ds))
		for o in self.ds:
			if type(o)==type(0) or type(o) == type(0.1): o=str(o)
			if not o: o=''
			try:
				o = o.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(o)))
			d += str(o)
		return d
		
	def unmarshall(self,d,idx_=0):
		idx = idx_
		try:
			size_,= struct.unpack('!I',d[idx:idx+4])
			idx += 4
			p = 0
			while p < size_:
				size, = struct.unpack('!I',d[idx:idx+4])
				idx+=4
				v = d[idx:idx+size]
				idx+=size
				self.ds.append(v)
				p+=1
		except:
			traceback.print_exc()
			return False,idx
		return True,idx

class SIDS_t:
	# -- SEQUENCE --
	def __init__(self,array):
		self.ds = array
		
	def marshall(self):
		d = '' 
		d += struct.pack('!I',len(self.ds))
		for o in self.ds:
			if type(o)==type(0) or type(o) == type(0.1): o=str(o)
			if not o: o=''
			try:
				o = o.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(o)))
			d += str(o)
		return d
		
	def unmarshall(self,d,idx_=0):
		idx = idx_
		try:
			size_,= struct.unpack('!I',d[idx:idx+4])
			idx += 4
			p = 0
			while p < size_:
				size, = struct.unpack('!I',d[idx:idx+4])
				idx+=4
				v = d[idx:idx+size]
				idx+=size
				self.ds.append(v)
				p+=1
		except:
			traceback.print_exc()
			return False,idx
		return True,idx

class Properties_t:
	# -- THIS IS DICTIONARY! --
	def __init__(self,ds={}):
		self.ds = ds
		
	def marshall(self):
		d = '' 
		d += struct.pack('!I',len(self.ds.keys()))
		for k,v in self.ds.items():
			if type(k)==type(0) or type(k) == type(0.1): k=str(k)
			if not k: k=''
			try:
				k = k.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(k)))
			d += str(k)
			if type(v)==type(0) or type(v) == type(0.1): v=str(v)
			if not v: v=''
			try:
				v = v.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(v)))
			d += str(v)
		return d
		
	def unmarshall(self,d,idx_=0):
		idx = idx_
		try:
			_size,= struct.unpack('!I',d[idx:idx+4])
			p = 0
			idx += 4
			while p < _size:
				size, = struct.unpack('!I',d[idx:idx+4])
				idx+=4
				x = d[idx:idx+size]
				idx+=size
				size, = struct.unpack('!I',d[idx:idx+4])
				idx+=4
				y = d[idx:idx+size]
				idx+=size
				self.ds[x] = y
				p+=1
		except:
			traceback.print_exc()
			return False,idx
		return True,idx

class StreamBytes_t:
	# -- SEQUENCE --
	def __init__(self,array):
		self.ds = array
		
	def marshall(self):
		d = '' 
		d += struct.pack('!I',len(self.ds))
		d+=self.ds
		return d
		
	def unmarshall(self,d,idx_=0):
		idx = idx_
		try:
			size_,= struct.unpack('!I',d[idx:idx+4])
			idx += 4
			self.ds = d[idx:idx+4]
			idx+=size_
		except:
			traceback.print_exc()
			return False,idx
		return True,idx

class StringIdList_t:
	# -- SEQUENCE --
	def __init__(self,array):
		self.ds = array
		
	def marshall(self):
		d = '' 
		d += struct.pack('!I',len(self.ds))
		for o in self.ds:
			if type(o)==type(0) or type(o) == type(0.1): o=str(o)
			if not o: o=''
			try:
				o = o.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(o)))
			d += str(o)
		return d
		
	def unmarshall(self,d,idx_=0):
		idx = idx_
		try:
			size_,= struct.unpack('!I',d[idx:idx+4])
			idx += 4
			p = 0
			while p < size_:
				size, = struct.unpack('!I',d[idx:idx+4])
				idx+=4
				v = d[idx:idx+size]
				idx+=size
				self.ds.append(v)
				p+=1
		except:
			traceback.print_exc()
			return False,idx
		return True,idx

class ImageData_t:
	# -- SEQUENCE --
	def __init__(self,array):
		self.ds = array
		
	def marshall(self):
		d = '' 
		d += struct.pack('!I',len(self.ds))
		d+=self.ds
		return d
		
	def unmarshall(self,d,idx_=0):
		idx = idx_
		try:
			size_,= struct.unpack('!I',d[idx:idx+4])
			idx += 4
			self.ds = d[idx:idx+4]
			idx+=size_
		except:
			traceback.print_exc()
			return False,idx
		return True,idx

class ImageDataList_t:
	# -- SEQUENCE --
	def __init__(self,array):
		self.ds = array
		
	def marshall(self):
		d = '' 
		d += struct.pack('!I',len(self.ds))
		for o in self.ds:
			container = ImageData_t(o)
			d += container.marshall()
		return d
		
	def unmarshall(self,d,idx_=0):
		idx = idx_
		try:
			size_,= struct.unpack('!I',d[idx:idx+4])
			idx += 4
			p = 0
			while p < size_:
				o =[]
				container = ImageData_t(o)
				r,idx = container.unmarshall(d,idx)
				if not r: return False,idx
				self.ds.append(o)
				p+=1
		except:
			traceback.print_exc()
			return False,idx
		return True,idx

class MessageImage_t:
# -- STRUCT -- 
	def __init__(self,type=0,width=0,height=0,data='',data64=''):
		self.type = type
		self.width = width
		self.height = height
		self.data = data
		self.data64 = data64
		
	def __str__(self):
		return 'OBJECT<MessageImage_t :%s> { type:%s,width:%s,height:%s,data:%s,data64:%s}'%(hex(id(self)),str(self.type),str(self.width),str(self.height),str(self.data),str(self.data64) ) 
		
	def marshall(self):
		d =''
		d += struct.pack('!i',self.type)
		d += struct.pack('!i',self.width)
		d += struct.pack('!i',self.height)
		container = ImageData_t(self.data)
		d += container.marshall()
		if type(self.data64)==type(0) or type(self.data64) == type(0.1): self.data64=str(self.data64)
		if not self.data64: self.data64=''
		try:
			self.data64 = self.data64.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.data64)))
		d += str(self.data64)
		return d
		
	def unmarshall(self,d,idx_=0):
		idx = idx_
		try:
			self.type, = struct.unpack('!i',d[idx:idx+4])
			idx+=4
			self.width, = struct.unpack('!i',d[idx:idx+4])
			idx+=4
			self.height, = struct.unpack('!i',d[idx:idx+4])
			idx+=4
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.data = d[idx:idx+size]
			idx+=size
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.data64 = d[idx:idx+size]
			idx+=size
		except:
			traceback.print_exc()
			return False,idx
		return True,idx
		

class GeoPoint_t:
# -- STRUCT -- 
	def __init__(self,lon=0.0,lat=0.0):
		self.lon = lon
		self.lat = lat
		
	def __str__(self):
		return 'OBJECT<GeoPoint_t :%s> { lon:%s,lat:%s}'%(hex(id(self)),str(self.lon),str(self.lat) ) 
		
	def marshall(self):
		d =''
		d += struct.pack('!f',self.lon)
		d += struct.pack('!f',self.lat)
		return d
		
	def unmarshall(self,d,idx_=0):
		idx = idx_
		try:
			self.lon, = struct.unpack('!f',d[idx:idx+4])
			idx+=4
			self.lat, = struct.unpack('!f',d[idx:idx+4])
			idx+=4
		except:
			traceback.print_exc()
			return False,idx
		return True,idx
		

class GeoSize_t:
# -- STRUCT -- 
	def __init__(self,cx=0.0,cy=0.0):
		self.cx = cx
		self.cy = cy
		
	def __str__(self):
		return 'OBJECT<GeoSize_t :%s> { cx:%s,cy:%s}'%(hex(id(self)),str(self.cx),str(self.cy) ) 
		
	def marshall(self):
		d =''
		d += struct.pack('!f',self.cx)
		d += struct.pack('!f',self.cy)
		return d
		
	def unmarshall(self,d,idx_=0):
		idx = idx_
		try:
			self.cx, = struct.unpack('!f',d[idx:idx+4])
			idx+=4
			self.cy, = struct.unpack('!f',d[idx:idx+4])
			idx+=4
		except:
			traceback.print_exc()
			return False,idx
		return True,idx
		

class GeoCircle_t:
# -- STRUCT -- 
	def __init__(self,center=GeoPoint_t(),radius=0.0):
		self.center = center
		self.radius = radius
		
	def __str__(self):
		return 'OBJECT<GeoCircle_t :%s> { center:%s,radius:%s}'%(hex(id(self)),str(self.center),str(self.radius) ) 
		
	def marshall(self):
		d =''
		d += self.center.marshall()
		d += struct.pack('!f',self.radius)
		return d
		
	def unmarshall(self,d,idx_=0):
		idx = idx_
		try:
			r,idx = self.center.unmarshall(d,idx)
			if not r: return False,idx
			self.radius, = struct.unpack('!f',d[idx:idx+4])
			idx+=4
		except:
			traceback.print_exc()
			return False,idx
		return True,idx
		

class GeoRect_t:
# -- STRUCT -- 
	def __init__(self,x=0.0,y=0.0,width=0.0,height=0.0):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		
	def __str__(self):
		return 'OBJECT<GeoRect_t :%s> { x:%s,y:%s,width:%s,height:%s}'%(hex(id(self)),str(self.x),str(self.y),str(self.width),str(self.height) ) 
		
	def marshall(self):
		d =''
		d += struct.pack('!f',self.x)
		d += struct.pack('!f',self.y)
		d += struct.pack('!f',self.width)
		d += struct.pack('!f',self.height)
		return d
		
	def unmarshall(self,d,idx_=0):
		idx = idx_
		try:
			self.x, = struct.unpack('!f',d[idx:idx+4])
			idx+=4
			self.y, = struct.unpack('!f',d[idx:idx+4])
			idx+=4
			self.width, = struct.unpack('!f',d[idx:idx+4])
			idx+=4
			self.height, = struct.unpack('!f',d[idx:idx+4])
			idx+=4
		except:
			traceback.print_exc()
			return False,idx
		return True,idx
		

class GpsExtraData_t:
# -- STRUCT -- 
	def __init__(self,miles=0,power=0,acc=0,av=0):
		self.miles = miles
		self.power = power
		self.acc = acc
		self.av = av
		
	def __str__(self):
		return 'OBJECT<GpsExtraData_t :%s> { miles:%s,power:%s,acc:%s,av:%s}'%(hex(id(self)),str(self.miles),str(self.power),str(self.acc),str(self.av) ) 
		
	def marshall(self):
		d =''
		d += struct.pack('!i',self.miles)
		d += struct.pack('!i',self.power)
		d += struct.pack('!i',self.acc)
		d += struct.pack('!i',self.av)
		return d
		
	def unmarshall(self,d,idx_=0):
		idx = idx_
		try:
			self.miles, = struct.unpack('!i',d[idx:idx+4])
			idx+=4
			self.power, = struct.unpack('!i',d[idx:idx+4])
			idx+=4
			self.acc, = struct.unpack('!i',d[idx:idx+4])
			idx+=4
			self.av, = struct.unpack('!i',d[idx:idx+4])
			idx+=4
		except:
			traceback.print_exc()
			return False,idx
		return True,idx
		

class GpsData_t:
# -- STRUCT -- 
	def __init__(self,lon=0.0,lat=0.0,speed=0.0,direction=0.0,time=0,extra=GpsExtraData_t()):
		self.lon = lon
		self.lat = lat
		self.speed = speed
		self.direction = direction
		self.time = time
		self.extra = extra
		
	def __str__(self):
		return 'OBJECT<GpsData_t :%s> { lon:%s,lat:%s,speed:%s,direction:%s,time:%s,extra:%s}'%(hex(id(self)),str(self.lon),str(self.lat),str(self.speed),str(self.direction),str(self.time),str(self.extra) ) 
		
	def marshall(self):
		d =''
		d += struct.pack('!f',self.lon)
		d += struct.pack('!f',self.lat)
		d += struct.pack('!f',self.speed)
		d += struct.pack('!f',self.direction)
		d += struct.pack('!i',self.time)
		d += self.extra.marshall()
		return d
		
	def unmarshall(self,d,idx_=0):
		idx = idx_
		try:
			self.lon, = struct.unpack('!f',d[idx:idx+4])
			idx+=4
			self.lat, = struct.unpack('!f',d[idx:idx+4])
			idx+=4
			self.speed, = struct.unpack('!f',d[idx:idx+4])
			idx+=4
			self.direction, = struct.unpack('!f',d[idx:idx+4])
			idx+=4
			self.time, = struct.unpack('!i',d[idx:idx+4])
			idx+=4
			r,idx = self.extra.unmarshall(d,idx)
			if not r: return False,idx
		except:
			traceback.print_exc()
			return False,idx
		return True,idx
		

class LocationInfo_t:
# -- STRUCT -- 
	def __init__(self,gps=GpsData_t(),desc=''):
		self.gps = gps
		self.desc = desc
		
	def __str__(self):
		return 'OBJECT<LocationInfo_t :%s> { gps:%s,desc:%s}'%(hex(id(self)),str(self.gps),str(self.desc) ) 
		
	def marshall(self):
		d =''
		d += self.gps.marshall()
		if type(self.desc)==type(0) or type(self.desc) == type(0.1): self.desc=str(self.desc)
		if not self.desc: self.desc=''
		try:
			self.desc = self.desc.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.desc)))
		d += str(self.desc)
		return d
		
	def unmarshall(self,d,idx_=0):
		idx = idx_
		try:
			r,idx = self.gps.unmarshall(d,idx)
			if not r: return False,idx
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.desc = d[idx:idx+size]
			idx+=size
		except:
			traceback.print_exc()
			return False,idx
		return True,idx
		

class LocationInfoList_t:
	# -- SEQUENCE --
	def __init__(self,array):
		self.ds = array
		
	def marshall(self):
		d = '' 
		d += struct.pack('!I',len(self.ds))
		for o in self.ds:
			d += o.marshall()
		return d
		
	def unmarshall(self,d,idx_=0):
		idx = idx_
		try:
			size_,= struct.unpack('!I',d[idx:idx+4])
			idx += 4
			p = 0
			while p < size_:
				o = LocationInfo_t()
				r,idx = o.unmarshall(d,idx)
				if not r: return False,idx
				self.ds.append(o)
				p+=1
		except:
			traceback.print_exc()
			return False,idx
		return True,idx

class AlarmInfo_t:
# -- STRUCT -- 
	def __init__(self,type='',params=''):
		self.type = type
		self.params = params
		
	def __str__(self):
		return 'OBJECT<AlarmInfo_t :%s> { type:%s,params:%s}'%(hex(id(self)),str(self.type),str(self.params) ) 
		
	def marshall(self):
		d =''
		if type(self.type)==type(0) or type(self.type) == type(0.1): self.type=str(self.type)
		if not self.type: self.type=''
		try:
			self.type = self.type.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.type)))
		d += str(self.type)
		if type(self.params)==type(0) or type(self.params) == type(0.1): self.params=str(self.params)
		if not self.params: self.params=''
		try:
			self.params = self.params.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.params)))
		d += str(self.params)
		return d
		
	def unmarshall(self,d,idx_=0):
		idx = idx_
		try:
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.type = d[idx:idx+size]
			idx+=size
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.params = d[idx:idx+size]
			idx+=size
		except:
			traceback.print_exc()
			return False,idx
		return True,idx
		

class MessageText_t:
# -- STRUCT -- 
	def __init__(self,type=0,content=''):
		self.type = type
		self.content = content
		
	def __str__(self):
		return 'OBJECT<MessageText_t :%s> { type:%s,content:%s}'%(hex(id(self)),str(self.type),str(self.content) ) 
		
	def marshall(self):
		d =''
		d += struct.pack('!i',self.type)
		if type(self.content)==type(0) or type(self.content) == type(0.1): self.content=str(self.content)
		if not self.content: self.content=''
		try:
			self.content = self.content.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.content)))
		d += str(self.content)
		return d
		
	def unmarshall(self,d,idx_=0):
		idx = idx_
		try:
			self.type, = struct.unpack('!i',d[idx:idx+4])
			idx+=4
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.content = d[idx:idx+size]
			idx+=size
		except:
			traceback.print_exc()
			return False,idx
		return True,idx
		

class AuthToken_t:
# -- STRUCT -- 
	def __init__(self,user_id='',user_name='',user_realname='',login_time=0,login_type=0,expire_time=0,rights='',user_type=0):
		self.user_id = user_id
		self.user_name = user_name
		self.user_realname = user_realname
		self.login_time = login_time
		self.login_type = login_type
		self.expire_time = expire_time
		self.rights = rights
		self.user_type = user_type
		
	def __str__(self):
		return 'OBJECT<AuthToken_t :%s> { user_id:%s,user_name:%s,user_realname:%s,login_time:%s,login_type:%s,expire_time:%s,rights:%s,user_type:%s}'%(hex(id(self)),str(self.user_id),str(self.user_name),str(self.user_realname),str(self.login_time),str(self.login_type),str(self.expire_time),str(self.rights),str(self.user_type) ) 
		
	def marshall(self):
		d =''
		if type(self.user_id)==type(0) or type(self.user_id) == type(0.1): self.user_id=str(self.user_id)
		if not self.user_id: self.user_id=''
		try:
			self.user_id = self.user_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.user_id)))
		d += str(self.user_id)
		if type(self.user_name)==type(0) or type(self.user_name) == type(0.1): self.user_name=str(self.user_name)
		if not self.user_name: self.user_name=''
		try:
			self.user_name = self.user_name.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.user_name)))
		d += str(self.user_name)
		if type(self.user_realname)==type(0) or type(self.user_realname) == type(0.1): self.user_realname=str(self.user_realname)
		if not self.user_realname: self.user_realname=''
		try:
			self.user_realname = self.user_realname.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.user_realname)))
		d += str(self.user_realname)
		d += struct.pack('!i',self.login_time)
		d += struct.pack('!i',self.login_type)
		d += struct.pack('!i',self.expire_time)
		if type(self.rights)==type(0) or type(self.rights) == type(0.1): self.rights=str(self.rights)
		if not self.rights: self.rights=''
		try:
			self.rights = self.rights.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.rights)))
		d += str(self.rights)
		d += struct.pack('!i',self.user_type)
		return d
		
	def unmarshall(self,d,idx_=0):
		idx = idx_
		try:
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.user_id = d[idx:idx+size]
			idx+=size
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.user_name = d[idx:idx+size]
			idx+=size
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.user_realname = d[idx:idx+size]
			idx+=size
			self.login_time, = struct.unpack('!i',d[idx:idx+4])
			idx+=4
			self.login_type, = struct.unpack('!i',d[idx:idx+4])
			idx+=4
			self.expire_time, = struct.unpack('!i',d[idx:idx+4])
			idx+=4
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.rights = d[idx:idx+size]
			idx+=size
			self.user_type, = struct.unpack('!i',d[idx:idx+4])
			idx+=4
		except:
			traceback.print_exc()
			return False,idx
		return True,idx
		

class Error_t:
# -- STRUCT -- 
	def __init__(self,succ=False,code=0,msg=''):
		self.succ = succ
		self.code = code
		self.msg = msg
		
	def __str__(self):
		return 'OBJECT<Error_t :%s> { succ:%s,code:%s,msg:%s}'%(hex(id(self)),str(self.succ),str(self.code),str(self.msg) ) 
		
	def marshall(self):
		d =''
		if self.succ == True:self.succ=1
		else: self.succ=0
		d += struct.pack('B',self.succ)
		d += struct.pack('!i',self.code)
		if type(self.msg)==type(0) or type(self.msg) == type(0.1): self.msg=str(self.msg)
		if not self.msg: self.msg=''
		try:
			self.msg = self.msg.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.msg)))
		d += str(self.msg)
		return d
		
	def unmarshall(self,d,idx_=0):
		idx = idx_
		try:
			self.succ, = struct.unpack('B',d[idx:idx+1])
			if self.succ == 0: self.succ = False
			else: self.succ = True
			idx+=1
			self.code, = struct.unpack('!i',d[idx:idx+4])
			idx+=4
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.msg = d[idx:idx+size]
			idx+=size
		except:
			traceback.print_exc()
			return False,idx
		return True,idx
		

class CallReturn_t:
# -- STRUCT -- 
	def __init__(self,error=Error_t(),value=''):
		self.error = error
		self.value = value
		
	def __str__(self):
		return 'OBJECT<CallReturn_t :%s> { error:%s,value:%s}'%(hex(id(self)),str(self.error),str(self.value) ) 
		
	def marshall(self):
		d =''
		d += self.error.marshall()
		if type(self.value)==type(0) or type(self.value) == type(0.1): self.value=str(self.value)
		if not self.value: self.value=''
		try:
			self.value = self.value.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.value)))
		d += str(self.value)
		return d
		
	def unmarshall(self,d,idx_=0):
		idx = idx_
		try:
			r,idx = self.error.unmarshall(d,idx)
			if not r: return False,idx
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.value = d[idx:idx+size]
			idx+=size
		except:
			traceback.print_exc()
			return False,idx
		return True,idx
		

class TimeRange_t:
# -- STRUCT -- 
	def __init__(self,start=0,end=0):
		self.start = start
		self.end = end
		
	def __str__(self):
		return 'OBJECT<TimeRange_t :%s> { start:%s,end:%s}'%(hex(id(self)),str(self.start),str(self.end) ) 
		
	def marshall(self):
		d =''
		d += struct.pack('!i',self.start)
		d += struct.pack('!i',self.end)
		return d
		
	def unmarshall(self,d,idx_=0):
		idx = idx_
		try:
			self.start, = struct.unpack('!i',d[idx:idx+4])
			idx+=4
			self.end, = struct.unpack('!i',d[idx:idx+4])
			idx+=4
		except:
			traceback.print_exc()
			return False,idx
		return True,idx
		

class IUserClient:
	# -- INTERFACE -- 
	def __init__(self):
		if not hasattr(self,'delegatecls'):
			self.delegatecls = {}
		self.delegatecls[0] = IUserClient_delegate
	
	def onGetLocation(self,aoid_,loc_,ctx):
		pass
	
	def onGetMessage(self,userid_,msg_,ctx):
		pass
	
	def onGetDeviceAlarm(self,aoid_,alarm_,ctx):
		pass
	

class IUserClient_delegate:
	def __init__(self,inst,adapter,conn=None):
		self.index = 0
		self.optlist={}
		self.id = '' 
		self.adapter = adapter
		self.optlist[0] = (self.onGetLocation)
		self.optlist[1] = (self.onGetMessage)
		self.optlist[2] = (self.onGetDeviceAlarm)
		
		self.inst = inst
	
	def onGetLocation(self,ctx):
		print "callin (onGetLocation)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_aoid_ = d[idx:idx+size]
		idx+=size
		_p_loc_ = LocationInfo_t()
		r,idx = _p_loc_.unmarshall(d,idx)
		if not r: return False
		cr = None
		self.inst.onGetLocation(_p_aoid_,_p_loc_,ctx)
		return True
	
	def onGetMessage(self,ctx):
		print "callin (onGetMessage)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_userid_ = d[idx:idx+size]
		idx+=size
		_p_msg_ = MessageText_t()
		r,idx = _p_msg_.unmarshall(d,idx)
		if not r: return False
		cr = None
		self.inst.onGetMessage(_p_userid_,_p_msg_,ctx)
		return True
	
	def onGetDeviceAlarm(self,ctx):
		print "callin (onGetDeviceAlarm)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_aoid_ = d[idx:idx+size]
		idx+=size
		_p_alarm_ = AlarmInfo_t()
		r,idx = _p_alarm_.unmarshall(d,idx)
		if not r: return False
		cr = None
		self.inst.onGetDeviceAlarm(_p_aoid_,_p_alarm_,ctx)
		return True
	
	
class IUserClientPrx:
	# -- INTERFACE PROXY -- 
	def __init__(self,conn):
		self.conn = conn
		self.delta = None
		pass
	
	@staticmethod
	def create(address):
		conn = tce.RpcConnectionSocket()
		conn.open(address)
		proxy = IUserClientPrx(conn)
		return proxy
	
	@staticmethod
	def createWithEpName(name):
		ep = tce.RpcCommunicator.instance().currentServer().findEndPointByName(name)
		if not ep: return None
		conn = ep.impl
		proxy = IUserClientPrx(conn)
		return proxy
	
	@staticmethod
	def createWithProxy(prx):
		proxy = IUserClientPrx(prx.conn)
		return proxy
	
	#extra must be map<string,string>
	def onGetLocation(self,aoid_,loc_,timeout=None,extra={}):
		# function index: 24
		
		m = tce.RpcMessageCall()
		m.ifidx = 0
		m.opidx = 0
		m.extra.setStrDict(extra)
		d = '' 
		if type(aoid_)==type(0) or type(aoid_) == type(0.1): aoid_=str(aoid_)
		if not aoid_: aoid_=''
		try:
			aoid_ = aoid_.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(aoid_)))
		d += str(aoid_)
		m.paramstream += d
		d = '' 
		d += loc_.marshall()
		m.paramstream += d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		if not timeout: timeout = tce.RpcCommunicator.instance().getRpcCallTimeout()
		m2 = None
		try:
			m2 = m.mtx.get(timeout=timeout)
		except:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def onGetLocation_oneway(self,aoid_,loc_,extra={}):
		# function index: 24
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 0
			m.opidx = 0
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
			m.extra.setStrDict(extra)
			d = '' 
			if type(aoid_)==type(0) or type(aoid_) == type(0.1): aoid_=str(aoid_)
			if not aoid_: aoid_=''
			try:
				aoid_ = aoid_.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(aoid_)))
			d += str(aoid_)
			m.paramstream += d
			d = '' 
			d += loc_.marshall()
			m.paramstream += d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	#extra must be map<string,string>
	def onGetMessage(self,userid_,msg_,timeout=None,extra={}):
		# function index: 24
		
		m = tce.RpcMessageCall()
		m.ifidx = 0
		m.opidx = 1
		m.extra.setStrDict(extra)
		d = '' 
		if type(userid_)==type(0) or type(userid_) == type(0.1): userid_=str(userid_)
		if not userid_: userid_=''
		try:
			userid_ = userid_.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(userid_)))
		d += str(userid_)
		m.paramstream += d
		d = '' 
		d += msg_.marshall()
		m.paramstream += d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		if not timeout: timeout = tce.RpcCommunicator.instance().getRpcCallTimeout()
		m2 = None
		try:
			m2 = m.mtx.get(timeout=timeout)
		except:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def onGetMessage_oneway(self,userid_,msg_,extra={}):
		# function index: 24
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 0
			m.opidx = 1
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
			m.extra.setStrDict(extra)
			d = '' 
			if type(userid_)==type(0) or type(userid_) == type(0.1): userid_=str(userid_)
			if not userid_: userid_=''
			try:
				userid_ = userid_.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(userid_)))
			d += str(userid_)
			m.paramstream += d
			d = '' 
			d += msg_.marshall()
			m.paramstream += d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	#extra must be map<string,string>
	def onGetDeviceAlarm(self,aoid_,alarm_,timeout=None,extra={}):
		# function index: 24
		
		m = tce.RpcMessageCall()
		m.ifidx = 0
		m.opidx = 2
		m.extra.setStrDict(extra)
		d = '' 
		if type(aoid_)==type(0) or type(aoid_) == type(0.1): aoid_=str(aoid_)
		if not aoid_: aoid_=''
		try:
			aoid_ = aoid_.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(aoid_)))
		d += str(aoid_)
		m.paramstream += d
		d = '' 
		d += alarm_.marshall()
		m.paramstream += d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		if not timeout: timeout = tce.RpcCommunicator.instance().getRpcCallTimeout()
		m2 = None
		try:
			m2 = m.mtx.get(timeout=timeout)
		except:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def onGetDeviceAlarm_oneway(self,aoid_,alarm_,extra={}):
		# function index: 24
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 0
			m.opidx = 2
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
			m.extra.setStrDict(extra)
			d = '' 
			if type(aoid_)==type(0) or type(aoid_) == type(0.1): aoid_=str(aoid_)
			if not aoid_: aoid_=''
			try:
				aoid_ = aoid_.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(aoid_)))
			d += str(aoid_)
			m.paramstream += d
			d = '' 
			d += alarm_.marshall()
			m.paramstream += d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	

class IGatewayAdapter:
	# -- INTERFACE -- 
	def __init__(self):
		if not hasattr(self,'delegatecls'):
			self.delegatecls = {}
		self.delegatecls[1] = IGatewayAdapter_delegate
	
	def login(self,token_,ctx):
		return CallReturn_t()
	def logout(self,ctx):
		pass
	
	def heartbeat(self,ctx):
		return 0

class IGatewayAdapter_delegate:
	def __init__(self,inst,adapter,conn=None):
		self.index = 1
		self.optlist={}
		self.id = '' 
		self.adapter = adapter
		self.optlist[0] = (self.login)
		self.optlist[1] = (self.logout)
		self.optlist[2] = (self.heartbeat)
		
		self.inst = inst
	
	def login(self,ctx):
		print "callin (login)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_token_ = d[idx:idx+size]
		idx+=size
		cr = None
		cr = self.inst.login(_p_token_,ctx)
		if  cr == None: return True
		d = '' 
		m = tce.RpcMessageReturn()
		m.sequence = ctx.msg.sequence
		m.callmsg = ctx.msg
		m.ifidx = ctx.msg.ifidx
		m.call_id = ctx.msg.call_id
		m.conn = ctx.msg.conn
		m.extra = ctx.msg.extra
		d += cr.marshall()
		if d: m.paramstream += d
		ctx.conn.sendMessage(m)
		return True
	
	def logout(self,ctx):
		print "callin (logout)"
		d = ctx.msg.paramstream 
		idx = 0
		cr = None
		self.inst.logout(ctx)
		return True
	
	def heartbeat(self,ctx):
		print "callin (heartbeat)"
		d = ctx.msg.paramstream 
		idx = 0
		cr = None
		cr = self.inst.heartbeat(ctx)
		if  cr == None: return True
		d = '' 
		m = tce.RpcMessageReturn()
		m.sequence = ctx.msg.sequence
		m.callmsg = ctx.msg
		m.ifidx = ctx.msg.ifidx
		m.call_id = ctx.msg.call_id
		m.conn = ctx.msg.conn
		m.extra = ctx.msg.extra
		d += struct.pack('!i',cr)
		if d: m.paramstream += d
		ctx.conn.sendMessage(m)
		return True
	
	
class IGatewayAdapterPrx:
	# -- INTERFACE PROXY -- 
	def __init__(self,conn):
		self.conn = conn
		self.delta = None
		pass
	
	@staticmethod
	def create(address):
		conn = tce.RpcConnectionSocket()
		conn.open(address)
		proxy = IGatewayAdapterPrx(conn)
		return proxy
	
	@staticmethod
	def createWithEpName(name):
		ep = tce.RpcCommunicator.instance().currentServer().findEndPointByName(name)
		if not ep: return None
		conn = ep.impl
		proxy = IGatewayAdapterPrx(conn)
		return proxy
	
	@staticmethod
	def createWithProxy(prx):
		proxy = IGatewayAdapterPrx(prx.conn)
		return proxy
	
	#extra must be map<string,string>
	def login(self,token_,timeout=None,extra={}):
		# function index: 25
		
		m = tce.RpcMessageCall()
		m.ifidx = 1
		m.opidx = 0
		m.extra.setStrDict(extra)
		d = '' 
		if type(token_)==type(0) or type(token_) == type(0.1): token_=str(token_)
		if not token_: token_=''
		try:
			token_ = token_.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(token_)))
		d += str(token_)
		m.paramstream += d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		if not timeout: timeout = tce.RpcCommunicator.instance().getRpcCallTimeout()
		m2 = None
		try:
			m2 = m.mtx.get(timeout=timeout)
		except:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
		idx = 0
		d = m.paramstream
		p = None
		r = False
		try:
			p = CallReturn_t()
			r,idx = p.unmarshall(d,idx)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_UNSERIALIZE_FAILED)
		return p
	
	def login_async(self,token_,async,extra={}):
		# function index: 25
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 1
		m.opidx = 0
		m.extra.setStrDict(extra)
		d = '' 
		if type(token_)==type(0) or type(token_) == type(0.1): token_=str(token_)
		if not token_: token_=''
		try:
			token_ = token_.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(token_)))
		d += str(token_)
		m.paramstream += d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
		m.async = async
		m.asyncparser = IGatewayAdapterPrx.login_asyncparser
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def login_asyncparser(m,m2):
		# function index: 25 , m2 - callreturn msg.
		
		stream = m2.paramstream
		user = m.async
		prx = m.prx
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC: return 
		try:
			idx = 0
			d = stream
			r = True
			p = CallReturn_t()
			r,idx = p.unmarshall(d,idx)
			if r:
				user(p,prx)
		except:
			traceback.print_exc()
		
	
	#extra must be map<string,string>
	def logout(self,timeout=None,extra={}):
		# function index: 25
		
		m = tce.RpcMessageCall()
		m.ifidx = 1
		m.opidx = 1
		m.extra.setStrDict(extra)
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		if not timeout: timeout = tce.RpcCommunicator.instance().getRpcCallTimeout()
		m2 = None
		try:
			m2 = m.mtx.get(timeout=timeout)
		except:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def logout_oneway(self,extra={}):
		# function index: 25
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 1
			m.opidx = 1
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
			m.extra.setStrDict(extra)
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	#extra must be map<string,string>
	def heartbeat(self,timeout=None,extra={}):
		# function index: 25
		
		m = tce.RpcMessageCall()
		m.ifidx = 1
		m.opidx = 2
		m.extra.setStrDict(extra)
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		if not timeout: timeout = tce.RpcCommunicator.instance().getRpcCallTimeout()
		m2 = None
		try:
			m2 = m.mtx.get(timeout=timeout)
		except:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
		idx = 0
		d = m.paramstream
		p = None
		r = False
		try:
			p = None
			p, = struct.unpack('!i',d[idx:idx+4])
			idx+=4
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_UNSERIALIZE_FAILED)
		return p
	
	def heartbeat_async(self,async,extra={}):
		# function index: 25
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 1
		m.opidx = 2
		m.extra.setStrDict(extra)
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
		m.async = async
		m.asyncparser = IGatewayAdapterPrx.heartbeat_asyncparser
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def heartbeat_asyncparser(m,m2):
		# function index: 25 , m2 - callreturn msg.
		
		stream = m2.paramstream
		user = m.async
		prx = m.prx
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC: return 
		try:
			idx = 0
			d = stream
			r = True
			p = None
			p, = struct.unpack('!i',d[idx:idx+4])
			idx+=4
			if r:
				user(p,prx)
		except:
			traceback.print_exc()
		
	

class IUserService:
	# -- INTERFACE -- 
	def __init__(self):
		if not hasattr(self,'delegatecls'):
			self.delegatecls = {}
		self.delegatecls[2] = IUserService_delegate
	
	def userLogin(self,userid_,gwaid_,ctx):
		pass
	
	def userLogout(self,userid_,gwaid_,ctx):
		pass
	

class IUserService_delegate:
	def __init__(self,inst,adapter,conn=None):
		self.index = 2
		self.optlist={}
		self.id = '' 
		self.adapter = adapter
		self.optlist[0] = (self.userLogin)
		self.optlist[1] = (self.userLogout)
		
		self.inst = inst
	
	def userLogin(self,ctx):
		print "callin (userLogin)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_userid_ = d[idx:idx+size]
		idx+=size
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_gwaid_ = d[idx:idx+size]
		idx+=size
		cr = None
		self.inst.userLogin(_p_userid_,_p_gwaid_,ctx)
		return True
	
	def userLogout(self,ctx):
		print "callin (userLogout)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_userid_ = d[idx:idx+size]
		idx+=size
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_gwaid_ = d[idx:idx+size]
		idx+=size
		cr = None
		self.inst.userLogout(_p_userid_,_p_gwaid_,ctx)
		return True
	
	
class IUserServicePrx:
	# -- INTERFACE PROXY -- 
	def __init__(self,conn):
		self.conn = conn
		self.delta = None
		pass
	
	@staticmethod
	def create(address):
		conn = tce.RpcConnectionSocket()
		conn.open(address)
		proxy = IUserServicePrx(conn)
		return proxy
	
	@staticmethod
	def createWithEpName(name):
		ep = tce.RpcCommunicator.instance().currentServer().findEndPointByName(name)
		if not ep: return None
		conn = ep.impl
		proxy = IUserServicePrx(conn)
		return proxy
	
	@staticmethod
	def createWithProxy(prx):
		proxy = IUserServicePrx(prx.conn)
		return proxy
	
	#extra must be map<string,string>
	def userLogin(self,userid_,gwaid_,timeout=None,extra={}):
		# function index: 26
		
		m = tce.RpcMessageCall()
		m.ifidx = 2
		m.opidx = 0
		m.extra.setStrDict(extra)
		d = '' 
		if type(userid_)==type(0) or type(userid_) == type(0.1): userid_=str(userid_)
		if not userid_: userid_=''
		try:
			userid_ = userid_.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(userid_)))
		d += str(userid_)
		m.paramstream += d
		d = '' 
		if type(gwaid_)==type(0) or type(gwaid_) == type(0.1): gwaid_=str(gwaid_)
		if not gwaid_: gwaid_=''
		try:
			gwaid_ = gwaid_.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(gwaid_)))
		d += str(gwaid_)
		m.paramstream += d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		if not timeout: timeout = tce.RpcCommunicator.instance().getRpcCallTimeout()
		m2 = None
		try:
			m2 = m.mtx.get(timeout=timeout)
		except:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def userLogin_oneway(self,userid_,gwaid_,extra={}):
		# function index: 26
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 2
			m.opidx = 0
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
			m.extra.setStrDict(extra)
			d = '' 
			if type(userid_)==type(0) or type(userid_) == type(0.1): userid_=str(userid_)
			if not userid_: userid_=''
			try:
				userid_ = userid_.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(userid_)))
			d += str(userid_)
			m.paramstream += d
			d = '' 
			if type(gwaid_)==type(0) or type(gwaid_) == type(0.1): gwaid_=str(gwaid_)
			if not gwaid_: gwaid_=''
			try:
				gwaid_ = gwaid_.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(gwaid_)))
			d += str(gwaid_)
			m.paramstream += d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	#extra must be map<string,string>
	def userLogout(self,userid_,gwaid_,timeout=None,extra={}):
		# function index: 26
		
		m = tce.RpcMessageCall()
		m.ifidx = 2
		m.opidx = 1
		m.extra.setStrDict(extra)
		d = '' 
		if type(userid_)==type(0) or type(userid_) == type(0.1): userid_=str(userid_)
		if not userid_: userid_=''
		try:
			userid_ = userid_.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(userid_)))
		d += str(userid_)
		m.paramstream += d
		d = '' 
		if type(gwaid_)==type(0) or type(gwaid_) == type(0.1): gwaid_=str(gwaid_)
		if not gwaid_: gwaid_=''
		try:
			gwaid_ = gwaid_.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(gwaid_)))
		d += str(gwaid_)
		m.paramstream += d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		if not timeout: timeout = tce.RpcCommunicator.instance().getRpcCallTimeout()
		m2 = None
		try:
			m2 = m.mtx.get(timeout=timeout)
		except:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def userLogout_oneway(self,userid_,gwaid_,extra={}):
		# function index: 26
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 2
			m.opidx = 1
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
			m.extra.setStrDict(extra)
			d = '' 
			if type(userid_)==type(0) or type(userid_) == type(0.1): userid_=str(userid_)
			if not userid_: userid_=''
			try:
				userid_ = userid_.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(userid_)))
			d += str(userid_)
			m.paramstream += d
			d = '' 
			if type(gwaid_)==type(0) or type(gwaid_) == type(0.1): gwaid_=str(gwaid_)
			if not gwaid_: gwaid_=''
			try:
				gwaid_ = gwaid_.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(gwaid_)))
			d += str(gwaid_)
			m.paramstream += d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	

class IAuthService:
	# -- INTERFACE -- 
	def __init__(self):
		if not hasattr(self,'delegatecls'):
			self.delegatecls = {}
		self.delegatecls[3] = IAuthService_delegate
	
	def userAuth(self,user_,passwd_,loginType_,ctx):
		return ''

class IAuthService_delegate:
	def __init__(self,inst,adapter,conn=None):
		self.index = 3
		self.optlist={}
		self.id = '' 
		self.adapter = adapter
		self.optlist[0] = (self.userAuth)
		
		self.inst = inst
	
	def userAuth(self,ctx):
		print "callin (userAuth)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_user_ = d[idx:idx+size]
		idx+=size
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_passwd_ = d[idx:idx+size]
		idx+=size
		_p_loginType_, = struct.unpack('!i',d[idx:idx+4])
		idx+=4
		cr = None
		cr = self.inst.userAuth(_p_user_,_p_passwd_,_p_loginType_,ctx)
		if  cr == None: return True
		d = '' 
		m = tce.RpcMessageReturn()
		m.sequence = ctx.msg.sequence
		m.callmsg = ctx.msg
		m.ifidx = ctx.msg.ifidx
		m.call_id = ctx.msg.call_id
		m.conn = ctx.msg.conn
		m.extra = ctx.msg.extra
		if type(cr)==type(0) or type(cr) == type(0.1): cr=str(cr)
		if not cr: cr=''
		try:
			cr = cr.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(cr)))
		d += str(cr)
		if d: m.paramstream += d
		ctx.conn.sendMessage(m)
		return True
	
	
class IAuthServicePrx:
	# -- INTERFACE PROXY -- 
	def __init__(self,conn):
		self.conn = conn
		self.delta = None
		pass
	
	@staticmethod
	def create(address):
		conn = tce.RpcConnectionSocket()
		conn.open(address)
		proxy = IAuthServicePrx(conn)
		return proxy
	
	@staticmethod
	def createWithEpName(name):
		ep = tce.RpcCommunicator.instance().currentServer().findEndPointByName(name)
		if not ep: return None
		conn = ep.impl
		proxy = IAuthServicePrx(conn)
		return proxy
	
	@staticmethod
	def createWithProxy(prx):
		proxy = IAuthServicePrx(prx.conn)
		return proxy
	
	#extra must be map<string,string>
	def userAuth(self,user_,passwd_,loginType_,timeout=None,extra={}):
		# function index: 27
		
		m = tce.RpcMessageCall()
		m.ifidx = 3
		m.opidx = 0
		m.extra.setStrDict(extra)
		d = '' 
		if type(user_)==type(0) or type(user_) == type(0.1): user_=str(user_)
		if not user_: user_=''
		try:
			user_ = user_.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(user_)))
		d += str(user_)
		m.paramstream += d
		d = '' 
		if type(passwd_)==type(0) or type(passwd_) == type(0.1): passwd_=str(passwd_)
		if not passwd_: passwd_=''
		try:
			passwd_ = passwd_.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(passwd_)))
		d += str(passwd_)
		m.paramstream += d
		d = '' 
		d += struct.pack('!i',loginType_)
		m.paramstream += d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		if not timeout: timeout = tce.RpcCommunicator.instance().getRpcCallTimeout()
		m2 = None
		try:
			m2 = m.mtx.get(timeout=timeout)
		except:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
		idx = 0
		d = m.paramstream
		p = None
		r = False
		try:
			p = None
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			p = d[idx:idx+size]
			idx+=size
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_UNSERIALIZE_FAILED)
		return p
	
	def userAuth_async(self,user_,passwd_,loginType_,async,extra={}):
		# function index: 27
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 3
		m.opidx = 0
		m.extra.setStrDict(extra)
		d = '' 
		if type(user_)==type(0) or type(user_) == type(0.1): user_=str(user_)
		if not user_: user_=''
		try:
			user_ = user_.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(user_)))
		d += str(user_)
		m.paramstream += d
		d = '' 
		if type(passwd_)==type(0) or type(passwd_) == type(0.1): passwd_=str(passwd_)
		if not passwd_: passwd_=''
		try:
			passwd_ = passwd_.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(passwd_)))
		d += str(passwd_)
		m.paramstream += d
		d = '' 
		d += struct.pack('!i',loginType_)
		m.paramstream += d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
		m.async = async
		m.asyncparser = IAuthServicePrx.userAuth_asyncparser
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def userAuth_asyncparser(m,m2):
		# function index: 27 , m2 - callreturn msg.
		
		stream = m2.paramstream
		user = m.async
		prx = m.prx
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC: return 
		try:
			idx = 0
			d = stream
			r = True
			p = None
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			p = d[idx:idx+size]
			idx+=size
			if r:
				user(p,prx)
		except:
			traceback.print_exc()
		
	

class ICtrlService:
	# -- INTERFACE -- 
	def __init__(self):
		if not hasattr(self,'delegatecls'):
			self.delegatecls = {}
		self.delegatecls[4] = ICtrlService_delegate
	
	def getProps(self,ctx):
		return {}

class ICtrlService_delegate:
	def __init__(self,inst,adapter,conn=None):
		self.index = 4
		self.optlist={}
		self.id = '' 
		self.adapter = adapter
		self.optlist[0] = (self.getProps)
		
		self.inst = inst
	
	def getProps(self,ctx):
		print "callin (getProps)"
		d = ctx.msg.paramstream 
		idx = 0
		cr = None
		cr = self.inst.getProps(ctx)
		if  cr == None: return True
		d = '' 
		m = tce.RpcMessageReturn()
		m.sequence = ctx.msg.sequence
		m.callmsg = ctx.msg
		m.ifidx = ctx.msg.ifidx
		m.call_id = ctx.msg.call_id
		m.conn = ctx.msg.conn
		m.extra = ctx.msg.extra
		container = Properties_t(cr)
		d += container.marshall()
		if d: m.paramstream += d
		ctx.conn.sendMessage(m)
		return True
	
	
class ICtrlServicePrx:
	# -- INTERFACE PROXY -- 
	def __init__(self,conn):
		self.conn = conn
		self.delta = None
		pass
	
	@staticmethod
	def create(address):
		conn = tce.RpcConnectionSocket()
		conn.open(address)
		proxy = ICtrlServicePrx(conn)
		return proxy
	
	@staticmethod
	def createWithEpName(name):
		ep = tce.RpcCommunicator.instance().currentServer().findEndPointByName(name)
		if not ep: return None
		conn = ep.impl
		proxy = ICtrlServicePrx(conn)
		return proxy
	
	@staticmethod
	def createWithProxy(prx):
		proxy = ICtrlServicePrx(prx.conn)
		return proxy
	
	#extra must be map<string,string>
	def getProps(self,timeout=None,extra={}):
		# function index: 28
		
		m = tce.RpcMessageCall()
		m.ifidx = 4
		m.opidx = 0
		m.extra.setStrDict(extra)
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		if not timeout: timeout = tce.RpcCommunicator.instance().getRpcCallTimeout()
		m2 = None
		try:
			m2 = m.mtx.get(timeout=timeout)
		except:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
		idx = 0
		d = m.paramstream
		p = None
		r = False
		try:
			p ={}
			container = Properties_t(p)
			r,idx = container.unmarshall(d,idx)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_UNSERIALIZE_FAILED)
		return p
	
	def getProps_async(self,async,extra={}):
		# function index: 28
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 4
		m.opidx = 0
		m.extra.setStrDict(extra)
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
		m.async = async
		m.asyncparser = ICtrlServicePrx.getProps_asyncparser
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def getProps_asyncparser(m,m2):
		# function index: 28 , m2 - callreturn msg.
		
		stream = m2.paramstream
		user = m.async
		prx = m.prx
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC: return 
		try:
			idx = 0
			d = stream
			r = True
			p ={}
			container = Properties_t(p)
			r,idx = container.unmarshall(d,idx)
			if r:
				user(p,prx)
		except:
			traceback.print_exc()
		
	

class INotificationService:
	# -- INTERFACE -- 
	def __init__(self):
		if not hasattr(self,'delegatecls'):
			self.delegatecls = {}
		self.delegatecls[5] = INotificationService_delegate
	
	def sendSMS(self,target_,content_,ctx):
		pass
	
	def sendMail(self,target_,content_,ctx):
		pass
	

class INotificationService_delegate:
	def __init__(self,inst,adapter,conn=None):
		self.index = 5
		self.optlist={}
		self.id = '' 
		self.adapter = adapter
		self.optlist[0] = (self.sendSMS)
		self.optlist[1] = (self.sendMail)
		
		self.inst = inst
	
	def sendSMS(self,ctx):
		print "callin (sendSMS)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_target_ = d[idx:idx+size]
		idx+=size
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_content_ = d[idx:idx+size]
		idx+=size
		cr = None
		self.inst.sendSMS(_p_target_,_p_content_,ctx)
		return True
	
	def sendMail(self,ctx):
		print "callin (sendMail)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_target_ = d[idx:idx+size]
		idx+=size
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_content_ = d[idx:idx+size]
		idx+=size
		cr = None
		self.inst.sendMail(_p_target_,_p_content_,ctx)
		return True
	
	
class INotificationServicePrx:
	# -- INTERFACE PROXY -- 
	def __init__(self,conn):
		self.conn = conn
		self.delta = None
		pass
	
	@staticmethod
	def create(address):
		conn = tce.RpcConnectionSocket()
		conn.open(address)
		proxy = INotificationServicePrx(conn)
		return proxy
	
	@staticmethod
	def createWithEpName(name):
		ep = tce.RpcCommunicator.instance().currentServer().findEndPointByName(name)
		if not ep: return None
		conn = ep.impl
		proxy = INotificationServicePrx(conn)
		return proxy
	
	@staticmethod
	def createWithProxy(prx):
		proxy = INotificationServicePrx(prx.conn)
		return proxy
	
	#extra must be map<string,string>
	def sendSMS(self,target_,content_,timeout=None,extra={}):
		# function index: 29
		
		m = tce.RpcMessageCall()
		m.ifidx = 5
		m.opidx = 0
		m.extra.setStrDict(extra)
		d = '' 
		if type(target_)==type(0) or type(target_) == type(0.1): target_=str(target_)
		if not target_: target_=''
		try:
			target_ = target_.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(target_)))
		d += str(target_)
		m.paramstream += d
		d = '' 
		if type(content_)==type(0) or type(content_) == type(0.1): content_=str(content_)
		if not content_: content_=''
		try:
			content_ = content_.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(content_)))
		d += str(content_)
		m.paramstream += d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		if not timeout: timeout = tce.RpcCommunicator.instance().getRpcCallTimeout()
		m2 = None
		try:
			m2 = m.mtx.get(timeout=timeout)
		except:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def sendSMS_oneway(self,target_,content_,extra={}):
		# function index: 29
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 5
			m.opidx = 0
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
			m.extra.setStrDict(extra)
			d = '' 
			if type(target_)==type(0) or type(target_) == type(0.1): target_=str(target_)
			if not target_: target_=''
			try:
				target_ = target_.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(target_)))
			d += str(target_)
			m.paramstream += d
			d = '' 
			if type(content_)==type(0) or type(content_) == type(0.1): content_=str(content_)
			if not content_: content_=''
			try:
				content_ = content_.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(content_)))
			d += str(content_)
			m.paramstream += d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	#extra must be map<string,string>
	def sendMail(self,target_,content_,timeout=None,extra={}):
		# function index: 29
		
		m = tce.RpcMessageCall()
		m.ifidx = 5
		m.opidx = 1
		m.extra.setStrDict(extra)
		d = '' 
		if type(target_)==type(0) or type(target_) == type(0.1): target_=str(target_)
		if not target_: target_=''
		try:
			target_ = target_.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(target_)))
		d += str(target_)
		m.paramstream += d
		d = '' 
		if type(content_)==type(0) or type(content_) == type(0.1): content_=str(content_)
		if not content_: content_=''
		try:
			content_ = content_.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(content_)))
		d += str(content_)
		m.paramstream += d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		if not timeout: timeout = tce.RpcCommunicator.instance().getRpcCallTimeout()
		m2 = None
		try:
			m2 = m.mtx.get(timeout=timeout)
		except:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def sendMail_oneway(self,target_,content_,extra={}):
		# function index: 29
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 5
			m.opidx = 1
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
			m.extra.setStrDict(extra)
			d = '' 
			if type(target_)==type(0) or type(target_) == type(0.1): target_=str(target_)
			if not target_: target_=''
			try:
				target_ = target_.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(target_)))
			d += str(target_)
			m.paramstream += d
			d = '' 
			if type(content_)==type(0) or type(content_) == type(0.1): content_=str(content_)
			if not content_: content_=''
			try:
				content_ = content_.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(content_)))
			d += str(content_)
			m.paramstream += d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	

class IAlarmService:
	# -- INTERFACE -- 
	def __init__(self):
		if not hasattr(self,'delegatecls'):
			self.delegatecls = {}
		self.delegatecls[6] = IAlarmService_delegate
	
	def addItem(self,aoid_,asid_,ctx):
		pass
	
	def removeItem(self,aoid_,asid_,ctx):
		pass
	

class IAlarmService_delegate:
	def __init__(self,inst,adapter,conn=None):
		self.index = 6
		self.optlist={}
		self.id = '' 
		self.adapter = adapter
		self.optlist[0] = (self.addItem)
		self.optlist[1] = (self.removeItem)
		
		self.inst = inst
	
	def addItem(self,ctx):
		print "callin (addItem)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_aoid_ = d[idx:idx+size]
		idx+=size
		_p_asid_, = struct.unpack('!i',d[idx:idx+4])
		idx+=4
		cr = None
		self.inst.addItem(_p_aoid_,_p_asid_,ctx)
		return True
	
	def removeItem(self,ctx):
		print "callin (removeItem)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_aoid_ = d[idx:idx+size]
		idx+=size
		_p_asid_, = struct.unpack('!i',d[idx:idx+4])
		idx+=4
		cr = None
		self.inst.removeItem(_p_aoid_,_p_asid_,ctx)
		return True
	
	
class IAlarmServicePrx:
	# -- INTERFACE PROXY -- 
	def __init__(self,conn):
		self.conn = conn
		self.delta = None
		pass
	
	@staticmethod
	def create(address):
		conn = tce.RpcConnectionSocket()
		conn.open(address)
		proxy = IAlarmServicePrx(conn)
		return proxy
	
	@staticmethod
	def createWithEpName(name):
		ep = tce.RpcCommunicator.instance().currentServer().findEndPointByName(name)
		if not ep: return None
		conn = ep.impl
		proxy = IAlarmServicePrx(conn)
		return proxy
	
	@staticmethod
	def createWithProxy(prx):
		proxy = IAlarmServicePrx(prx.conn)
		return proxy
	
	#extra must be map<string,string>
	def addItem(self,aoid_,asid_,timeout=None,extra={}):
		# function index: 30
		
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 0
		m.extra.setStrDict(extra)
		d = '' 
		if type(aoid_)==type(0) or type(aoid_) == type(0.1): aoid_=str(aoid_)
		if not aoid_: aoid_=''
		try:
			aoid_ = aoid_.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(aoid_)))
		d += str(aoid_)
		m.paramstream += d
		d = '' 
		d += struct.pack('!i',asid_)
		m.paramstream += d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		if not timeout: timeout = tce.RpcCommunicator.instance().getRpcCallTimeout()
		m2 = None
		try:
			m2 = m.mtx.get(timeout=timeout)
		except:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def addItem_oneway(self,aoid_,asid_,extra={}):
		# function index: 30
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 6
			m.opidx = 0
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
			m.extra.setStrDict(extra)
			d = '' 
			if type(aoid_)==type(0) or type(aoid_) == type(0.1): aoid_=str(aoid_)
			if not aoid_: aoid_=''
			try:
				aoid_ = aoid_.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(aoid_)))
			d += str(aoid_)
			m.paramstream += d
			d = '' 
			d += struct.pack('!i',asid_)
			m.paramstream += d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	#extra must be map<string,string>
	def removeItem(self,aoid_,asid_,timeout=None,extra={}):
		# function index: 30
		
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 1
		m.extra.setStrDict(extra)
		d = '' 
		if type(aoid_)==type(0) or type(aoid_) == type(0.1): aoid_=str(aoid_)
		if not aoid_: aoid_=''
		try:
			aoid_ = aoid_.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(aoid_)))
		d += str(aoid_)
		m.paramstream += d
		d = '' 
		d += struct.pack('!i',asid_)
		m.paramstream += d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		if not timeout: timeout = tce.RpcCommunicator.instance().getRpcCallTimeout()
		m2 = None
		try:
			m2 = m.mtx.get(timeout=timeout)
		except:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def removeItem_oneway(self,aoid_,asid_,extra={}):
		# function index: 30
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 6
			m.opidx = 1
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
			m.extra.setStrDict(extra)
			d = '' 
			if type(aoid_)==type(0) or type(aoid_) == type(0.1): aoid_=str(aoid_)
			if not aoid_: aoid_=''
			try:
				aoid_ = aoid_.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(aoid_)))
			d += str(aoid_)
			m.paramstream += d
			d = '' 
			d += struct.pack('!i',asid_)
			m.paramstream += d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	

class ITaskService:
	# -- INTERFACE -- 
	def __init__(self):
		if not hasattr(self,'delegatecls'):
			self.delegatecls = {}
		self.delegatecls[7] = ITaskService_delegate
	
	def getProps(self,ctx):
		return {}

class ITaskService_delegate:
	def __init__(self,inst,adapter,conn=None):
		self.index = 7
		self.optlist={}
		self.id = '' 
		self.adapter = adapter
		self.optlist[0] = (self.getProps)
		
		self.inst = inst
	
	def getProps(self,ctx):
		print "callin (getProps)"
		d = ctx.msg.paramstream 
		idx = 0
		cr = None
		cr = self.inst.getProps(ctx)
		if  cr == None: return True
		d = '' 
		m = tce.RpcMessageReturn()
		m.sequence = ctx.msg.sequence
		m.callmsg = ctx.msg
		m.ifidx = ctx.msg.ifidx
		m.call_id = ctx.msg.call_id
		m.conn = ctx.msg.conn
		m.extra = ctx.msg.extra
		container = Properties_t(cr)
		d += container.marshall()
		if d: m.paramstream += d
		ctx.conn.sendMessage(m)
		return True
	
	
class ITaskServicePrx:
	# -- INTERFACE PROXY -- 
	def __init__(self,conn):
		self.conn = conn
		self.delta = None
		pass
	
	@staticmethod
	def create(address):
		conn = tce.RpcConnectionSocket()
		conn.open(address)
		proxy = ITaskServicePrx(conn)
		return proxy
	
	@staticmethod
	def createWithEpName(name):
		ep = tce.RpcCommunicator.instance().currentServer().findEndPointByName(name)
		if not ep: return None
		conn = ep.impl
		proxy = ITaskServicePrx(conn)
		return proxy
	
	@staticmethod
	def createWithProxy(prx):
		proxy = ITaskServicePrx(prx.conn)
		return proxy
	
	#extra must be map<string,string>
	def getProps(self,timeout=None,extra={}):
		# function index: 31
		
		m = tce.RpcMessageCall()
		m.ifidx = 7
		m.opidx = 0
		m.extra.setStrDict(extra)
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		if not timeout: timeout = tce.RpcCommunicator.instance().getRpcCallTimeout()
		m2 = None
		try:
			m2 = m.mtx.get(timeout=timeout)
		except:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
		idx = 0
		d = m.paramstream
		p = None
		r = False
		try:
			p ={}
			container = Properties_t(p)
			r,idx = container.unmarshall(d,idx)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_UNSERIALIZE_FAILED)
		return p
	
	def getProps_async(self,async,extra={}):
		# function index: 31
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 7
		m.opidx = 0
		m.extra.setStrDict(extra)
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
		m.async = async
		m.asyncparser = ITaskServicePrx.getProps_asyncparser
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def getProps_asyncparser(m,m2):
		# function index: 31 , m2 - callreturn msg.
		
		stream = m2.paramstream
		user = m.async
		prx = m.prx
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC: return 
		try:
			idx = 0
			d = stream
			r = True
			p ={}
			container = Properties_t(p)
			r,idx = container.unmarshall(d,idx)
			if r:
				user(p,prx)
		except:
			traceback.print_exc()
		
	

class IAoModuleClient:
	# -- INTERFACE -- 
	def __init__(self):
		if not hasattr(self,'delegatecls'):
			self.delegatecls = {}
		self.delegatecls[8] = IAoModuleClient_delegate
	
	def onGetGpsData(self,aoid_,gps_,ctx):
		pass
	
	def onGetAlarm(self,aoid_,alarm_,ctx):
		pass
	
	def onModuleData(self,json_,ctx):
		pass
	

class IAoModuleClient_delegate:
	def __init__(self,inst,adapter,conn=None):
		self.index = 8
		self.optlist={}
		self.id = '' 
		self.adapter = adapter
		self.optlist[0] = (self.onGetGpsData)
		self.optlist[1] = (self.onGetAlarm)
		self.optlist[2] = (self.onModuleData)
		
		self.inst = inst
	
	def onGetGpsData(self,ctx):
		print "callin (onGetGpsData)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_aoid_ = d[idx:idx+size]
		idx+=size
		_p_gps_ = GpsData_t()
		r,idx = _p_gps_.unmarshall(d,idx)
		if not r: return False
		cr = None
		self.inst.onGetGpsData(_p_aoid_,_p_gps_,ctx)
		return True
	
	def onGetAlarm(self,ctx):
		print "callin (onGetAlarm)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_aoid_ = d[idx:idx+size]
		idx+=size
		_p_alarm_ = AlarmInfo_t()
		r,idx = _p_alarm_.unmarshall(d,idx)
		if not r: return False
		cr = None
		self.inst.onGetAlarm(_p_aoid_,_p_alarm_,ctx)
		return True
	
	def onModuleData(self,ctx):
		print "callin (onModuleData)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_json_ = d[idx:idx+size]
		idx+=size
		cr = None
		self.inst.onModuleData(_p_json_,ctx)
		return True
	
	
class IAoModuleClientPrx:
	# -- INTERFACE PROXY -- 
	def __init__(self,conn):
		self.conn = conn
		self.delta = None
		pass
	
	@staticmethod
	def create(address):
		conn = tce.RpcConnectionSocket()
		conn.open(address)
		proxy = IAoModuleClientPrx(conn)
		return proxy
	
	@staticmethod
	def createWithEpName(name):
		ep = tce.RpcCommunicator.instance().currentServer().findEndPointByName(name)
		if not ep: return None
		conn = ep.impl
		proxy = IAoModuleClientPrx(conn)
		return proxy
	
	@staticmethod
	def createWithProxy(prx):
		proxy = IAoModuleClientPrx(prx.conn)
		return proxy
	
	#extra must be map<string,string>
	def onGetGpsData(self,aoid_,gps_,timeout=None,extra={}):
		# function index: 32
		
		m = tce.RpcMessageCall()
		m.ifidx = 8
		m.opidx = 0
		m.extra.setStrDict(extra)
		d = '' 
		if type(aoid_)==type(0) or type(aoid_) == type(0.1): aoid_=str(aoid_)
		if not aoid_: aoid_=''
		try:
			aoid_ = aoid_.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(aoid_)))
		d += str(aoid_)
		m.paramstream += d
		d = '' 
		d += gps_.marshall()
		m.paramstream += d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		if not timeout: timeout = tce.RpcCommunicator.instance().getRpcCallTimeout()
		m2 = None
		try:
			m2 = m.mtx.get(timeout=timeout)
		except:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def onGetGpsData_oneway(self,aoid_,gps_,extra={}):
		# function index: 32
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 8
			m.opidx = 0
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
			m.extra.setStrDict(extra)
			d = '' 
			if type(aoid_)==type(0) or type(aoid_) == type(0.1): aoid_=str(aoid_)
			if not aoid_: aoid_=''
			try:
				aoid_ = aoid_.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(aoid_)))
			d += str(aoid_)
			m.paramstream += d
			d = '' 
			d += gps_.marshall()
			m.paramstream += d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	#extra must be map<string,string>
	def onGetAlarm(self,aoid_,alarm_,timeout=None,extra={}):
		# function index: 32
		
		m = tce.RpcMessageCall()
		m.ifidx = 8
		m.opidx = 1
		m.extra.setStrDict(extra)
		d = '' 
		if type(aoid_)==type(0) or type(aoid_) == type(0.1): aoid_=str(aoid_)
		if not aoid_: aoid_=''
		try:
			aoid_ = aoid_.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(aoid_)))
		d += str(aoid_)
		m.paramstream += d
		d = '' 
		d += alarm_.marshall()
		m.paramstream += d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		if not timeout: timeout = tce.RpcCommunicator.instance().getRpcCallTimeout()
		m2 = None
		try:
			m2 = m.mtx.get(timeout=timeout)
		except:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def onGetAlarm_oneway(self,aoid_,alarm_,extra={}):
		# function index: 32
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 8
			m.opidx = 1
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
			m.extra.setStrDict(extra)
			d = '' 
			if type(aoid_)==type(0) or type(aoid_) == type(0.1): aoid_=str(aoid_)
			if not aoid_: aoid_=''
			try:
				aoid_ = aoid_.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(aoid_)))
			d += str(aoid_)
			m.paramstream += d
			d = '' 
			d += alarm_.marshall()
			m.paramstream += d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	#extra must be map<string,string>
	def onModuleData(self,json_,timeout=None,extra={}):
		# function index: 32
		
		m = tce.RpcMessageCall()
		m.ifidx = 8
		m.opidx = 2
		m.extra.setStrDict(extra)
		d = '' 
		if type(json_)==type(0) or type(json_) == type(0.1): json_=str(json_)
		if not json_: json_=''
		try:
			json_ = json_.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(json_)))
		d += str(json_)
		m.paramstream += d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		if not timeout: timeout = tce.RpcCommunicator.instance().getRpcCallTimeout()
		m2 = None
		try:
			m2 = m.mtx.get(timeout=timeout)
		except:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def onModuleData_oneway(self,json_,extra={}):
		# function index: 32
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 8
			m.opidx = 2
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
			m.extra.setStrDict(extra)
			d = '' 
			if type(json_)==type(0) or type(json_) == type(0.1): json_=str(json_)
			if not json_: json_=''
			try:
				json_ = json_.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(json_)))
			d += str(json_)
			m.paramstream += d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	

class IAoModuleCtrl:
	# -- INTERFACE -- 
	def __init__(self):
		if not hasattr(self,'delegatecls'):
			self.delegatecls = {}
		self.delegatecls[9] = IAoModuleCtrl_delegate
	
	def openListen(self,aoid_,phone_,ctx):
		pass
	
	def closeListen(self,aoid_,ctx):
		pass
	
	def getVersion(self,aoid_,ctx):
		return ''
	def onceNamed(self,aoid_,ctx):
		pass
	
	def speedLimit(self,aoid_,high_,low_,ctx):
		pass
	
	def oilCtrl(self,aoid_,onoff_,ctx):
		pass
	
	def reset(self,aoid_,ctx):
		pass
	
	def setFreqAccOn(self,aoid_,freq_,ctx):
		pass
	
	def setFreqAccOff(self,aoid_,freq_,ctx):
		pass
	
	def setBarrierLeave(self,aoid_,x1_,y1_,x2_,y2_,ctx):
		pass
	
	def setBarrierEnter(self,aoid_,x1_,y1_,x2_,y2_,ctx):
		pass
	
	def clearAlarms(self,aoid_,ctx):
		pass
	
	def clearMiles(self,aoid_,miles_,ctx):
		pass
	

class IAoModuleCtrl_delegate:
	def __init__(self,inst,adapter,conn=None):
		self.index = 9
		self.optlist={}
		self.id = '' 
		self.adapter = adapter
		self.optlist[0] = (self.openListen)
		self.optlist[1] = (self.closeListen)
		self.optlist[2] = (self.getVersion)
		self.optlist[3] = (self.onceNamed)
		self.optlist[4] = (self.speedLimit)
		self.optlist[5] = (self.oilCtrl)
		self.optlist[6] = (self.reset)
		self.optlist[7] = (self.setFreqAccOn)
		self.optlist[8] = (self.setFreqAccOff)
		self.optlist[9] = (self.setBarrierLeave)
		self.optlist[10] = (self.setBarrierEnter)
		self.optlist[11] = (self.clearAlarms)
		self.optlist[12] = (self.clearMiles)
		
		self.inst = inst
	
	def openListen(self,ctx):
		print "callin (openListen)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_aoid_ = d[idx:idx+size]
		idx+=size
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_phone_ = d[idx:idx+size]
		idx+=size
		cr = None
		self.inst.openListen(_p_aoid_,_p_phone_,ctx)
		return True
	
	def closeListen(self,ctx):
		print "callin (closeListen)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_aoid_ = d[idx:idx+size]
		idx+=size
		cr = None
		self.inst.closeListen(_p_aoid_,ctx)
		return True
	
	def getVersion(self,ctx):
		print "callin (getVersion)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_aoid_ = d[idx:idx+size]
		idx+=size
		cr = None
		cr = self.inst.getVersion(_p_aoid_,ctx)
		if  cr == None: return True
		d = '' 
		m = tce.RpcMessageReturn()
		m.sequence = ctx.msg.sequence
		m.callmsg = ctx.msg
		m.ifidx = ctx.msg.ifidx
		m.call_id = ctx.msg.call_id
		m.conn = ctx.msg.conn
		m.extra = ctx.msg.extra
		if type(cr)==type(0) or type(cr) == type(0.1): cr=str(cr)
		if not cr: cr=''
		try:
			cr = cr.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(cr)))
		d += str(cr)
		if d: m.paramstream += d
		ctx.conn.sendMessage(m)
		return True
	
	def onceNamed(self,ctx):
		print "callin (onceNamed)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_aoid_ = d[idx:idx+size]
		idx+=size
		cr = None
		self.inst.onceNamed(_p_aoid_,ctx)
		return True
	
	def speedLimit(self,ctx):
		print "callin (speedLimit)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_aoid_ = d[idx:idx+size]
		idx+=size
		_p_high_, = struct.unpack('!i',d[idx:idx+4])
		idx+=4
		_p_low_, = struct.unpack('!i',d[idx:idx+4])
		idx+=4
		cr = None
		self.inst.speedLimit(_p_aoid_,_p_high_,_p_low_,ctx)
		return True
	
	def oilCtrl(self,ctx):
		print "callin (oilCtrl)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_aoid_ = d[idx:idx+size]
		idx+=size
		_p_onoff_, = struct.unpack('B',d[idx:idx+1])
		if _p_onoff_ == 0: _p_onoff_ = False
		else: _p_onoff_ = True
		idx+=1
		cr = None
		self.inst.oilCtrl(_p_aoid_,_p_onoff_,ctx)
		return True
	
	def reset(self,ctx):
		print "callin (reset)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_aoid_ = d[idx:idx+size]
		idx+=size
		cr = None
		self.inst.reset(_p_aoid_,ctx)
		return True
	
	def setFreqAccOn(self,ctx):
		print "callin (setFreqAccOn)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_aoid_ = d[idx:idx+size]
		idx+=size
		_p_freq_, = struct.unpack('!i',d[idx:idx+4])
		idx+=4
		cr = None
		self.inst.setFreqAccOn(_p_aoid_,_p_freq_,ctx)
		return True
	
	def setFreqAccOff(self,ctx):
		print "callin (setFreqAccOff)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_aoid_ = d[idx:idx+size]
		idx+=size
		_p_freq_, = struct.unpack('!i',d[idx:idx+4])
		idx+=4
		cr = None
		self.inst.setFreqAccOff(_p_aoid_,_p_freq_,ctx)
		return True
	
	def setBarrierLeave(self,ctx):
		print "callin (setBarrierLeave)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_aoid_ = d[idx:idx+size]
		idx+=size
		_p_x1_, = struct.unpack('!f',d[idx:idx+4])
		idx+=4
		_p_y1_, = struct.unpack('!f',d[idx:idx+4])
		idx+=4
		_p_x2_, = struct.unpack('!f',d[idx:idx+4])
		idx+=4
		_p_y2_, = struct.unpack('!f',d[idx:idx+4])
		idx+=4
		cr = None
		self.inst.setBarrierLeave(_p_aoid_,_p_x1_,_p_y1_,_p_x2_,_p_y2_,ctx)
		return True
	
	def setBarrierEnter(self,ctx):
		print "callin (setBarrierEnter)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_aoid_ = d[idx:idx+size]
		idx+=size
		_p_x1_, = struct.unpack('!f',d[idx:idx+4])
		idx+=4
		_p_y1_, = struct.unpack('!f',d[idx:idx+4])
		idx+=4
		_p_x2_, = struct.unpack('!f',d[idx:idx+4])
		idx+=4
		_p_y2_, = struct.unpack('!f',d[idx:idx+4])
		idx+=4
		cr = None
		self.inst.setBarrierEnter(_p_aoid_,_p_x1_,_p_y1_,_p_x2_,_p_y2_,ctx)
		return True
	
	def clearAlarms(self,ctx):
		print "callin (clearAlarms)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_aoid_ = d[idx:idx+size]
		idx+=size
		cr = None
		self.inst.clearAlarms(_p_aoid_,ctx)
		return True
	
	def clearMiles(self,ctx):
		print "callin (clearMiles)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_aoid_ = d[idx:idx+size]
		idx+=size
		_p_miles_, = struct.unpack('!i',d[idx:idx+4])
		idx+=4
		cr = None
		self.inst.clearMiles(_p_aoid_,_p_miles_,ctx)
		return True
	
	
class IAoModuleCtrlPrx:
	# -- INTERFACE PROXY -- 
	def __init__(self,conn):
		self.conn = conn
		self.delta = None
		pass
	
	@staticmethod
	def create(address):
		conn = tce.RpcConnectionSocket()
		conn.open(address)
		proxy = IAoModuleCtrlPrx(conn)
		return proxy
	
	@staticmethod
	def createWithEpName(name):
		ep = tce.RpcCommunicator.instance().currentServer().findEndPointByName(name)
		if not ep: return None
		conn = ep.impl
		proxy = IAoModuleCtrlPrx(conn)
		return proxy
	
	@staticmethod
	def createWithProxy(prx):
		proxy = IAoModuleCtrlPrx(prx.conn)
		return proxy
	
	#extra must be map<string,string>
	def openListen(self,aoid_,phone_,timeout=None,extra={}):
		# function index: 33
		
		m = tce.RpcMessageCall()
		m.ifidx = 9
		m.opidx = 0
		m.extra.setStrDict(extra)
		d = '' 
		if type(aoid_)==type(0) or type(aoid_) == type(0.1): aoid_=str(aoid_)
		if not aoid_: aoid_=''
		try:
			aoid_ = aoid_.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(aoid_)))
		d += str(aoid_)
		m.paramstream += d
		d = '' 
		if type(phone_)==type(0) or type(phone_) == type(0.1): phone_=str(phone_)
		if not phone_: phone_=''
		try:
			phone_ = phone_.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(phone_)))
		d += str(phone_)
		m.paramstream += d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		if not timeout: timeout = tce.RpcCommunicator.instance().getRpcCallTimeout()
		m2 = None
		try:
			m2 = m.mtx.get(timeout=timeout)
		except:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def openListen_oneway(self,aoid_,phone_,extra={}):
		# function index: 33
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 9
			m.opidx = 0
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
			m.extra.setStrDict(extra)
			d = '' 
			if type(aoid_)==type(0) or type(aoid_) == type(0.1): aoid_=str(aoid_)
			if not aoid_: aoid_=''
			try:
				aoid_ = aoid_.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(aoid_)))
			d += str(aoid_)
			m.paramstream += d
			d = '' 
			if type(phone_)==type(0) or type(phone_) == type(0.1): phone_=str(phone_)
			if not phone_: phone_=''
			try:
				phone_ = phone_.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(phone_)))
			d += str(phone_)
			m.paramstream += d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	#extra must be map<string,string>
	def closeListen(self,aoid_,timeout=None,extra={}):
		# function index: 33
		
		m = tce.RpcMessageCall()
		m.ifidx = 9
		m.opidx = 1
		m.extra.setStrDict(extra)
		d = '' 
		if type(aoid_)==type(0) or type(aoid_) == type(0.1): aoid_=str(aoid_)
		if not aoid_: aoid_=''
		try:
			aoid_ = aoid_.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(aoid_)))
		d += str(aoid_)
		m.paramstream += d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		if not timeout: timeout = tce.RpcCommunicator.instance().getRpcCallTimeout()
		m2 = None
		try:
			m2 = m.mtx.get(timeout=timeout)
		except:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def closeListen_oneway(self,aoid_,extra={}):
		# function index: 33
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 9
			m.opidx = 1
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
			m.extra.setStrDict(extra)
			d = '' 
			if type(aoid_)==type(0) or type(aoid_) == type(0.1): aoid_=str(aoid_)
			if not aoid_: aoid_=''
			try:
				aoid_ = aoid_.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(aoid_)))
			d += str(aoid_)
			m.paramstream += d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	#extra must be map<string,string>
	def getVersion(self,aoid_,timeout=None,extra={}):
		# function index: 33
		
		m = tce.RpcMessageCall()
		m.ifidx = 9
		m.opidx = 2
		m.extra.setStrDict(extra)
		d = '' 
		if type(aoid_)==type(0) or type(aoid_) == type(0.1): aoid_=str(aoid_)
		if not aoid_: aoid_=''
		try:
			aoid_ = aoid_.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(aoid_)))
		d += str(aoid_)
		m.paramstream += d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		if not timeout: timeout = tce.RpcCommunicator.instance().getRpcCallTimeout()
		m2 = None
		try:
			m2 = m.mtx.get(timeout=timeout)
		except:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
		idx = 0
		d = m.paramstream
		p = None
		r = False
		try:
			p = None
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			p = d[idx:idx+size]
			idx+=size
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_UNSERIALIZE_FAILED)
		return p
	
	def getVersion_async(self,aoid_,async,extra={}):
		# function index: 33
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 9
		m.opidx = 2
		m.extra.setStrDict(extra)
		d = '' 
		if type(aoid_)==type(0) or type(aoid_) == type(0.1): aoid_=str(aoid_)
		if not aoid_: aoid_=''
		try:
			aoid_ = aoid_.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(aoid_)))
		d += str(aoid_)
		m.paramstream += d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
		m.async = async
		m.asyncparser = IAoModuleCtrlPrx.getVersion_asyncparser
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def getVersion_asyncparser(m,m2):
		# function index: 33 , m2 - callreturn msg.
		
		stream = m2.paramstream
		user = m.async
		prx = m.prx
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC: return 
		try:
			idx = 0
			d = stream
			r = True
			p = None
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			p = d[idx:idx+size]
			idx+=size
			if r:
				user(p,prx)
		except:
			traceback.print_exc()
		
	
	#extra must be map<string,string>
	def onceNamed(self,aoid_,timeout=None,extra={}):
		# function index: 33
		
		m = tce.RpcMessageCall()
		m.ifidx = 9
		m.opidx = 3
		m.extra.setStrDict(extra)
		d = '' 
		if type(aoid_)==type(0) or type(aoid_) == type(0.1): aoid_=str(aoid_)
		if not aoid_: aoid_=''
		try:
			aoid_ = aoid_.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(aoid_)))
		d += str(aoid_)
		m.paramstream += d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		if not timeout: timeout = tce.RpcCommunicator.instance().getRpcCallTimeout()
		m2 = None
		try:
			m2 = m.mtx.get(timeout=timeout)
		except:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def onceNamed_oneway(self,aoid_,extra={}):
		# function index: 33
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 9
			m.opidx = 3
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
			m.extra.setStrDict(extra)
			d = '' 
			if type(aoid_)==type(0) or type(aoid_) == type(0.1): aoid_=str(aoid_)
			if not aoid_: aoid_=''
			try:
				aoid_ = aoid_.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(aoid_)))
			d += str(aoid_)
			m.paramstream += d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	#extra must be map<string,string>
	def speedLimit(self,aoid_,high_,low_,timeout=None,extra={}):
		# function index: 33
		
		m = tce.RpcMessageCall()
		m.ifidx = 9
		m.opidx = 4
		m.extra.setStrDict(extra)
		d = '' 
		if type(aoid_)==type(0) or type(aoid_) == type(0.1): aoid_=str(aoid_)
		if not aoid_: aoid_=''
		try:
			aoid_ = aoid_.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(aoid_)))
		d += str(aoid_)
		m.paramstream += d
		d = '' 
		d += struct.pack('!i',high_)
		m.paramstream += d
		d = '' 
		d += struct.pack('!i',low_)
		m.paramstream += d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		if not timeout: timeout = tce.RpcCommunicator.instance().getRpcCallTimeout()
		m2 = None
		try:
			m2 = m.mtx.get(timeout=timeout)
		except:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def speedLimit_oneway(self,aoid_,high_,low_,extra={}):
		# function index: 33
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 9
			m.opidx = 4
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
			m.extra.setStrDict(extra)
			d = '' 
			if type(aoid_)==type(0) or type(aoid_) == type(0.1): aoid_=str(aoid_)
			if not aoid_: aoid_=''
			try:
				aoid_ = aoid_.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(aoid_)))
			d += str(aoid_)
			m.paramstream += d
			d = '' 
			d += struct.pack('!i',high_)
			m.paramstream += d
			d = '' 
			d += struct.pack('!i',low_)
			m.paramstream += d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	#extra must be map<string,string>
	def oilCtrl(self,aoid_,onoff_,timeout=None,extra={}):
		# function index: 33
		
		m = tce.RpcMessageCall()
		m.ifidx = 9
		m.opidx = 5
		m.extra.setStrDict(extra)
		d = '' 
		if type(aoid_)==type(0) or type(aoid_) == type(0.1): aoid_=str(aoid_)
		if not aoid_: aoid_=''
		try:
			aoid_ = aoid_.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(aoid_)))
		d += str(aoid_)
		m.paramstream += d
		d = '' 
		if onoff_ == True:onoff_=1
		else: onoff_=0
		d += struct.pack('B',onoff_)
		m.paramstream += d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		if not timeout: timeout = tce.RpcCommunicator.instance().getRpcCallTimeout()
		m2 = None
		try:
			m2 = m.mtx.get(timeout=timeout)
		except:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def oilCtrl_oneway(self,aoid_,onoff_,extra={}):
		# function index: 33
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 9
			m.opidx = 5
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
			m.extra.setStrDict(extra)
			d = '' 
			if type(aoid_)==type(0) or type(aoid_) == type(0.1): aoid_=str(aoid_)
			if not aoid_: aoid_=''
			try:
				aoid_ = aoid_.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(aoid_)))
			d += str(aoid_)
			m.paramstream += d
			d = '' 
			if onoff_ == True:onoff_=1
			else: onoff_=0
			d += struct.pack('B',onoff_)
			m.paramstream += d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	#extra must be map<string,string>
	def reset(self,aoid_,timeout=None,extra={}):
		# function index: 33
		
		m = tce.RpcMessageCall()
		m.ifidx = 9
		m.opidx = 6
		m.extra.setStrDict(extra)
		d = '' 
		if type(aoid_)==type(0) or type(aoid_) == type(0.1): aoid_=str(aoid_)
		if not aoid_: aoid_=''
		try:
			aoid_ = aoid_.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(aoid_)))
		d += str(aoid_)
		m.paramstream += d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		if not timeout: timeout = tce.RpcCommunicator.instance().getRpcCallTimeout()
		m2 = None
		try:
			m2 = m.mtx.get(timeout=timeout)
		except:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def reset_oneway(self,aoid_,extra={}):
		# function index: 33
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 9
			m.opidx = 6
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
			m.extra.setStrDict(extra)
			d = '' 
			if type(aoid_)==type(0) or type(aoid_) == type(0.1): aoid_=str(aoid_)
			if not aoid_: aoid_=''
			try:
				aoid_ = aoid_.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(aoid_)))
			d += str(aoid_)
			m.paramstream += d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	#extra must be map<string,string>
	def setFreqAccOn(self,aoid_,freq_,timeout=None,extra={}):
		# function index: 33
		
		m = tce.RpcMessageCall()
		m.ifidx = 9
		m.opidx = 7
		m.extra.setStrDict(extra)
		d = '' 
		if type(aoid_)==type(0) or type(aoid_) == type(0.1): aoid_=str(aoid_)
		if not aoid_: aoid_=''
		try:
			aoid_ = aoid_.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(aoid_)))
		d += str(aoid_)
		m.paramstream += d
		d = '' 
		d += struct.pack('!i',freq_)
		m.paramstream += d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		if not timeout: timeout = tce.RpcCommunicator.instance().getRpcCallTimeout()
		m2 = None
		try:
			m2 = m.mtx.get(timeout=timeout)
		except:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def setFreqAccOn_oneway(self,aoid_,freq_,extra={}):
		# function index: 33
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 9
			m.opidx = 7
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
			m.extra.setStrDict(extra)
			d = '' 
			if type(aoid_)==type(0) or type(aoid_) == type(0.1): aoid_=str(aoid_)
			if not aoid_: aoid_=''
			try:
				aoid_ = aoid_.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(aoid_)))
			d += str(aoid_)
			m.paramstream += d
			d = '' 
			d += struct.pack('!i',freq_)
			m.paramstream += d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	#extra must be map<string,string>
	def setFreqAccOff(self,aoid_,freq_,timeout=None,extra={}):
		# function index: 33
		
		m = tce.RpcMessageCall()
		m.ifidx = 9
		m.opidx = 8
		m.extra.setStrDict(extra)
		d = '' 
		if type(aoid_)==type(0) or type(aoid_) == type(0.1): aoid_=str(aoid_)
		if not aoid_: aoid_=''
		try:
			aoid_ = aoid_.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(aoid_)))
		d += str(aoid_)
		m.paramstream += d
		d = '' 
		d += struct.pack('!i',freq_)
		m.paramstream += d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		if not timeout: timeout = tce.RpcCommunicator.instance().getRpcCallTimeout()
		m2 = None
		try:
			m2 = m.mtx.get(timeout=timeout)
		except:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def setFreqAccOff_oneway(self,aoid_,freq_,extra={}):
		# function index: 33
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 9
			m.opidx = 8
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
			m.extra.setStrDict(extra)
			d = '' 
			if type(aoid_)==type(0) or type(aoid_) == type(0.1): aoid_=str(aoid_)
			if not aoid_: aoid_=''
			try:
				aoid_ = aoid_.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(aoid_)))
			d += str(aoid_)
			m.paramstream += d
			d = '' 
			d += struct.pack('!i',freq_)
			m.paramstream += d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	#extra must be map<string,string>
	def setBarrierLeave(self,aoid_,x1_,y1_,x2_,y2_,timeout=None,extra={}):
		# function index: 33
		
		m = tce.RpcMessageCall()
		m.ifidx = 9
		m.opidx = 9
		m.extra.setStrDict(extra)
		d = '' 
		if type(aoid_)==type(0) or type(aoid_) == type(0.1): aoid_=str(aoid_)
		if not aoid_: aoid_=''
		try:
			aoid_ = aoid_.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(aoid_)))
		d += str(aoid_)
		m.paramstream += d
		d = '' 
		d += struct.pack('!f',x1_)
		m.paramstream += d
		d = '' 
		d += struct.pack('!f',y1_)
		m.paramstream += d
		d = '' 
		d += struct.pack('!f',x2_)
		m.paramstream += d
		d = '' 
		d += struct.pack('!f',y2_)
		m.paramstream += d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		if not timeout: timeout = tce.RpcCommunicator.instance().getRpcCallTimeout()
		m2 = None
		try:
			m2 = m.mtx.get(timeout=timeout)
		except:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def setBarrierLeave_oneway(self,aoid_,x1_,y1_,x2_,y2_,extra={}):
		# function index: 33
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 9
			m.opidx = 9
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
			m.extra.setStrDict(extra)
			d = '' 
			if type(aoid_)==type(0) or type(aoid_) == type(0.1): aoid_=str(aoid_)
			if not aoid_: aoid_=''
			try:
				aoid_ = aoid_.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(aoid_)))
			d += str(aoid_)
			m.paramstream += d
			d = '' 
			d += struct.pack('!f',x1_)
			m.paramstream += d
			d = '' 
			d += struct.pack('!f',y1_)
			m.paramstream += d
			d = '' 
			d += struct.pack('!f',x2_)
			m.paramstream += d
			d = '' 
			d += struct.pack('!f',y2_)
			m.paramstream += d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	#extra must be map<string,string>
	def setBarrierEnter(self,aoid_,x1_,y1_,x2_,y2_,timeout=None,extra={}):
		# function index: 33
		
		m = tce.RpcMessageCall()
		m.ifidx = 9
		m.opidx = 10
		m.extra.setStrDict(extra)
		d = '' 
		if type(aoid_)==type(0) or type(aoid_) == type(0.1): aoid_=str(aoid_)
		if not aoid_: aoid_=''
		try:
			aoid_ = aoid_.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(aoid_)))
		d += str(aoid_)
		m.paramstream += d
		d = '' 
		d += struct.pack('!f',x1_)
		m.paramstream += d
		d = '' 
		d += struct.pack('!f',y1_)
		m.paramstream += d
		d = '' 
		d += struct.pack('!f',x2_)
		m.paramstream += d
		d = '' 
		d += struct.pack('!f',y2_)
		m.paramstream += d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		if not timeout: timeout = tce.RpcCommunicator.instance().getRpcCallTimeout()
		m2 = None
		try:
			m2 = m.mtx.get(timeout=timeout)
		except:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def setBarrierEnter_oneway(self,aoid_,x1_,y1_,x2_,y2_,extra={}):
		# function index: 33
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 9
			m.opidx = 10
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
			m.extra.setStrDict(extra)
			d = '' 
			if type(aoid_)==type(0) or type(aoid_) == type(0.1): aoid_=str(aoid_)
			if not aoid_: aoid_=''
			try:
				aoid_ = aoid_.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(aoid_)))
			d += str(aoid_)
			m.paramstream += d
			d = '' 
			d += struct.pack('!f',x1_)
			m.paramstream += d
			d = '' 
			d += struct.pack('!f',y1_)
			m.paramstream += d
			d = '' 
			d += struct.pack('!f',x2_)
			m.paramstream += d
			d = '' 
			d += struct.pack('!f',y2_)
			m.paramstream += d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	#extra must be map<string,string>
	def clearAlarms(self,aoid_,timeout=None,extra={}):
		# function index: 33
		
		m = tce.RpcMessageCall()
		m.ifidx = 9
		m.opidx = 11
		m.extra.setStrDict(extra)
		d = '' 
		if type(aoid_)==type(0) or type(aoid_) == type(0.1): aoid_=str(aoid_)
		if not aoid_: aoid_=''
		try:
			aoid_ = aoid_.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(aoid_)))
		d += str(aoid_)
		m.paramstream += d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		if not timeout: timeout = tce.RpcCommunicator.instance().getRpcCallTimeout()
		m2 = None
		try:
			m2 = m.mtx.get(timeout=timeout)
		except:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def clearAlarms_oneway(self,aoid_,extra={}):
		# function index: 33
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 9
			m.opidx = 11
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
			m.extra.setStrDict(extra)
			d = '' 
			if type(aoid_)==type(0) or type(aoid_) == type(0.1): aoid_=str(aoid_)
			if not aoid_: aoid_=''
			try:
				aoid_ = aoid_.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(aoid_)))
			d += str(aoid_)
			m.paramstream += d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	#extra must be map<string,string>
	def clearMiles(self,aoid_,miles_,timeout=None,extra={}):
		# function index: 33
		
		m = tce.RpcMessageCall()
		m.ifidx = 9
		m.opidx = 12
		m.extra.setStrDict(extra)
		d = '' 
		if type(aoid_)==type(0) or type(aoid_) == type(0.1): aoid_=str(aoid_)
		if not aoid_: aoid_=''
		try:
			aoid_ = aoid_.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(aoid_)))
		d += str(aoid_)
		m.paramstream += d
		d = '' 
		d += struct.pack('!i',miles_)
		m.paramstream += d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		if not timeout: timeout = tce.RpcCommunicator.instance().getRpcCallTimeout()
		m2 = None
		try:
			m2 = m.mtx.get(timeout=timeout)
		except:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def clearMiles_oneway(self,aoid_,miles_,extra={}):
		# function index: 33
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 9
			m.opidx = 12
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
			m.extra.setStrDict(extra)
			d = '' 
			if type(aoid_)==type(0) or type(aoid_) == type(0.1): aoid_=str(aoid_)
			if not aoid_: aoid_=''
			try:
				aoid_ = aoid_.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(aoid_)))
			d += str(aoid_)
			m.paramstream += d
			d = '' 
			d += struct.pack('!i',miles_)
			m.paramstream += d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	

class IDtuService:
	# -- INTERFACE -- 
	def __init__(self):
		if not hasattr(self,'delegatecls'):
			self.delegatecls = {}
		self.delegatecls[10] = IDtuService_delegate
	
	def getProps(self,ctx):
		return {}

class IDtuService_delegate:
	def __init__(self,inst,adapter,conn=None):
		self.index = 10
		self.optlist={}
		self.id = '' 
		self.adapter = adapter
		self.optlist[0] = (self.getProps)
		
		self.inst = inst
	
	def getProps(self,ctx):
		print "callin (getProps)"
		d = ctx.msg.paramstream 
		idx = 0
		cr = None
		cr = self.inst.getProps(ctx)
		if  cr == None: return True
		d = '' 
		m = tce.RpcMessageReturn()
		m.sequence = ctx.msg.sequence
		m.callmsg = ctx.msg
		m.ifidx = ctx.msg.ifidx
		m.call_id = ctx.msg.call_id
		m.conn = ctx.msg.conn
		m.extra = ctx.msg.extra
		container = Properties_t(cr)
		d += container.marshall()
		if d: m.paramstream += d
		ctx.conn.sendMessage(m)
		return True
	
	
class IDtuServicePrx:
	# -- INTERFACE PROXY -- 
	def __init__(self,conn):
		self.conn = conn
		self.delta = None
		pass
	
	@staticmethod
	def create(address):
		conn = tce.RpcConnectionSocket()
		conn.open(address)
		proxy = IDtuServicePrx(conn)
		return proxy
	
	@staticmethod
	def createWithEpName(name):
		ep = tce.RpcCommunicator.instance().currentServer().findEndPointByName(name)
		if not ep: return None
		conn = ep.impl
		proxy = IDtuServicePrx(conn)
		return proxy
	
	@staticmethod
	def createWithProxy(prx):
		proxy = IDtuServicePrx(prx.conn)
		return proxy
	
	#extra must be map<string,string>
	def getProps(self,timeout=None,extra={}):
		# function index: 34
		
		m = tce.RpcMessageCall()
		m.ifidx = 10
		m.opidx = 0
		m.extra.setStrDict(extra)
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		if not timeout: timeout = tce.RpcCommunicator.instance().getRpcCallTimeout()
		m2 = None
		try:
			m2 = m.mtx.get(timeout=timeout)
		except:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
		idx = 0
		d = m.paramstream
		p = None
		r = False
		try:
			p ={}
			container = Properties_t(p)
			r,idx = container.unmarshall(d,idx)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_UNSERIALIZE_FAILED)
		return p
	
	def getProps_async(self,async,extra={}):
		# function index: 34
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 10
		m.opidx = 0
		m.extra.setStrDict(extra)
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcCommunicator.instance().currentServer().getId()
		m.async = async
		m.asyncparser = IDtuServicePrx.getProps_asyncparser
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def getProps_asyncparser(m,m2):
		# function index: 34 , m2 - callreturn msg.
		
		stream = m2.paramstream
		user = m.async
		prx = m.prx
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC: return 
		try:
			idx = 0
			d = stream
			r = True
			p ={}
			container = Properties_t(p)
			r,idx = container.unmarshall(d,idx)
			if r:
				user(p,prx)
		except:
			traceback.print_exc()
		
	

