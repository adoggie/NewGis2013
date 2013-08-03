
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

class StrStr_t:
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

class StrStrList_t:
	# -- SEQUENCE --
	def __init__(self,array):
		self.ds = array
		
	def marshall(self):
		d = '' 
		d += struct.pack('!I',len(self.ds))
		for o in self.ds:
			container = StrStr_t(o)
			d += container.marshall()
		return d
		
	def unmarshall(self,d,idx_=0):
		idx = idx_
		try:
			size_,= struct.unpack('!I',d[idx:idx+4])
			idx += 4
			p = 0
			while p < size_:
				o ={}
				container = StrStr_t(o)
				r,idx = container.unmarshall(d,idx)
				if not r: return False,idx
				self.ds.append(o)
				p+=1
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
		

class GpsInfo_t:
# -- STRUCT -- 
	def __init__(self,loc=GeoPoint_t(),speed=0.0,direction=0.0,timesec=0):
		self.loc = loc
		self.speed = speed
		self.direction = direction
		self.timesec = timesec
		
	def __str__(self):
		return 'OBJECT<GpsInfo_t :%s> { loc:%s,speed:%s,direction:%s,timesec:%s}'%(hex(id(self)),str(self.loc),str(self.speed),str(self.direction),str(self.timesec) ) 
		
	def marshall(self):
		d =''
		d += self.loc.marshall()
		d += struct.pack('!f',self.speed)
		d += struct.pack('!f',self.direction)
		d += struct.pack('!i',self.timesec)
		return d
		
	def unmarshall(self,d,idx_=0):
		idx = idx_
		try:
			r,idx = self.loc.unmarshall(d,idx)
			if not r: return False,idx
			self.speed, = struct.unpack('!f',d[idx:idx+4])
			idx+=4
			self.direction, = struct.unpack('!f',d[idx:idx+4])
			idx+=4
			self.timesec, = struct.unpack('!i',d[idx:idx+4])
			idx+=4
		except:
			traceback.print_exc()
			return False,idx
		return True,idx
		

class LocationInfo_t:
# -- STRUCT -- 
	def __init__(self,user_id='',gps=GpsInfo_t(),desc=''):
		self.user_id = user_id
		self.gps = gps
		self.desc = desc
		
	def __str__(self):
		return 'OBJECT<LocationInfo_t :%s> { user_id:%s,gps:%s,desc:%s}'%(hex(id(self)),str(self.user_id),str(self.gps),str(self.desc) ) 
		
	def marshall(self):
		d =''
		if type(self.user_id)==type(0) or type(self.user_id) == type(0.1): self.user_id=str(self.user_id)
		if not self.user_id: self.user_id=''
		try:
			self.user_id = self.user_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.user_id)))
		d += str(self.user_id)
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
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.user_id = d[idx:idx+size]
			idx+=size
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

class StrangerInfo_t:
# -- STRUCT -- 
	def __init__(self,userid='',usertype=0,loc=LocationInfo_t()):
		self.userid = userid
		self.usertype = usertype
		self.loc = loc
		
	def __str__(self):
		return 'OBJECT<StrangerInfo_t :%s> { userid:%s,usertype:%s,loc:%s}'%(hex(id(self)),str(self.userid),str(self.usertype),str(self.loc) ) 
		
	def marshall(self):
		d =''
		if type(self.userid)==type(0) or type(self.userid) == type(0.1): self.userid=str(self.userid)
		if not self.userid: self.userid=''
		try:
			self.userid = self.userid.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.userid)))
		d += str(self.userid)
		d += struct.pack('!i',self.usertype)
		d += self.loc.marshall()
		return d
		
	def unmarshall(self,d,idx_=0):
		idx = idx_
		try:
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.userid = d[idx:idx+size]
			idx+=size
			self.usertype, = struct.unpack('!i',d[idx:idx+4])
			idx+=4
			r,idx = self.loc.unmarshall(d,idx)
			if not r: return False,idx
		except:
			traceback.print_exc()
			return False,idx
		return True,idx
		

class StrangerInfoList_t:
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
				o = StrangerInfo_t()
				r,idx = o.unmarshall(d,idx)
				if not r: return False,idx
				self.ds.append(o)
				p+=1
		except:
			traceback.print_exc()
			return False,idx
		return True,idx

class StrangerSearchCase_t:
# -- STRUCT -- 
	def __init__(self,type=0,rect=GeoRect_t(),circle=GeoCircle_t(),limit=0,order=0,target_type=0,target_subtype=0):
		self.type = type
		self.rect = rect
		self.circle = circle
		self.limit = limit
		self.order = order
		self.target_type = target_type
		self.target_subtype = target_subtype
		
	def __str__(self):
		return 'OBJECT<StrangerSearchCase_t :%s> { type:%s,rect:%s,circle:%s,limit:%s,order:%s,target_type:%s,target_subtype:%s}'%(hex(id(self)),str(self.type),str(self.rect),str(self.circle),str(self.limit),str(self.order),str(self.target_type),str(self.target_subtype) ) 
		
	def marshall(self):
		d =''
		d += struct.pack('!i',self.type)
		d += self.rect.marshall()
		d += self.circle.marshall()
		d += struct.pack('!i',self.limit)
		d += struct.pack('!i',self.order)
		d += struct.pack('!i',self.target_type)
		d += struct.pack('!i',self.target_subtype)
		return d
		
	def unmarshall(self,d,idx_=0):
		idx = idx_
		try:
			self.type, = struct.unpack('!i',d[idx:idx+4])
			idx+=4
			r,idx = self.rect.unmarshall(d,idx)
			if not r: return False,idx
			r,idx = self.circle.unmarshall(d,idx)
			if not r: return False,idx
			self.limit, = struct.unpack('!i',d[idx:idx+4])
			idx+=4
			self.order, = struct.unpack('!i',d[idx:idx+4])
			idx+=4
			self.target_type, = struct.unpack('!i',d[idx:idx+4])
			idx+=4
			self.target_subtype, = struct.unpack('!i',d[idx:idx+4])
			idx+=4
		except:
			traceback.print_exc()
			return False,idx
		return True,idx
		

class UserInfo_t:
# -- STRUCT -- 
	def __init__(self,id='',username='',name='',age=0,sex=0,phone='',city='',address='',email='',status=0,lock_reason='',icon='',signtext='',groupid='',usertype=0,invlink=''):
		self.id = id
		self.username = username
		self.name = name
		self.age = age
		self.sex = sex
		self.phone = phone
		self.city = city
		self.address = address
		self.email = email
		self.status = status
		self.lock_reason = lock_reason
		self.icon = icon
		self.signtext = signtext
		self.groupid = groupid
		self.usertype = usertype
		self.invlink = invlink
		
	def __str__(self):
		return 'OBJECT<UserInfo_t :%s> { id:%s,username:%s,name:%s,age:%s,sex:%s,phone:%s,city:%s,address:%s,email:%s,status:%s,lock_reason:%s,icon:%s,signtext:%s,groupid:%s,usertype:%s,invlink:%s}'%(hex(id(self)),str(self.id),str(self.username),str(self.name),str(self.age),str(self.sex),str(self.phone),str(self.city),str(self.address),str(self.email),str(self.status),str(self.lock_reason),str(self.icon),str(self.signtext),str(self.groupid),str(self.usertype),str(self.invlink) ) 
		
	def marshall(self):
		d =''
		if type(self.id)==type(0) or type(self.id) == type(0.1): self.id=str(self.id)
		if not self.id: self.id=''
		try:
			self.id = self.id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.id)))
		d += str(self.id)
		if type(self.username)==type(0) or type(self.username) == type(0.1): self.username=str(self.username)
		if not self.username: self.username=''
		try:
			self.username = self.username.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.username)))
		d += str(self.username)
		if type(self.name)==type(0) or type(self.name) == type(0.1): self.name=str(self.name)
		if not self.name: self.name=''
		try:
			self.name = self.name.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.name)))
		d += str(self.name)
		d += struct.pack('!i',self.age)
		d += struct.pack('!i',self.sex)
		if type(self.phone)==type(0) or type(self.phone) == type(0.1): self.phone=str(self.phone)
		if not self.phone: self.phone=''
		try:
			self.phone = self.phone.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.phone)))
		d += str(self.phone)
		if type(self.city)==type(0) or type(self.city) == type(0.1): self.city=str(self.city)
		if not self.city: self.city=''
		try:
			self.city = self.city.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.city)))
		d += str(self.city)
		if type(self.address)==type(0) or type(self.address) == type(0.1): self.address=str(self.address)
		if not self.address: self.address=''
		try:
			self.address = self.address.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.address)))
		d += str(self.address)
		if type(self.email)==type(0) or type(self.email) == type(0.1): self.email=str(self.email)
		if not self.email: self.email=''
		try:
			self.email = self.email.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.email)))
		d += str(self.email)
		d += struct.pack('!i',self.status)
		if type(self.lock_reason)==type(0) or type(self.lock_reason) == type(0.1): self.lock_reason=str(self.lock_reason)
		if not self.lock_reason: self.lock_reason=''
		try:
			self.lock_reason = self.lock_reason.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.lock_reason)))
		d += str(self.lock_reason)
		if type(self.icon)==type(0) or type(self.icon) == type(0.1): self.icon=str(self.icon)
		if not self.icon: self.icon=''
		try:
			self.icon = self.icon.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.icon)))
		d += str(self.icon)
		if type(self.signtext)==type(0) or type(self.signtext) == type(0.1): self.signtext=str(self.signtext)
		if not self.signtext: self.signtext=''
		try:
			self.signtext = self.signtext.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.signtext)))
		d += str(self.signtext)
		if type(self.groupid)==type(0) or type(self.groupid) == type(0.1): self.groupid=str(self.groupid)
		if not self.groupid: self.groupid=''
		try:
			self.groupid = self.groupid.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.groupid)))
		d += str(self.groupid)
		d += struct.pack('!i',self.usertype)
		if type(self.invlink)==type(0) or type(self.invlink) == type(0.1): self.invlink=str(self.invlink)
		if not self.invlink: self.invlink=''
		try:
			self.invlink = self.invlink.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.invlink)))
		d += str(self.invlink)
		return d
		
	def unmarshall(self,d,idx_=0):
		idx = idx_
		try:
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.id = d[idx:idx+size]
			idx+=size
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.username = d[idx:idx+size]
			idx+=size
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.name = d[idx:idx+size]
			idx+=size
			self.age, = struct.unpack('!i',d[idx:idx+4])
			idx+=4
			self.sex, = struct.unpack('!i',d[idx:idx+4])
			idx+=4
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.phone = d[idx:idx+size]
			idx+=size
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.city = d[idx:idx+size]
			idx+=size
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.address = d[idx:idx+size]
			idx+=size
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.email = d[idx:idx+size]
			idx+=size
			self.status, = struct.unpack('!i',d[idx:idx+4])
			idx+=4
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.lock_reason = d[idx:idx+size]
			idx+=size
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.icon = d[idx:idx+size]
			idx+=size
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.signtext = d[idx:idx+size]
			idx+=size
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.groupid = d[idx:idx+size]
			idx+=size
			self.usertype, = struct.unpack('!i',d[idx:idx+4])
			idx+=4
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.invlink = d[idx:idx+size]
			idx+=size
		except:
			traceback.print_exc()
			return False,idx
		return True,idx
		

class UserInfoList_t:
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
				o = UserInfo_t()
				r,idx = o.unmarshall(d,idx)
				if not r: return False,idx
				self.ds.append(o)
				p+=1
		except:
			traceback.print_exc()
			return False,idx
		return True,idx

class UserInfoDetail_t:
# -- STRUCT -- 
	def __init__(self,user_id=''):
		self.user_id = user_id
		
	def __str__(self):
		return 'OBJECT<UserInfoDetail_t :%s> { user_id:%s}'%(hex(id(self)),str(self.user_id) ) 
		
	def marshall(self):
		d =''
		if type(self.user_id)==type(0) or type(self.user_id) == type(0.1): self.user_id=str(self.user_id)
		if not self.user_id: self.user_id=''
		try:
			self.user_id = self.user_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.user_id)))
		d += str(self.user_id)
		return d
		
	def unmarshall(self,d,idx_=0):
		idx = idx_
		try:
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.user_id = d[idx:idx+size]
			idx+=size
		except:
			traceback.print_exc()
			return False,idx
		return True,idx
		

class UserGroupInfo_t:
# -- STRUCT -- 
	def __init__(self,id='',name=''):
		self.id = id
		self.name = name
		
	def __str__(self):
		return 'OBJECT<UserGroupInfo_t :%s> { id:%s,name:%s}'%(hex(id(self)),str(self.id),str(self.name) ) 
		
	def marshall(self):
		d =''
		if type(self.id)==type(0) or type(self.id) == type(0.1): self.id=str(self.id)
		if not self.id: self.id=''
		try:
			self.id = self.id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.id)))
		d += str(self.id)
		if type(self.name)==type(0) or type(self.name) == type(0.1): self.name=str(self.name)
		if not self.name: self.name=''
		try:
			self.name = self.name.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.name)))
		d += str(self.name)
		return d
		
	def unmarshall(self,d,idx_=0):
		idx = idx_
		try:
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.id = d[idx:idx+size]
			idx+=size
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.name = d[idx:idx+size]
			idx+=size
		except:
			traceback.print_exc()
			return False,idx
		return True,idx
		

class UserGroupInfoList_t:
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
				o = UserGroupInfo_t()
				r,idx = o.unmarshall(d,idx)
				if not r: return False,idx
				self.ds.append(o)
				p+=1
		except:
			traceback.print_exc()
			return False,idx
		return True,idx

class StreamData_t:
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

class BinaryStream_t:
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

class LL:
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
				x=[]
				size, = struct.unpack('!I',d[idx:idx+4])
				idx+=4
				x = d[idx:idx+size]
				idx+=size
				y=[]
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

class MimeImage_t:
# -- STRUCT -- 
	def __init__(self,type=0,width=0,height=0,data='',data64=''):
		self.type = type
		self.width = width
		self.height = height
		self.data = data
		self.data64 = data64
		
	def __str__(self):
		return 'OBJECT<MimeImage_t :%s> { type:%s,width:%s,height:%s,data:%s,data64:%s}'%(hex(id(self)),str(self.type),str(self.width),str(self.height),str(self.data),str(self.data64) ) 
		
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
		

class MimeText_t:
# -- STRUCT -- 
	def __init__(self,type=0,text=''):
		self.type = type
		self.text = text
		
	def __str__(self):
		return 'OBJECT<MimeText_t :%s> { type:%s,text:%s}'%(hex(id(self)),str(self.type),str(self.text) ) 
		
	def marshall(self):
		d =''
		d += struct.pack('!i',self.type)
		if type(self.text)==type(0) or type(self.text) == type(0.1): self.text=str(self.text)
		if not self.text: self.text=''
		try:
			self.text = self.text.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.text)))
		d += str(self.text)
		return d
		
	def unmarshall(self,d,idx_=0):
		idx = idx_
		try:
			self.type, = struct.unpack('!i',d[idx:idx+4])
			idx+=4
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.text = d[idx:idx+size]
			idx+=size
		except:
			traceback.print_exc()
			return False,idx
		return True,idx
		

class MimeAudioClip_t:
# -- STRUCT -- 
	def __init__(self,type=0,samples=0,channel=0,timelen=0,data=''):
		self.type = type
		self.samples = samples
		self.channel = channel
		self.timelen = timelen
		self.data = data
		
	def __str__(self):
		return 'OBJECT<MimeAudioClip_t :%s> { type:%s,samples:%s,channel:%s,timelen:%s,data:%s}'%(hex(id(self)),str(self.type),str(self.samples),str(self.channel),str(self.timelen),str(self.data) ) 
		
	def marshall(self):
		d =''
		d += struct.pack('!h',self.type)
		d += struct.pack('!h',self.samples)
		d += struct.pack('!h',self.channel)
		d += struct.pack('!h',self.timelen)
		container = StreamData_t(self.data)
		d += container.marshall()
		return d
		
	def unmarshall(self,d,idx_=0):
		idx = idx_
		try:
			self.type, = struct.unpack('!h',d[idx:idx+2])
			idx+=2
			self.samples, = struct.unpack('!h',d[idx:idx+2])
			idx+=2
			self.channel, = struct.unpack('!h',d[idx:idx+2])
			idx+=2
			self.timelen, = struct.unpack('!h',d[idx:idx+2])
			idx+=2
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.data = d[idx:idx+size]
			idx+=size
		except:
			traceback.print_exc()
			return False,idx
		return True,idx
		

class MimeMessage_t:
# -- STRUCT -- 
	def __init__(self,type=0,text=MimeText_t(),image=MimeImage_t(),audio=MimeAudioClip_t(),timesec=0,sender_id=''):
		self.type = type
		self.text = text
		self.image = image
		self.audio = audio
		self.timesec = timesec
		self.sender_id = sender_id
		
	def __str__(self):
		return 'OBJECT<MimeMessage_t :%s> { type:%s,text:%s,image:%s,audio:%s,timesec:%s,sender_id:%s}'%(hex(id(self)),str(self.type),str(self.text),str(self.image),str(self.audio),str(self.timesec),str(self.sender_id) ) 
		
	def marshall(self):
		d =''
		d += struct.pack('!i',self.type)
		d += self.text.marshall()
		d += self.image.marshall()
		d += self.audio.marshall()
		d += struct.pack('!i',self.timesec)
		if type(self.sender_id)==type(0) or type(self.sender_id) == type(0.1): self.sender_id=str(self.sender_id)
		if not self.sender_id: self.sender_id=''
		try:
			self.sender_id = self.sender_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.sender_id)))
		d += str(self.sender_id)
		return d
		
	def unmarshall(self,d,idx_=0):
		idx = idx_
		try:
			self.type, = struct.unpack('!i',d[idx:idx+4])
			idx+=4
			r,idx = self.text.unmarshall(d,idx)
			if not r: return False,idx
			r,idx = self.image.unmarshall(d,idx)
			if not r: return False,idx
			r,idx = self.audio.unmarshall(d,idx)
			if not r: return False,idx
			self.timesec, = struct.unpack('!i',d[idx:idx+4])
			idx+=4
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.sender_id = d[idx:idx+size]
			idx+=size
		except:
			traceback.print_exc()
			return False,idx
		return True,idx
		

class MimeMessageList_t:
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
				o = MimeMessage_t()
				r,idx = o.unmarshall(d,idx)
				if not r: return False,idx
				self.ds.append(o)
				p+=1
		except:
			traceback.print_exc()
			return False,idx
		return True,idx

class FriendIdList_t:
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
		

class UserStatus_t:
# -- STRUCT -- 
	def __init__(self,userid='',status=0):
		self.userid = userid
		self.status = status
		
	def __str__(self):
		return 'OBJECT<UserStatus_t :%s> { userid:%s,status:%s}'%(hex(id(self)),str(self.userid),str(self.status) ) 
		
	def marshall(self):
		d =''
		if type(self.userid)==type(0) or type(self.userid) == type(0.1): self.userid=str(self.userid)
		if not self.userid: self.userid=''
		try:
			self.userid = self.userid.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.userid)))
		d += str(self.userid)
		d += struct.pack('!i',self.status)
		return d
		
	def unmarshall(self,d,idx_=0):
		idx = idx_
		try:
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.userid = d[idx:idx+size]
			idx+=size
			self.status, = struct.unpack('!i',d[idx:idx+4])
			idx+=4
		except:
			traceback.print_exc()
			return False,idx
		return True,idx
		

class UserStatusList_t:
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
				o = UserStatus_t()
				r,idx = o.unmarshall(d,idx)
				if not r: return False,idx
				self.ds.append(o)
				p+=1
		except:
			traceback.print_exc()
			return False,idx
		return True,idx

class QueryMessageLogResult_t:
# -- STRUCT -- 
	def __init__(self,msglist=[]):
		self.msglist = msglist
		
	def __str__(self):
		return 'OBJECT<QueryMessageLogResult_t :%s> { msglist:%s}'%(hex(id(self)),str(self.msglist) ) 
		
	def marshall(self):
		d =''
		container = MimeMessageList_t(self.msglist)
		d += container.marshall()
		return d
		
	def unmarshall(self,d,idx_=0):
		idx = idx_
		try:
			self.msglist = [ ]
			container = MimeMessageList_t(self.msglist)
			r,idx = container.unmarshall(d,idx)
			if not r: return False,idx
		except:
			traceback.print_exc()
			return False,idx
		return True,idx
		

class InviteResultInfo_t:
# -- STRUCT -- 
	def __init__(self,user_id='',type=0,reason=''):
		self.user_id = user_id
		self.type = type
		self.reason = reason
		
	def __str__(self):
		return 'OBJECT<InviteResultInfo_t :%s> { user_id:%s,type:%s,reason:%s}'%(hex(id(self)),str(self.user_id),str(self.type),str(self.reason) ) 
		
	def marshall(self):
		d =''
		if type(self.user_id)==type(0) or type(self.user_id) == type(0.1): self.user_id=str(self.user_id)
		if not self.user_id: self.user_id=''
		try:
			self.user_id = self.user_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.user_id)))
		d += str(self.user_id)
		d += struct.pack('!i',self.type)
		if type(self.reason)==type(0) or type(self.reason) == type(0.1): self.reason=str(self.reason)
		if not self.reason: self.reason=''
		try:
			self.reason = self.reason.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.reason)))
		d += str(self.reason)
		return d
		
	def unmarshall(self,d,idx_=0):
		idx = idx_
		try:
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.user_id = d[idx:idx+size]
			idx+=size
			self.type, = struct.unpack('!i',d[idx:idx+4])
			idx+=4
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.reason = d[idx:idx+size]
			idx+=size
		except:
			traceback.print_exc()
			return False,idx
		return True,idx
		

class InviteRequestInfo_t:
# -- STRUCT -- 
	def __init__(self,user_id='',user_name='',timesec=0,greeting=''):
		self.user_id = user_id
		self.user_name = user_name
		self.timesec = timesec
		self.greeting = greeting
		
	def __str__(self):
		return 'OBJECT<InviteRequestInfo_t :%s> { user_id:%s,user_name:%s,timesec:%s,greeting:%s}'%(hex(id(self)),str(self.user_id),str(self.user_name),str(self.timesec),str(self.greeting) ) 
		
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
		d += struct.pack('!i',self.timesec)
		if type(self.greeting)==type(0) or type(self.greeting) == type(0.1): self.greeting=str(self.greeting)
		if not self.greeting: self.greeting=''
		try:
			self.greeting = self.greeting.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.greeting)))
		d += str(self.greeting)
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
			self.timesec, = struct.unpack('!i',d[idx:idx+4])
			idx+=4
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.greeting = d[idx:idx+size]
			idx+=size
		except:
			traceback.print_exc()
			return False,idx
		return True,idx
		

class GatewayAdapterInfo_t:
# -- STRUCT -- 
	def __init__(self,host='',port=0):
		self.host = host
		self.port = port
		
	def __str__(self):
		return 'OBJECT<GatewayAdapterInfo_t :%s> { host:%s,port:%s}'%(hex(id(self)),str(self.host),str(self.port) ) 
		
	def marshall(self):
		d =''
		if type(self.host)==type(0) or type(self.host) == type(0.1): self.host=str(self.host)
		if not self.host: self.host=''
		try:
			self.host = self.host.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.host)))
		d += str(self.host)
		d += struct.pack('!i',self.port)
		return d
		
	def unmarshall(self,d,idx_=0):
		idx = idx_
		try:
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.host = d[idx:idx+size]
			idx+=size
			self.port, = struct.unpack('!i',d[idx:idx+4])
			idx+=4
		except:
			traceback.print_exc()
			return False,idx
		return True,idx
		

class GatewayAdapterInfoList_t:
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
				o = GatewayAdapterInfo_t()
				r,idx = o.unmarshall(d,idx)
				if not r: return False,idx
				self.ds.append(o)
				p+=1
		except:
			traceback.print_exc()
			return False,idx
		return True,idx

class TeamInfo_t:
# -- STRUCT -- 
	def __init__(self,id='',name='',desc=''):
		self.id = id
		self.name = name
		self.desc = desc
		
	def __str__(self):
		return 'OBJECT<TeamInfo_t :%s> { id:%s,name:%s,desc:%s}'%(hex(id(self)),str(self.id),str(self.name),str(self.desc) ) 
		
	def marshall(self):
		d =''
		if type(self.id)==type(0) or type(self.id) == type(0.1): self.id=str(self.id)
		if not self.id: self.id=''
		try:
			self.id = self.id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.id)))
		d += str(self.id)
		if type(self.name)==type(0) or type(self.name) == type(0.1): self.name=str(self.name)
		if not self.name: self.name=''
		try:
			self.name = self.name.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.name)))
		d += str(self.name)
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
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.id = d[idx:idx+size]
			idx+=size
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.name = d[idx:idx+size]
			idx+=size
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.desc = d[idx:idx+size]
			idx+=size
		except:
			traceback.print_exc()
			return False,idx
		return True,idx
		

class TeamInfoList_t:
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
				o = TeamInfo_t()
				r,idx = o.unmarshall(d,idx)
				if not r: return False,idx
				self.ds.append(o)
				p+=1
		except:
			traceback.print_exc()
			return False,idx
		return True,idx

class ServiceURI_t:
# -- STRUCT -- 
	def __init__(self,type=0,host='',port=0):
		self.type = type
		self.host = host
		self.port = port
		
	def __str__(self):
		return 'OBJECT<ServiceURI_t :%s> { type:%s,host:%s,port:%s}'%(hex(id(self)),str(self.type),str(self.host),str(self.port) ) 
		
	def marshall(self):
		d =''
		d += struct.pack('!i',self.type)
		if type(self.host)==type(0) or type(self.host) == type(0.1): self.host=str(self.host)
		if not self.host: self.host=''
		try:
			self.host = self.host.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.host)))
		d += str(self.host)
		d += struct.pack('!i',self.port)
		return d
		
	def unmarshall(self,d,idx_=0):
		idx = idx_
		try:
			self.type, = struct.unpack('!i',d[idx:idx+4])
			idx+=4
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.host = d[idx:idx+size]
			idx+=size
			self.port, = struct.unpack('!i',d[idx:idx+4])
			idx+=4
		except:
			traceback.print_exc()
			return False,idx
		return True,idx
		

class ServiceURIList_t:
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
				o = ServiceURI_t()
				r,idx = o.unmarshall(d,idx)
				if not r: return False,idx
				self.ds.append(o)
				p+=1
		except:
			traceback.print_exc()
			return False,idx
		return True,idx

class TalkingResource_t:
# -- STRUCT -- 
	def __init__(self,error=Error_t(),talking_id='',owner_id='',host='',port=0):
		self.error = error
		self.talking_id = talking_id
		self.owner_id = owner_id
		self.host = host
		self.port = port
		
	def __str__(self):
		return 'OBJECT<TalkingResource_t :%s> { error:%s,talking_id:%s,owner_id:%s,host:%s,port:%s}'%(hex(id(self)),str(self.error),str(self.talking_id),str(self.owner_id),str(self.host),str(self.port) ) 
		
	def marshall(self):
		d =''
		d += self.error.marshall()
		if type(self.talking_id)==type(0) or type(self.talking_id) == type(0.1): self.talking_id=str(self.talking_id)
		if not self.talking_id: self.talking_id=''
		try:
			self.talking_id = self.talking_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.talking_id)))
		d += str(self.talking_id)
		if type(self.owner_id)==type(0) or type(self.owner_id) == type(0.1): self.owner_id=str(self.owner_id)
		if not self.owner_id: self.owner_id=''
		try:
			self.owner_id = self.owner_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.owner_id)))
		d += str(self.owner_id)
		if type(self.host)==type(0) or type(self.host) == type(0.1): self.host=str(self.host)
		if not self.host: self.host=''
		try:
			self.host = self.host.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.host)))
		d += str(self.host)
		d += struct.pack('!i',self.port)
		return d
		
	def unmarshall(self,d,idx_=0):
		idx = idx_
		try:
			r,idx = self.error.unmarshall(d,idx)
			if not r: return False,idx
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.talking_id = d[idx:idx+size]
			idx+=size
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.owner_id = d[idx:idx+size]
			idx+=size
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.host = d[idx:idx+size]
			idx+=size
			self.port, = struct.unpack('!i',d[idx:idx+4])
			idx+=4
		except:
			traceback.print_exc()
			return False,idx
		return True,idx
		

class TermNotifyInfo_t:
# -- STRUCT -- 
	def __init__(self,type=0,p1='',p2='',p3=''):
		self.type = type
		self.p1 = p1
		self.p2 = p2
		self.p3 = p3
		
	def __str__(self):
		return 'OBJECT<TermNotifyInfo_t :%s> { type:%s,p1:%s,p2:%s,p3:%s}'%(hex(id(self)),str(self.type),str(self.p1),str(self.p2),str(self.p3) ) 
		
	def marshall(self):
		d =''
		d += struct.pack('!i',self.type)
		if type(self.p1)==type(0) or type(self.p1) == type(0.1): self.p1=str(self.p1)
		if not self.p1: self.p1=''
		try:
			self.p1 = self.p1.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.p1)))
		d += str(self.p1)
		if type(self.p2)==type(0) or type(self.p2) == type(0.1): self.p2=str(self.p2)
		if not self.p2: self.p2=''
		try:
			self.p2 = self.p2.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.p2)))
		d += str(self.p2)
		if type(self.p3)==type(0) or type(self.p3) == type(0.1): self.p3=str(self.p3)
		if not self.p3: self.p3=''
		try:
			self.p3 = self.p3.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.p3)))
		d += str(self.p3)
		return d
		
	def unmarshall(self,d,idx_=0):
		idx = idx_
		try:
			self.type, = struct.unpack('!i',d[idx:idx+4])
			idx+=4
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.p1 = d[idx:idx+size]
			idx+=size
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.p2 = d[idx:idx+size]
			idx+=size
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.p3 = d[idx:idx+size]
			idx+=size
		except:
			traceback.print_exc()
			return False,idx
		return True,idx
		

class ITerminal:
	# -- INTERFACE -- 
	def __init__(self):
		self.delegatecls = ITerminal_delegate
	
	def inviteReject(self,seq,invitee_id,ctx):
		pass
	
	def inviteAccept(self,seq,invitee_id,ctx):
		pass
	
	def inviteRequest(self,seq,inviter_id,greeting,ctx):
		pass
	
	def onGetLocation(self,src_id,loc,ctx):
		pass
	
	def onGetMessage(self,src_id,team_id,msg,seq,ctx):
		pass
	
	def onNotifyMessage(self,notify,ctx):
		pass
	
	def inviteTalking(self,from_id,talking,ctx):
		pass
	
	def inviteTalkingAccept(self,talking_id,from_id,ctx):
		pass
	
	def inviteTalkingReject(self,talking_id,from_id,reason,ctx):
		pass
	
	def exitTalking(self,talking_id,user_id,reason,ctx):
		pass
	
	def test(self,bytes,ctx):
		return [ ]

class ITerminal_delegate:
	def __init__(self,inst,adapter,conn=None):
		self.index = 0
		self.optlist={}
		self.id = '' 
		self.adapter = adapter
		self.optlist[0] = (self.inviteReject)
		self.optlist[1] = (self.inviteAccept)
		self.optlist[2] = (self.inviteRequest)
		self.optlist[3] = (self.onGetLocation)
		self.optlist[4] = (self.onGetMessage)
		self.optlist[5] = (self.onNotifyMessage)
		self.optlist[6] = (self.inviteTalking)
		self.optlist[7] = (self.inviteTalkingAccept)
		self.optlist[8] = (self.inviteTalkingReject)
		self.optlist[9] = (self.exitTalking)
		self.optlist[10] = (self.test)
		
		self.inst = inst
	
	def inviteReject(self,ctx):
		print "callin (inviteReject)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_seq = d[idx:idx+size]
		idx+=size
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_invitee_id = d[idx:idx+size]
		idx+=size
		cr = None
		self.inst.inviteReject(_p_seq,_p_invitee_id,ctx)
		return True
	
	def inviteAccept(self,ctx):
		print "callin (inviteAccept)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_seq = d[idx:idx+size]
		idx+=size
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_invitee_id = d[idx:idx+size]
		idx+=size
		cr = None
		self.inst.inviteAccept(_p_seq,_p_invitee_id,ctx)
		return True
	
	def inviteRequest(self,ctx):
		print "callin (inviteRequest)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_seq = d[idx:idx+size]
		idx+=size
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_inviter_id = d[idx:idx+size]
		idx+=size
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_greeting = d[idx:idx+size]
		idx+=size
		cr = None
		self.inst.inviteRequest(_p_seq,_p_inviter_id,_p_greeting,ctx)
		return True
	
	def onGetLocation(self,ctx):
		print "callin (onGetLocation)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_src_id = d[idx:idx+size]
		idx+=size
		_p_loc = LocationInfo_t()
		r,idx = _p_loc.unmarshall(d,idx)
		if not r: return False
		cr = None
		self.inst.onGetLocation(_p_src_id,_p_loc,ctx)
		return True
	
	def onGetMessage(self,ctx):
		print "callin (onGetMessage)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_src_id = d[idx:idx+size]
		idx+=size
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_team_id = d[idx:idx+size]
		idx+=size
		_p_msg = MimeMessage_t()
		r,idx = _p_msg.unmarshall(d,idx)
		if not r: return False
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_seq = d[idx:idx+size]
		idx+=size
		cr = None
		self.inst.onGetMessage(_p_src_id,_p_team_id,_p_msg,_p_seq,ctx)
		return True
	
	def onNotifyMessage(self,ctx):
		print "callin (onNotifyMessage)"
		d = ctx.msg.paramstream 
		idx = 0
		_p_notify = TermNotifyInfo_t()
		r,idx = _p_notify.unmarshall(d,idx)
		if not r: return False
		cr = None
		self.inst.onNotifyMessage(_p_notify,ctx)
		return True
	
	def inviteTalking(self,ctx):
		print "callin (inviteTalking)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_from_id = d[idx:idx+size]
		idx+=size
		_p_talking = TalkingResource_t()
		r,idx = _p_talking.unmarshall(d,idx)
		if not r: return False
		cr = None
		self.inst.inviteTalking(_p_from_id,_p_talking,ctx)
		return True
	
	def inviteTalkingAccept(self,ctx):
		print "callin (inviteTalkingAccept)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_talking_id = d[idx:idx+size]
		idx+=size
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_from_id = d[idx:idx+size]
		idx+=size
		cr = None
		self.inst.inviteTalkingAccept(_p_talking_id,_p_from_id,ctx)
		return True
	
	def inviteTalkingReject(self,ctx):
		print "callin (inviteTalkingReject)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_talking_id = d[idx:idx+size]
		idx+=size
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_from_id = d[idx:idx+size]
		idx+=size
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_reason = d[idx:idx+size]
		idx+=size
		cr = None
		self.inst.inviteTalkingReject(_p_talking_id,_p_from_id,_p_reason,ctx)
		return True
	
	def exitTalking(self,ctx):
		print "callin (exitTalking)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_talking_id = d[idx:idx+size]
		idx+=size
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_user_id = d[idx:idx+size]
		idx+=size
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_reason = d[idx:idx+size]
		idx+=size
		cr = None
		self.inst.exitTalking(_p_talking_id,_p_user_id,_p_reason,ctx)
		return True
	
	def test(self,ctx):
		print "callin (test)"
		d = ctx.msg.paramstream 
		idx = 0
		_p_bytes =[] 
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_bytes = d[idx:idx+size]
		idx+=size
		cr = None
		cr = self.inst.test(_p_bytes,ctx)
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
	
	
class ITerminalPrx:
	# -- INTERFACE PROXY -- 
	def __init__(self,conn):
		self.conn = conn
		self.delta = None
		pass
	
	@staticmethod
	def create(pdest,try_connect=False):
		conn = tce.RpcConnection(pdest=pdest)
		proxy = ITerminalPrx(conn)
		return proxy
	
	@staticmethod
	def createWithMQ(name):
		ep = tce.RpcMqSet.instance().server.findEndPointByName(name)
		if not ep: return None
		conn = ep.impl
		proxy = ITerminalPrx(conn)
		return proxy
	
	#extra must be map<string,string>
	def inviteReject(self,seq,invitee_id,timeout=0,extra={}):
		# function index: 49
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 0
		m.opidx = 0
		m.extra.setStrDict(extra)
		d = '' 
		if type(seq)==type(0) or type(seq) == type(0.1): seq=str(seq)
		if not seq: seq=''
		try:
			seq = seq.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(seq)))
		d += str(seq)
		m.paramstream+=d
		d = '' 
		if type(invitee_id)==type(0) or type(invitee_id) == type(0.1): invitee_id=str(invitee_id)
		if not invitee_id: invitee_id=''
		try:
			invitee_id = invitee_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(invitee_id)))
		d += str(invitee_id)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def inviteReject_oneway(self,seq,invitee_id,extra={}):
		# function index: 49
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 0
			m.opidx = 0
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcMqSet.instance().server.getId()
			m.extra.setStrDict(extra)
			d = '' 
			if type(seq)==type(0) or type(seq) == type(0.1): seq=str(seq)
			if not seq: seq=''
			try:
				seq = seq.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(seq)))
			d += str(seq)
			m.paramstream+=d
			d = '' 
			if type(invitee_id)==type(0) or type(invitee_id) == type(0.1): invitee_id=str(invitee_id)
			if not invitee_id: invitee_id=''
			try:
				invitee_id = invitee_id.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(invitee_id)))
			d += str(invitee_id)
			m.paramstream+=d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	#extra must be map<string,string>
	def inviteAccept(self,seq,invitee_id,timeout=0,extra={}):
		# function index: 49
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 0
		m.opidx = 1
		m.extra.setStrDict(extra)
		d = '' 
		if type(seq)==type(0) or type(seq) == type(0.1): seq=str(seq)
		if not seq: seq=''
		try:
			seq = seq.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(seq)))
		d += str(seq)
		m.paramstream+=d
		d = '' 
		if type(invitee_id)==type(0) or type(invitee_id) == type(0.1): invitee_id=str(invitee_id)
		if not invitee_id: invitee_id=''
		try:
			invitee_id = invitee_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(invitee_id)))
		d += str(invitee_id)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def inviteAccept_oneway(self,seq,invitee_id,extra={}):
		# function index: 49
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 0
			m.opidx = 1
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcMqSet.instance().server.getId()
			m.extra.setStrDict(extra)
			d = '' 
			if type(seq)==type(0) or type(seq) == type(0.1): seq=str(seq)
			if not seq: seq=''
			try:
				seq = seq.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(seq)))
			d += str(seq)
			m.paramstream+=d
			d = '' 
			if type(invitee_id)==type(0) or type(invitee_id) == type(0.1): invitee_id=str(invitee_id)
			if not invitee_id: invitee_id=''
			try:
				invitee_id = invitee_id.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(invitee_id)))
			d += str(invitee_id)
			m.paramstream+=d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	#extra must be map<string,string>
	def inviteRequest(self,seq,inviter_id,greeting,timeout=0,extra={}):
		# function index: 49
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 0
		m.opidx = 2
		m.extra.setStrDict(extra)
		d = '' 
		if type(seq)==type(0) or type(seq) == type(0.1): seq=str(seq)
		if not seq: seq=''
		try:
			seq = seq.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(seq)))
		d += str(seq)
		m.paramstream+=d
		d = '' 
		if type(inviter_id)==type(0) or type(inviter_id) == type(0.1): inviter_id=str(inviter_id)
		if not inviter_id: inviter_id=''
		try:
			inviter_id = inviter_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(inviter_id)))
		d += str(inviter_id)
		m.paramstream+=d
		d = '' 
		if type(greeting)==type(0) or type(greeting) == type(0.1): greeting=str(greeting)
		if not greeting: greeting=''
		try:
			greeting = greeting.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(greeting)))
		d += str(greeting)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def inviteRequest_oneway(self,seq,inviter_id,greeting,extra={}):
		# function index: 49
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 0
			m.opidx = 2
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcMqSet.instance().server.getId()
			m.extra.setStrDict(extra)
			d = '' 
			if type(seq)==type(0) or type(seq) == type(0.1): seq=str(seq)
			if not seq: seq=''
			try:
				seq = seq.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(seq)))
			d += str(seq)
			m.paramstream+=d
			d = '' 
			if type(inviter_id)==type(0) or type(inviter_id) == type(0.1): inviter_id=str(inviter_id)
			if not inviter_id: inviter_id=''
			try:
				inviter_id = inviter_id.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(inviter_id)))
			d += str(inviter_id)
			m.paramstream+=d
			d = '' 
			if type(greeting)==type(0) or type(greeting) == type(0.1): greeting=str(greeting)
			if not greeting: greeting=''
			try:
				greeting = greeting.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(greeting)))
			d += str(greeting)
			m.paramstream+=d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	#extra must be map<string,string>
	def onGetLocation(self,src_id,loc,timeout=0,extra={}):
		# function index: 49
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 0
		m.opidx = 3
		m.extra.setStrDict(extra)
		d = '' 
		if type(src_id)==type(0) or type(src_id) == type(0.1): src_id=str(src_id)
		if not src_id: src_id=''
		try:
			src_id = src_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(src_id)))
		d += str(src_id)
		m.paramstream+=d
		d = '' 
		d += loc.marshall()
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def onGetLocation_oneway(self,src_id,loc,extra={}):
		# function index: 49
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 0
			m.opidx = 3
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcMqSet.instance().server.getId()
			m.extra.setStrDict(extra)
			d = '' 
			if type(src_id)==type(0) or type(src_id) == type(0.1): src_id=str(src_id)
			if not src_id: src_id=''
			try:
				src_id = src_id.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(src_id)))
			d += str(src_id)
			m.paramstream+=d
			d = '' 
			d += loc.marshall()
			m.paramstream+=d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	#extra must be map<string,string>
	def onGetMessage(self,src_id,team_id,msg,seq,timeout=0,extra={}):
		# function index: 49
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 0
		m.opidx = 4
		m.extra.setStrDict(extra)
		d = '' 
		if type(src_id)==type(0) or type(src_id) == type(0.1): src_id=str(src_id)
		if not src_id: src_id=''
		try:
			src_id = src_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(src_id)))
		d += str(src_id)
		m.paramstream+=d
		d = '' 
		if type(team_id)==type(0) or type(team_id) == type(0.1): team_id=str(team_id)
		if not team_id: team_id=''
		try:
			team_id = team_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(team_id)))
		d += str(team_id)
		m.paramstream+=d
		d = '' 
		d += msg.marshall()
		m.paramstream+=d
		d = '' 
		if type(seq)==type(0) or type(seq) == type(0.1): seq=str(seq)
		if not seq: seq=''
		try:
			seq = seq.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(seq)))
		d += str(seq)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def onGetMessage_oneway(self,src_id,team_id,msg,seq,extra={}):
		# function index: 49
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 0
			m.opidx = 4
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcMqSet.instance().server.getId()
			m.extra.setStrDict(extra)
			d = '' 
			if type(src_id)==type(0) or type(src_id) == type(0.1): src_id=str(src_id)
			if not src_id: src_id=''
			try:
				src_id = src_id.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(src_id)))
			d += str(src_id)
			m.paramstream+=d
			d = '' 
			if type(team_id)==type(0) or type(team_id) == type(0.1): team_id=str(team_id)
			if not team_id: team_id=''
			try:
				team_id = team_id.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(team_id)))
			d += str(team_id)
			m.paramstream+=d
			d = '' 
			d += msg.marshall()
			m.paramstream+=d
			d = '' 
			if type(seq)==type(0) or type(seq) == type(0.1): seq=str(seq)
			if not seq: seq=''
			try:
				seq = seq.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(seq)))
			d += str(seq)
			m.paramstream+=d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	#extra must be map<string,string>
	def onNotifyMessage(self,notify,timeout=0,extra={}):
		# function index: 49
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 0
		m.opidx = 5
		m.extra.setStrDict(extra)
		d = '' 
		d += notify.marshall()
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def onNotifyMessage_oneway(self,notify,extra={}):
		# function index: 49
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 0
			m.opidx = 5
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcMqSet.instance().server.getId()
			m.extra.setStrDict(extra)
			d = '' 
			d += notify.marshall()
			m.paramstream+=d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	#extra must be map<string,string>
	def inviteTalking(self,from_id,talking,timeout=0,extra={}):
		# function index: 49
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 0
		m.opidx = 6
		m.extra.setStrDict(extra)
		d = '' 
		if type(from_id)==type(0) or type(from_id) == type(0.1): from_id=str(from_id)
		if not from_id: from_id=''
		try:
			from_id = from_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(from_id)))
		d += str(from_id)
		m.paramstream+=d
		d = '' 
		d += talking.marshall()
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def inviteTalking_oneway(self,from_id,talking,extra={}):
		# function index: 49
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 0
			m.opidx = 6
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcMqSet.instance().server.getId()
			m.extra.setStrDict(extra)
			d = '' 
			if type(from_id)==type(0) or type(from_id) == type(0.1): from_id=str(from_id)
			if not from_id: from_id=''
			try:
				from_id = from_id.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(from_id)))
			d += str(from_id)
			m.paramstream+=d
			d = '' 
			d += talking.marshall()
			m.paramstream+=d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	#extra must be map<string,string>
	def inviteTalkingAccept(self,talking_id,from_id,timeout=0,extra={}):
		# function index: 49
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 0
		m.opidx = 7
		m.extra.setStrDict(extra)
		d = '' 
		if type(talking_id)==type(0) or type(talking_id) == type(0.1): talking_id=str(talking_id)
		if not talking_id: talking_id=''
		try:
			talking_id = talking_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(talking_id)))
		d += str(talking_id)
		m.paramstream+=d
		d = '' 
		if type(from_id)==type(0) or type(from_id) == type(0.1): from_id=str(from_id)
		if not from_id: from_id=''
		try:
			from_id = from_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(from_id)))
		d += str(from_id)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def inviteTalkingAccept_oneway(self,talking_id,from_id,extra={}):
		# function index: 49
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 0
			m.opidx = 7
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcMqSet.instance().server.getId()
			m.extra.setStrDict(extra)
			d = '' 
			if type(talking_id)==type(0) or type(talking_id) == type(0.1): talking_id=str(talking_id)
			if not talking_id: talking_id=''
			try:
				talking_id = talking_id.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(talking_id)))
			d += str(talking_id)
			m.paramstream+=d
			d = '' 
			if type(from_id)==type(0) or type(from_id) == type(0.1): from_id=str(from_id)
			if not from_id: from_id=''
			try:
				from_id = from_id.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(from_id)))
			d += str(from_id)
			m.paramstream+=d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	#extra must be map<string,string>
	def inviteTalkingReject(self,talking_id,from_id,reason,timeout=0,extra={}):
		# function index: 49
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 0
		m.opidx = 8
		m.extra.setStrDict(extra)
		d = '' 
		if type(talking_id)==type(0) or type(talking_id) == type(0.1): talking_id=str(talking_id)
		if not talking_id: talking_id=''
		try:
			talking_id = talking_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(talking_id)))
		d += str(talking_id)
		m.paramstream+=d
		d = '' 
		if type(from_id)==type(0) or type(from_id) == type(0.1): from_id=str(from_id)
		if not from_id: from_id=''
		try:
			from_id = from_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(from_id)))
		d += str(from_id)
		m.paramstream+=d
		d = '' 
		if type(reason)==type(0) or type(reason) == type(0.1): reason=str(reason)
		if not reason: reason=''
		try:
			reason = reason.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(reason)))
		d += str(reason)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def inviteTalkingReject_oneway(self,talking_id,from_id,reason,extra={}):
		# function index: 49
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 0
			m.opidx = 8
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcMqSet.instance().server.getId()
			m.extra.setStrDict(extra)
			d = '' 
			if type(talking_id)==type(0) or type(talking_id) == type(0.1): talking_id=str(talking_id)
			if not talking_id: talking_id=''
			try:
				talking_id = talking_id.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(talking_id)))
			d += str(talking_id)
			m.paramstream+=d
			d = '' 
			if type(from_id)==type(0) or type(from_id) == type(0.1): from_id=str(from_id)
			if not from_id: from_id=''
			try:
				from_id = from_id.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(from_id)))
			d += str(from_id)
			m.paramstream+=d
			d = '' 
			if type(reason)==type(0) or type(reason) == type(0.1): reason=str(reason)
			if not reason: reason=''
			try:
				reason = reason.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(reason)))
			d += str(reason)
			m.paramstream+=d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	#extra must be map<string,string>
	def exitTalking(self,talking_id,user_id,reason,timeout=0,extra={}):
		# function index: 49
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 0
		m.opidx = 9
		m.extra.setStrDict(extra)
		d = '' 
		if type(talking_id)==type(0) or type(talking_id) == type(0.1): talking_id=str(talking_id)
		if not talking_id: talking_id=''
		try:
			talking_id = talking_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(talking_id)))
		d += str(talking_id)
		m.paramstream+=d
		d = '' 
		if type(user_id)==type(0) or type(user_id) == type(0.1): user_id=str(user_id)
		if not user_id: user_id=''
		try:
			user_id = user_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(user_id)))
		d += str(user_id)
		m.paramstream+=d
		d = '' 
		if type(reason)==type(0) or type(reason) == type(0.1): reason=str(reason)
		if not reason: reason=''
		try:
			reason = reason.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(reason)))
		d += str(reason)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def exitTalking_oneway(self,talking_id,user_id,reason,extra={}):
		# function index: 49
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 0
			m.opidx = 9
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcMqSet.instance().server.getId()
			m.extra.setStrDict(extra)
			d = '' 
			if type(talking_id)==type(0) or type(talking_id) == type(0.1): talking_id=str(talking_id)
			if not talking_id: talking_id=''
			try:
				talking_id = talking_id.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(talking_id)))
			d += str(talking_id)
			m.paramstream+=d
			d = '' 
			if type(user_id)==type(0) or type(user_id) == type(0.1): user_id=str(user_id)
			if not user_id: user_id=''
			try:
				user_id = user_id.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(user_id)))
			d += str(user_id)
			m.paramstream+=d
			d = '' 
			if type(reason)==type(0) or type(reason) == type(0.1): reason=str(reason)
			if not reason: reason=''
			try:
				reason = reason.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(reason)))
			d += str(reason)
			m.paramstream+=d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	#extra must be map<string,string>
	def test(self,bytes,timeout=0,extra={}):
		# function index: 49
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 0
		m.opidx = 10
		m.extra.setStrDict(extra)
		d = '' 
		if type(bytes)==type(0) or type(bytes) == type(0.1): bytes=str(bytes)
		if not bytes: bytes=''
		try:
			bytes = bytes.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(bytes)))
		d += str(bytes)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
		idx = 0
		d = m.paramstream
		p = None
		r = False
		try:
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			p = d[idx:idx+size]
			idx+=size
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_UNSERIALIZE_FAILED)
		return p
	
	def test_async(self,bytes,async,extra={}):
		# function index: 49
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 0
		m.opidx = 10
		m.extra.setStrDict(extra)
		d = '' 
		if type(bytes)==type(0) or type(bytes) == type(0.1): bytes=str(bytes)
		if not bytes: bytes=''
		try:
			bytes = bytes.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(bytes)))
		d += str(bytes)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		m.async = async
		m.asyncparser = ITerminalPrx.test_asyncparser
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def test_asyncparser(m,m2):
		# function index: 49 , m2 - callreturn msg.
		
		stream = m2.paramstream
		user = m.async
		prx = m.prx
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC: return 
		try:
			idx = 0
			d = stream
			r = True
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			p = d[idx:idx+size]
			idx+=size
			if r:
				user(p,prx)
		except:
			traceback.print_exc()
		
	

class IAuthService:
	# -- INTERFACE -- 
	def __init__(self):
		self.delegatecls = IAuthService_delegate
	
	def userLogin(self,user,passwd,loginType,ctx):
		return ''
	def strangerLogin(self,inv_link,loginType,ctx):
		return ''

class IAuthService_delegate:
	def __init__(self,inst,adapter,conn=None):
		self.index = 1
		self.optlist={}
		self.id = '' 
		self.adapter = adapter
		self.optlist[0] = (self.userLogin)
		self.optlist[1] = (self.strangerLogin)
		
		self.inst = inst
	
	def userLogin(self,ctx):
		print "callin (userLogin)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_user = d[idx:idx+size]
		idx+=size
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_passwd = d[idx:idx+size]
		idx+=size
		_p_loginType, = struct.unpack('!i',d[idx:idx+4])
		idx+=4
		cr = None
		cr = self.inst.userLogin(_p_user,_p_passwd,_p_loginType,ctx)
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
	
	def strangerLogin(self,ctx):
		print "callin (strangerLogin)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_inv_link = d[idx:idx+size]
		idx+=size
		_p_loginType, = struct.unpack('!i',d[idx:idx+4])
		idx+=4
		cr = None
		cr = self.inst.strangerLogin(_p_inv_link,_p_loginType,ctx)
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
	def create(pdest,try_connect=False):
		conn = tce.RpcConnection(pdest=pdest)
		proxy = IAuthServicePrx(conn)
		return proxy
	
	@staticmethod
	def createWithMQ(name):
		ep = tce.RpcMqSet.instance().server.findEndPointByName(name)
		if not ep: return None
		conn = ep.impl
		proxy = IAuthServicePrx(conn)
		return proxy
	
	#extra must be map<string,string>
	def userLogin(self,user,passwd,loginType,timeout=0,extra={}):
		# function index: 50
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 1
		m.opidx = 0
		m.extra.setStrDict(extra)
		d = '' 
		if type(user)==type(0) or type(user) == type(0.1): user=str(user)
		if not user: user=''
		try:
			user = user.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(user)))
		d += str(user)
		m.paramstream+=d
		d = '' 
		if type(passwd)==type(0) or type(passwd) == type(0.1): passwd=str(passwd)
		if not passwd: passwd=''
		try:
			passwd = passwd.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(passwd)))
		d += str(passwd)
		m.paramstream+=d
		d = '' 
		d += struct.pack('!i',loginType)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
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
	
	def userLogin_async(self,user,passwd,loginType,async,extra={}):
		# function index: 50
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 1
		m.opidx = 0
		m.extra.setStrDict(extra)
		d = '' 
		if type(user)==type(0) or type(user) == type(0.1): user=str(user)
		if not user: user=''
		try:
			user = user.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(user)))
		d += str(user)
		m.paramstream+=d
		d = '' 
		if type(passwd)==type(0) or type(passwd) == type(0.1): passwd=str(passwd)
		if not passwd: passwd=''
		try:
			passwd = passwd.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(passwd)))
		d += str(passwd)
		m.paramstream+=d
		d = '' 
		d += struct.pack('!i',loginType)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		m.async = async
		m.asyncparser = IAuthServicePrx.userLogin_asyncparser
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def userLogin_asyncparser(m,m2):
		# function index: 50 , m2 - callreturn msg.
		
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
	def strangerLogin(self,inv_link,loginType,timeout=0,extra={}):
		# function index: 50
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 1
		m.opidx = 1
		m.extra.setStrDict(extra)
		d = '' 
		if type(inv_link)==type(0) or type(inv_link) == type(0.1): inv_link=str(inv_link)
		if not inv_link: inv_link=''
		try:
			inv_link = inv_link.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(inv_link)))
		d += str(inv_link)
		m.paramstream+=d
		d = '' 
		d += struct.pack('!i',loginType)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
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
	
	def strangerLogin_async(self,inv_link,loginType,async,extra={}):
		# function index: 50
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 1
		m.opidx = 1
		m.extra.setStrDict(extra)
		d = '' 
		if type(inv_link)==type(0) or type(inv_link) == type(0.1): inv_link=str(inv_link)
		if not inv_link: inv_link=''
		try:
			inv_link = inv_link.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(inv_link)))
		d += str(inv_link)
		m.paramstream+=d
		d = '' 
		d += struct.pack('!i',loginType)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		m.async = async
		m.asyncparser = IAuthServicePrx.strangerLogin_asyncparser
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def strangerLogin_asyncparser(m,m2):
		# function index: 50 , m2 - callreturn msg.
		
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
		
	

class IGatewayAdapter:
	# -- INTERFACE -- 
	def __init__(self):
		self.delegatecls = IGatewayAdapter_delegate
	
	def login(self,token,ctx):
		return CallReturn_t()
	def logout(self,ctx):
		pass
	
	def heartbeat(self,ctx):
		return 0

class IGatewayAdapter_delegate:
	def __init__(self,inst,adapter,conn=None):
		self.index = 2
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
		_p_token = d[idx:idx+size]
		idx+=size
		cr = None
		cr = self.inst.login(_p_token,ctx)
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
	def create(pdest,try_connect=False):
		conn = tce.RpcConnection(pdest=pdest)
		proxy = IGatewayAdapterPrx(conn)
		return proxy
	
	@staticmethod
	def createWithMQ(name):
		ep = tce.RpcMqSet.instance().server.findEndPointByName(name)
		if not ep: return None
		conn = ep.impl
		proxy = IGatewayAdapterPrx(conn)
		return proxy
	
	#extra must be map<string,string>
	def login(self,token,timeout=0,extra={}):
		# function index: 51
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 2
		m.opidx = 0
		m.extra.setStrDict(extra)
		d = '' 
		if type(token)==type(0) or type(token) == type(0.1): token=str(token)
		if not token: token=''
		try:
			token = token.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(token)))
		d += str(token)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
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
	
	def login_async(self,token,async,extra={}):
		# function index: 51
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 2
		m.opidx = 0
		m.extra.setStrDict(extra)
		d = '' 
		if type(token)==type(0) or type(token) == type(0.1): token=str(token)
		if not token: token=''
		try:
			token = token.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(token)))
		d += str(token)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		m.async = async
		m.asyncparser = IGatewayAdapterPrx.login_asyncparser
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def login_asyncparser(m,m2):
		# function index: 51 , m2 - callreturn msg.
		
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
	def logout(self,timeout=0,extra={}):
		# function index: 51
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 2
		m.opidx = 1
		m.extra.setStrDict(extra)
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def logout_oneway(self,extra={}):
		# function index: 51
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 2
			m.opidx = 1
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcMqSet.instance().server.getId()
			m.extra.setStrDict(extra)
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	#extra must be map<string,string>
	def heartbeat(self,timeout=0,extra={}):
		# function index: 51
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 2
		m.opidx = 2
		m.extra.setStrDict(extra)
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
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
		# function index: 51
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 2
		m.opidx = 2
		m.extra.setStrDict(extra)
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		m.async = async
		m.asyncparser = IGatewayAdapterPrx.heartbeat_asyncparser
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def heartbeat_asyncparser(m,m2):
		# function index: 51 , m2 - callreturn msg.
		
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
		
	

class UserLocationSettings_t:
# -- STRUCT -- 
	def __init__(self,userid='',shared=False,type=0):
		self.userid = userid
		self.shared = shared
		self.type = type
		
	def __str__(self):
		return 'OBJECT<UserLocationSettings_t :%s> { userid:%s,shared:%s,type:%s}'%(hex(id(self)),str(self.userid),str(self.shared),str(self.type) ) 
		
	def marshall(self):
		d =''
		if type(self.userid)==type(0) or type(self.userid) == type(0.1): self.userid=str(self.userid)
		if not self.userid: self.userid=''
		try:
			self.userid = self.userid.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.userid)))
		d += str(self.userid)
		if self.shared == True:self.shared=1
		else: self.shared=0
		d += struct.pack('B',self.shared)
		d += struct.pack('!i',self.type)
		return d
		
	def unmarshall(self,d,idx_=0):
		idx = idx_
		try:
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.userid = d[idx:idx+size]
			idx+=size
			self.shared, = struct.unpack('B',d[idx:idx+1])
			if self.shared == 0: self.shared = False
			else: self.shared = True
			idx+=1
			self.type, = struct.unpack('!i',d[idx:idx+4])
			idx+=4
		except:
			traceback.print_exc()
			return False,idx
		return True,idx
		

class ILocationServer:
	# -- INTERFACE -- 
	def __init__(self):
		self.delegatecls = ILocationServer_delegate
	
	def searchNearestStrangers(self,p_,ctx):
		return [ ]
	def getLocations(self,user_ids,ctx):
		return [ ]
	def shareLocation(self,show,ctx):
		pass
	
	def getMySettings(self,ctx):
		return UserLocationSettings_t()
	def setUserType(self,type,ctx):
		return CallReturn_t()
	def g2m(self,pt,ctx):
		return GeoPoint_t()

class ILocationServer_delegate:
	def __init__(self,inst,adapter,conn=None):
		self.index = 3
		self.optlist={}
		self.id = '' 
		self.adapter = adapter
		self.optlist[0] = (self.searchNearestStrangers)
		self.optlist[1] = (self.getLocations)
		self.optlist[2] = (self.shareLocation)
		self.optlist[3] = (self.getMySettings)
		self.optlist[4] = (self.setUserType)
		self.optlist[5] = (self.g2m)
		
		self.inst = inst
	
	def searchNearestStrangers(self,ctx):
		print "callin (searchNearestStrangers)"
		d = ctx.msg.paramstream 
		idx = 0
		_p_p_ = StrangerSearchCase_t()
		r,idx = _p_p_.unmarshall(d,idx)
		if not r: return False
		cr = None
		cr = self.inst.searchNearestStrangers(_p_p_,ctx)
		if  cr == None: return True
		d = '' 
		m = tce.RpcMessageReturn()
		m.sequence = ctx.msg.sequence
		m.callmsg = ctx.msg
		m.ifidx = ctx.msg.ifidx
		m.call_id = ctx.msg.call_id
		m.conn = ctx.msg.conn
		m.extra = ctx.msg.extra
		container = StrangerInfoList_t(cr)
		d += container.marshall()
		if d: m.paramstream += d
		ctx.conn.sendMessage(m)
		return True
	
	def getLocations(self,ctx):
		print "callin (getLocations)"
		d = ctx.msg.paramstream 
		idx = 0
		_p_user_ids =[] 
		container = UserIdList_t(_p_user_ids)
		r,idx = container.unmarshall(d,idx)
		if not r: return False
		cr = None
		cr = self.inst.getLocations(_p_user_ids,ctx)
		if  cr == None: return True
		d = '' 
		m = tce.RpcMessageReturn()
		m.sequence = ctx.msg.sequence
		m.callmsg = ctx.msg
		m.ifidx = ctx.msg.ifidx
		m.call_id = ctx.msg.call_id
		m.conn = ctx.msg.conn
		m.extra = ctx.msg.extra
		container = LocationInfoList_t(cr)
		d += container.marshall()
		if d: m.paramstream += d
		ctx.conn.sendMessage(m)
		return True
	
	def shareLocation(self,ctx):
		print "callin (shareLocation)"
		d = ctx.msg.paramstream 
		idx = 0
		_p_show, = struct.unpack('B',d[idx:idx+1])
		if _p_show == 0: _p_show = False
		else: _p_show = True
		idx+=1
		cr = None
		self.inst.shareLocation(_p_show,ctx)
		return True
	
	def getMySettings(self,ctx):
		print "callin (getMySettings)"
		d = ctx.msg.paramstream 
		idx = 0
		cr = None
		cr = self.inst.getMySettings(ctx)
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
	
	def setUserType(self,ctx):
		print "callin (setUserType)"
		d = ctx.msg.paramstream 
		idx = 0
		_p_type, = struct.unpack('!i',d[idx:idx+4])
		idx+=4
		cr = None
		cr = self.inst.setUserType(_p_type,ctx)
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
	
	def g2m(self,ctx):
		print "callin (g2m)"
		d = ctx.msg.paramstream 
		idx = 0
		_p_pt = GeoPoint_t()
		r,idx = _p_pt.unmarshall(d,idx)
		if not r: return False
		cr = None
		cr = self.inst.g2m(_p_pt,ctx)
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
	
	
class ILocationServerPrx:
	# -- INTERFACE PROXY -- 
	def __init__(self,conn):
		self.conn = conn
		self.delta = None
		pass
	
	@staticmethod
	def create(pdest,try_connect=False):
		conn = tce.RpcConnection(pdest=pdest)
		proxy = ILocationServerPrx(conn)
		return proxy
	
	@staticmethod
	def createWithMQ(name):
		ep = tce.RpcMqSet.instance().server.findEndPointByName(name)
		if not ep: return None
		conn = ep.impl
		proxy = ILocationServerPrx(conn)
		return proxy
	
	#extra must be map<string,string>
	def searchNearestStrangers(self,p_,timeout=0,extra={}):
		# function index: 53
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 3
		m.opidx = 0
		m.extra.setStrDict(extra)
		d = '' 
		d += p_.marshall()
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
		idx = 0
		d = m.paramstream
		p = None
		r = False
		try:
			p =[]
			container = StrangerInfoList_t(p)
			r,idx = container.unmarshall(d,idx)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_UNSERIALIZE_FAILED)
		return p
	
	def searchNearestStrangers_async(self,p_,async,extra={}):
		# function index: 53
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 3
		m.opidx = 0
		m.extra.setStrDict(extra)
		d = '' 
		d += p_.marshall()
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		m.async = async
		m.asyncparser = ILocationServerPrx.searchNearestStrangers_asyncparser
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def searchNearestStrangers_asyncparser(m,m2):
		# function index: 53 , m2 - callreturn msg.
		
		stream = m2.paramstream
		user = m.async
		prx = m.prx
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC: return 
		try:
			idx = 0
			d = stream
			r = True
			p =[]
			container = StrangerInfoList_t(p)
			r,idx = container.unmarshall(d,idx)
			if r:
				user(p,prx)
		except:
			traceback.print_exc()
		
	
	#extra must be map<string,string>
	def getLocations(self,user_ids,timeout=0,extra={}):
		# function index: 53
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 3
		m.opidx = 1
		m.extra.setStrDict(extra)
		d = '' 
		container = UserIdList_t(user_ids)
		d += container.marshall()
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
		idx = 0
		d = m.paramstream
		p = None
		r = False
		try:
			p =[]
			container = LocationInfoList_t(p)
			r,idx = container.unmarshall(d,idx)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_UNSERIALIZE_FAILED)
		return p
	
	def getLocations_async(self,user_ids,async,extra={}):
		# function index: 53
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 3
		m.opidx = 1
		m.extra.setStrDict(extra)
		d = '' 
		container = UserIdList_t(user_ids)
		d += container.marshall()
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		m.async = async
		m.asyncparser = ILocationServerPrx.getLocations_asyncparser
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def getLocations_asyncparser(m,m2):
		# function index: 53 , m2 - callreturn msg.
		
		stream = m2.paramstream
		user = m.async
		prx = m.prx
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC: return 
		try:
			idx = 0
			d = stream
			r = True
			p =[]
			container = LocationInfoList_t(p)
			r,idx = container.unmarshall(d,idx)
			if r:
				user(p,prx)
		except:
			traceback.print_exc()
		
	
	#extra must be map<string,string>
	def shareLocation(self,show,timeout=0,extra={}):
		# function index: 53
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 3
		m.opidx = 2
		m.extra.setStrDict(extra)
		d = '' 
		if show == True:show=1
		else: show=0
		d += struct.pack('B',show)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def shareLocation_oneway(self,show,extra={}):
		# function index: 53
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 3
			m.opidx = 2
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcMqSet.instance().server.getId()
			m.extra.setStrDict(extra)
			d = '' 
			if show == True:show=1
			else: show=0
			d += struct.pack('B',show)
			m.paramstream+=d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	#extra must be map<string,string>
	def getMySettings(self,timeout=0,extra={}):
		# function index: 53
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 3
		m.opidx = 3
		m.extra.setStrDict(extra)
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
		idx = 0
		d = m.paramstream
		p = None
		r = False
		try:
			p = UserLocationSettings_t()
			r,idx = p.unmarshall(d,idx)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_UNSERIALIZE_FAILED)
		return p
	
	def getMySettings_async(self,async,extra={}):
		# function index: 53
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 3
		m.opidx = 3
		m.extra.setStrDict(extra)
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		m.async = async
		m.asyncparser = ILocationServerPrx.getMySettings_asyncparser
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def getMySettings_asyncparser(m,m2):
		# function index: 53 , m2 - callreturn msg.
		
		stream = m2.paramstream
		user = m.async
		prx = m.prx
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC: return 
		try:
			idx = 0
			d = stream
			r = True
			p = UserLocationSettings_t()
			r,idx = p.unmarshall(d,idx)
			if r:
				user(p,prx)
		except:
			traceback.print_exc()
		
	
	#extra must be map<string,string>
	def setUserType(self,type,timeout=0,extra={}):
		# function index: 53
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 3
		m.opidx = 4
		m.extra.setStrDict(extra)
		d = '' 
		d += struct.pack('!i',type)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
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
	
	def setUserType_async(self,type,async,extra={}):
		# function index: 53
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 3
		m.opidx = 4
		m.extra.setStrDict(extra)
		d = '' 
		d += struct.pack('!i',type)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		m.async = async
		m.asyncparser = ILocationServerPrx.setUserType_asyncparser
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def setUserType_asyncparser(m,m2):
		# function index: 53 , m2 - callreturn msg.
		
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
	def g2m(self,pt,timeout=0,extra={}):
		# function index: 53
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 3
		m.opidx = 5
		m.extra.setStrDict(extra)
		d = '' 
		d += pt.marshall()
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
		idx = 0
		d = m.paramstream
		p = None
		r = False
		try:
			p = GeoPoint_t()
			r,idx = p.unmarshall(d,idx)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_UNSERIALIZE_FAILED)
		return p
	
	def g2m_async(self,pt,async,extra={}):
		# function index: 53
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 3
		m.opidx = 5
		m.extra.setStrDict(extra)
		d = '' 
		d += pt.marshall()
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		m.async = async
		m.asyncparser = ILocationServerPrx.g2m_asyncparser
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def g2m_asyncparser(m,m2):
		# function index: 53 , m2 - callreturn msg.
		
		stream = m2.paramstream
		user = m.async
		prx = m.prx
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC: return 
		try:
			idx = 0
			d = stream
			r = True
			p = GeoPoint_t()
			r,idx = p.unmarshall(d,idx)
			if r:
				user(p,prx)
		except:
			traceback.print_exc()
		
	

class IMessagingService:
	# -- INTERFACE -- 
	def __init__(self):
		self.delegatecls = IMessagingService_delegate
	
	def sendMessage(self,targets,type,msg,ctx):
		pass
	
	def sendLocation(self,targets,type,loc,ctx):
		pass
	
	def sendMsgAck(self,seqs,ctx):
		pass
	
	def createTalking(self,type,ctx):
		return TalkingResource_t()
	def inviteTalking(self,target_id,talking,ctx):
		pass
	
	def inviteTalkingAccept(self,talking_id,ctx):
		pass
	
	def inviteTalkingReject(self,talking_id,reason,ctx):
		pass
	
	def initOnlineUserList(self,gwaid,useridlist,ctx):
		pass
	
	def uploadLocation(self,loc,ctx):
		pass
	

class IMessagingService_delegate:
	def __init__(self,inst,adapter,conn=None):
		self.index = 4
		self.optlist={}
		self.id = '' 
		self.adapter = adapter
		self.optlist[0] = (self.sendMessage)
		self.optlist[1] = (self.sendLocation)
		self.optlist[2] = (self.sendMsgAck)
		self.optlist[3] = (self.createTalking)
		self.optlist[4] = (self.inviteTalking)
		self.optlist[5] = (self.inviteTalkingAccept)
		self.optlist[6] = (self.inviteTalkingReject)
		self.optlist[7] = (self.initOnlineUserList)
		self.optlist[8] = (self.uploadLocation)
		
		self.inst = inst
	
	def sendMessage(self,ctx):
		print "callin (sendMessage)"
		d = ctx.msg.paramstream 
		idx = 0
		_p_targets =[] 
		container = SIDS_t(_p_targets)
		r,idx = container.unmarshall(d,idx)
		if not r: return False
		_p_type, = struct.unpack('!i',d[idx:idx+4])
		idx+=4
		_p_msg = MimeMessage_t()
		r,idx = _p_msg.unmarshall(d,idx)
		if not r: return False
		cr = None
		self.inst.sendMessage(_p_targets,_p_type,_p_msg,ctx)
		return True
	
	def sendLocation(self,ctx):
		print "callin (sendLocation)"
		d = ctx.msg.paramstream 
		idx = 0
		_p_targets =[] 
		container = SIDS_t(_p_targets)
		r,idx = container.unmarshall(d,idx)
		if not r: return False
		_p_type, = struct.unpack('!i',d[idx:idx+4])
		idx+=4
		_p_loc = LocationInfo_t()
		r,idx = _p_loc.unmarshall(d,idx)
		if not r: return False
		cr = None
		self.inst.sendLocation(_p_targets,_p_type,_p_loc,ctx)
		return True
	
	def sendMsgAck(self,ctx):
		print "callin (sendMsgAck)"
		d = ctx.msg.paramstream 
		idx = 0
		_p_seqs =[] 
		container = StringList_t(_p_seqs)
		r,idx = container.unmarshall(d,idx)
		if not r: return False
		cr = None
		self.inst.sendMsgAck(_p_seqs,ctx)
		return True
	
	def createTalking(self,ctx):
		print "callin (createTalking)"
		d = ctx.msg.paramstream 
		idx = 0
		_p_type, = struct.unpack('!i',d[idx:idx+4])
		idx+=4
		cr = None
		cr = self.inst.createTalking(_p_type,ctx)
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
	
	def inviteTalking(self,ctx):
		print "callin (inviteTalking)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_target_id = d[idx:idx+size]
		idx+=size
		_p_talking = TalkingResource_t()
		r,idx = _p_talking.unmarshall(d,idx)
		if not r: return False
		cr = None
		self.inst.inviteTalking(_p_target_id,_p_talking,ctx)
		return True
	
	def inviteTalkingAccept(self,ctx):
		print "callin (inviteTalkingAccept)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_talking_id = d[idx:idx+size]
		idx+=size
		cr = None
		self.inst.inviteTalkingAccept(_p_talking_id,ctx)
		return True
	
	def inviteTalkingReject(self,ctx):
		print "callin (inviteTalkingReject)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_talking_id = d[idx:idx+size]
		idx+=size
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_reason = d[idx:idx+size]
		idx+=size
		cr = None
		self.inst.inviteTalkingReject(_p_talking_id,_p_reason,ctx)
		return True
	
	def initOnlineUserList(self,ctx):
		print "callin (initOnlineUserList)"
		d = ctx.msg.paramstream 
		idx = 0
		_p_gwaid, = struct.unpack('!i',d[idx:idx+4])
		idx+=4
		_p_useridlist =[] 
		container = SIDS_t(_p_useridlist)
		r,idx = container.unmarshall(d,idx)
		if not r: return False
		cr = None
		self.inst.initOnlineUserList(_p_gwaid,_p_useridlist,ctx)
		return True
	
	def uploadLocation(self,ctx):
		print "callin (uploadLocation)"
		d = ctx.msg.paramstream 
		idx = 0
		_p_loc = LocationInfo_t()
		r,idx = _p_loc.unmarshall(d,idx)
		if not r: return False
		cr = None
		self.inst.uploadLocation(_p_loc,ctx)
		return True
	
	
class IMessagingServicePrx:
	# -- INTERFACE PROXY -- 
	def __init__(self,conn):
		self.conn = conn
		self.delta = None
		pass
	
	@staticmethod
	def create(pdest,try_connect=False):
		conn = tce.RpcConnection(pdest=pdest)
		proxy = IMessagingServicePrx(conn)
		return proxy
	
	@staticmethod
	def createWithMQ(name):
		ep = tce.RpcMqSet.instance().server.findEndPointByName(name)
		if not ep: return None
		conn = ep.impl
		proxy = IMessagingServicePrx(conn)
		return proxy
	
	#extra must be map<string,string>
	def sendMessage(self,targets,type,msg,timeout=0,extra={}):
		# function index: 54
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 4
		m.opidx = 0
		m.extra.setStrDict(extra)
		d = '' 
		container = SIDS_t(targets)
		d += container.marshall()
		m.paramstream+=d
		d = '' 
		d += struct.pack('!i',type)
		m.paramstream+=d
		d = '' 
		d += msg.marshall()
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def sendMessage_oneway(self,targets,type,msg,extra={}):
		# function index: 54
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 4
			m.opidx = 0
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcMqSet.instance().server.getId()
			m.extra.setStrDict(extra)
			d = '' 
			container = SIDS_t(targets)
			d += container.marshall()
			m.paramstream+=d
			d = '' 
			d += struct.pack('!i',type)
			m.paramstream+=d
			d = '' 
			d += msg.marshall()
			m.paramstream+=d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	#extra must be map<string,string>
	def sendLocation(self,targets,type,loc,timeout=0,extra={}):
		# function index: 54
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 4
		m.opidx = 1
		m.extra.setStrDict(extra)
		d = '' 
		container = SIDS_t(targets)
		d += container.marshall()
		m.paramstream+=d
		d = '' 
		d += struct.pack('!i',type)
		m.paramstream+=d
		d = '' 
		d += loc.marshall()
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def sendLocation_oneway(self,targets,type,loc,extra={}):
		# function index: 54
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 4
			m.opidx = 1
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcMqSet.instance().server.getId()
			m.extra.setStrDict(extra)
			d = '' 
			container = SIDS_t(targets)
			d += container.marshall()
			m.paramstream+=d
			d = '' 
			d += struct.pack('!i',type)
			m.paramstream+=d
			d = '' 
			d += loc.marshall()
			m.paramstream+=d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	#extra must be map<string,string>
	def sendMsgAck(self,seqs,timeout=0,extra={}):
		# function index: 54
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 4
		m.opidx = 2
		m.extra.setStrDict(extra)
		d = '' 
		container = StringList_t(seqs)
		d += container.marshall()
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def sendMsgAck_oneway(self,seqs,extra={}):
		# function index: 54
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 4
			m.opidx = 2
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcMqSet.instance().server.getId()
			m.extra.setStrDict(extra)
			d = '' 
			container = StringList_t(seqs)
			d += container.marshall()
			m.paramstream+=d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	#extra must be map<string,string>
	def createTalking(self,type,timeout=0,extra={}):
		# function index: 54
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 4
		m.opidx = 3
		m.extra.setStrDict(extra)
		d = '' 
		d += struct.pack('!i',type)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
		idx = 0
		d = m.paramstream
		p = None
		r = False
		try:
			p = TalkingResource_t()
			r,idx = p.unmarshall(d,idx)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_UNSERIALIZE_FAILED)
		return p
	
	def createTalking_async(self,type,async,extra={}):
		# function index: 54
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 4
		m.opidx = 3
		m.extra.setStrDict(extra)
		d = '' 
		d += struct.pack('!i',type)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		m.async = async
		m.asyncparser = IMessagingServicePrx.createTalking_asyncparser
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def createTalking_asyncparser(m,m2):
		# function index: 54 , m2 - callreturn msg.
		
		stream = m2.paramstream
		user = m.async
		prx = m.prx
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC: return 
		try:
			idx = 0
			d = stream
			r = True
			p = TalkingResource_t()
			r,idx = p.unmarshall(d,idx)
			if r:
				user(p,prx)
		except:
			traceback.print_exc()
		
	
	#extra must be map<string,string>
	def inviteTalking(self,target_id,talking,timeout=0,extra={}):
		# function index: 54
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 4
		m.opidx = 4
		m.extra.setStrDict(extra)
		d = '' 
		if type(target_id)==type(0) or type(target_id) == type(0.1): target_id=str(target_id)
		if not target_id: target_id=''
		try:
			target_id = target_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(target_id)))
		d += str(target_id)
		m.paramstream+=d
		d = '' 
		d += talking.marshall()
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def inviteTalking_oneway(self,target_id,talking,extra={}):
		# function index: 54
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 4
			m.opidx = 4
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcMqSet.instance().server.getId()
			m.extra.setStrDict(extra)
			d = '' 
			if type(target_id)==type(0) or type(target_id) == type(0.1): target_id=str(target_id)
			if not target_id: target_id=''
			try:
				target_id = target_id.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(target_id)))
			d += str(target_id)
			m.paramstream+=d
			d = '' 
			d += talking.marshall()
			m.paramstream+=d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	#extra must be map<string,string>
	def inviteTalkingAccept(self,talking_id,timeout=0,extra={}):
		# function index: 54
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 4
		m.opidx = 5
		m.extra.setStrDict(extra)
		d = '' 
		if type(talking_id)==type(0) or type(talking_id) == type(0.1): talking_id=str(talking_id)
		if not talking_id: talking_id=''
		try:
			talking_id = talking_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(talking_id)))
		d += str(talking_id)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def inviteTalkingAccept_oneway(self,talking_id,extra={}):
		# function index: 54
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 4
			m.opidx = 5
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcMqSet.instance().server.getId()
			m.extra.setStrDict(extra)
			d = '' 
			if type(talking_id)==type(0) or type(talking_id) == type(0.1): talking_id=str(talking_id)
			if not talking_id: talking_id=''
			try:
				talking_id = talking_id.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(talking_id)))
			d += str(talking_id)
			m.paramstream+=d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	#extra must be map<string,string>
	def inviteTalkingReject(self,talking_id,reason,timeout=0,extra={}):
		# function index: 54
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 4
		m.opidx = 6
		m.extra.setStrDict(extra)
		d = '' 
		if type(talking_id)==type(0) or type(talking_id) == type(0.1): talking_id=str(talking_id)
		if not talking_id: talking_id=''
		try:
			talking_id = talking_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(talking_id)))
		d += str(talking_id)
		m.paramstream+=d
		d = '' 
		if type(reason)==type(0) or type(reason) == type(0.1): reason=str(reason)
		if not reason: reason=''
		try:
			reason = reason.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(reason)))
		d += str(reason)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def inviteTalkingReject_oneway(self,talking_id,reason,extra={}):
		# function index: 54
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 4
			m.opidx = 6
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcMqSet.instance().server.getId()
			m.extra.setStrDict(extra)
			d = '' 
			if type(talking_id)==type(0) or type(talking_id) == type(0.1): talking_id=str(talking_id)
			if not talking_id: talking_id=''
			try:
				talking_id = talking_id.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(talking_id)))
			d += str(talking_id)
			m.paramstream+=d
			d = '' 
			if type(reason)==type(0) or type(reason) == type(0.1): reason=str(reason)
			if not reason: reason=''
			try:
				reason = reason.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(reason)))
			d += str(reason)
			m.paramstream+=d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	#extra must be map<string,string>
	def initOnlineUserList(self,gwaid,useridlist,timeout=0,extra={}):
		# function index: 54
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 4
		m.opidx = 7
		m.extra.setStrDict(extra)
		d = '' 
		d += struct.pack('!i',gwaid)
		m.paramstream+=d
		d = '' 
		container = SIDS_t(useridlist)
		d += container.marshall()
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def initOnlineUserList_oneway(self,gwaid,useridlist,extra={}):
		# function index: 54
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 4
			m.opidx = 7
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcMqSet.instance().server.getId()
			m.extra.setStrDict(extra)
			d = '' 
			d += struct.pack('!i',gwaid)
			m.paramstream+=d
			d = '' 
			container = SIDS_t(useridlist)
			d += container.marshall()
			m.paramstream+=d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	#extra must be map<string,string>
	def uploadLocation(self,loc,timeout=0,extra={}):
		# function index: 54
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 4
		m.opidx = 8
		m.extra.setStrDict(extra)
		d = '' 
		d += loc.marshall()
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def uploadLocation_oneway(self,loc,extra={}):
		# function index: 54
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 4
			m.opidx = 8
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcMqSet.instance().server.getId()
			m.extra.setStrDict(extra)
			d = '' 
			d += loc.marshall()
			m.paramstream+=d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	

class ILocationReciever:
	# -- INTERFACE -- 
	def __init__(self):
		self.delegatecls = ILocationReciever_delegate
	
	def updateLocation(self,userid,gps,ctx):
		pass
	

class ILocationReciever_delegate:
	def __init__(self,inst,adapter,conn=None):
		self.index = 5
		self.optlist={}
		self.id = '' 
		self.adapter = adapter
		self.optlist[0] = (self.updateLocation)
		
		self.inst = inst
	
	def updateLocation(self,ctx):
		print "callin (updateLocation)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_userid = d[idx:idx+size]
		idx+=size
		_p_gps = GpsInfo_t()
		r,idx = _p_gps.unmarshall(d,idx)
		if not r: return False
		cr = None
		self.inst.updateLocation(_p_userid,_p_gps,ctx)
		return True
	
	
class ILocationRecieverPrx:
	# -- INTERFACE PROXY -- 
	def __init__(self,conn):
		self.conn = conn
		self.delta = None
		pass
	
	@staticmethod
	def create(pdest,try_connect=False):
		conn = tce.RpcConnection(pdest=pdest)
		proxy = ILocationRecieverPrx(conn)
		return proxy
	
	@staticmethod
	def createWithMQ(name):
		ep = tce.RpcMqSet.instance().server.findEndPointByName(name)
		if not ep: return None
		conn = ep.impl
		proxy = ILocationRecieverPrx(conn)
		return proxy
	
	#extra must be map<string,string>
	def updateLocation(self,userid,gps,timeout=0,extra={}):
		# function index: 55
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 5
		m.opidx = 0
		m.extra.setStrDict(extra)
		d = '' 
		if type(userid)==type(0) or type(userid) == type(0.1): userid=str(userid)
		if not userid: userid=''
		try:
			userid = userid.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(userid)))
		d += str(userid)
		m.paramstream+=d
		d = '' 
		d += gps.marshall()
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def updateLocation_oneway(self,userid,gps,extra={}):
		# function index: 55
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 5
			m.opidx = 0
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcMqSet.instance().server.getId()
			m.extra.setStrDict(extra)
			d = '' 
			if type(userid)==type(0) or type(userid) == type(0.1): userid=str(userid)
			if not userid: userid=''
			try:
				userid = userid.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(userid)))
			d += str(userid)
			m.paramstream+=d
			d = '' 
			d += gps.marshall()
			m.paramstream+=d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	

class IUserService:
	# -- INTERFACE -- 
	def __init__(self):
		self.delegatecls = IUserService_delegate
	
	def getFriendGroups(self,ctx):
		return [ ]
	def getFriendsInGroup(self,group_id,ctx):
		return [ ]
	def getAllFriends(self,ctx):
		return [ ]
	def getUserDetail(self,user_id,ctx):
		return UserInfoDetail_t()
	def renameFriendName(self,user_id,nickname,ctx):
		return CallReturn_t()
	def getUserInfoList(self,userids,ctx):
		return [ ]
	def updateUserInfo(self,userinfo,ctx):
		return CallReturn_t()
	def changeUserPasswd(self,oldpasswd,newpasswd,ctx):
		return CallReturn_t()
	def getUserInfo(self,ctx):
		return UserInfo_t()
	def getInvitorOfStranger(self,ctx):
		return UserInfo_t()
	def createGroup(self,group,ctx):
		return CallReturn_t()
	def deleteGroup(self,group_id,ctx):
		return CallReturn_t()
	def addGroupUser(self,group_id,user_id,ctx):
		return CallReturn_t()
	def removeGroupUser(self,group_id,user_id,ctx):
		return CallReturn_t()
	def removeFriend(self,user_id,ctx):
		return CallReturn_t()
	def getTeams(self,ctx):
		return [ ]
	def getUsersInTeam(self,team_id,ctx):
		return [ ]
	def addTeamUser(self,team_id,user_id,ctx):
		return CallReturn_t()
	def removeTeamUser(self,team_id,user_id,ctx):
		return CallReturn_t()
	def exitTeam(self,team_id,ctx):
		return CallReturn_t()
	def createTeam(self,team,ctx):
		return CallReturn_t()
	def deleteTeam(self,team_id,ctx):
		return CallReturn_t()
	def updateTeamInfo(self,team,ctx):
		return CallReturn_t()
	def inviteFriend(self,stranger_id,msg,ctx):
		return CallReturn_t()
	def inviteFriendReject(self,seq,reason,ctx):
		pass
	
	def inviteFriendAccept(self,seq,ctx):
		pass
	
	def getMessageLogList(self,target_id,type,timerange,ctx):
		return QueryMessageLogResult_t()
	def setUserStatus(self,type,ctx):
		pass
	
	def getUserStatus(self,ctx):
		return CallReturn_t()
	def getUserStatusList(self,userids,ctx):
		return [ ]
	def inviteStranger(self,target,type,msg,ctx):
		return CallReturn_t()

class IUserService_delegate:
	def __init__(self,inst,adapter,conn=None):
		self.index = 6
		self.optlist={}
		self.id = '' 
		self.adapter = adapter
		self.optlist[0] = (self.getFriendGroups)
		self.optlist[1] = (self.getFriendsInGroup)
		self.optlist[2] = (self.getAllFriends)
		self.optlist[3] = (self.getUserDetail)
		self.optlist[4] = (self.renameFriendName)
		self.optlist[5] = (self.getUserInfoList)
		self.optlist[6] = (self.updateUserInfo)
		self.optlist[7] = (self.changeUserPasswd)
		self.optlist[8] = (self.getUserInfo)
		self.optlist[9] = (self.getInvitorOfStranger)
		self.optlist[10] = (self.createGroup)
		self.optlist[11] = (self.deleteGroup)
		self.optlist[12] = (self.addGroupUser)
		self.optlist[13] = (self.removeGroupUser)
		self.optlist[14] = (self.removeFriend)
		self.optlist[15] = (self.getTeams)
		self.optlist[16] = (self.getUsersInTeam)
		self.optlist[17] = (self.addTeamUser)
		self.optlist[18] = (self.removeTeamUser)
		self.optlist[19] = (self.exitTeam)
		self.optlist[20] = (self.createTeam)
		self.optlist[21] = (self.deleteTeam)
		self.optlist[22] = (self.updateTeamInfo)
		self.optlist[23] = (self.inviteFriend)
		self.optlist[24] = (self.inviteFriendReject)
		self.optlist[25] = (self.inviteFriendAccept)
		self.optlist[26] = (self.getMessageLogList)
		self.optlist[27] = (self.setUserStatus)
		self.optlist[28] = (self.getUserStatus)
		self.optlist[29] = (self.getUserStatusList)
		self.optlist[30] = (self.inviteStranger)
		
		self.inst = inst
	
	def getFriendGroups(self,ctx):
		print "callin (getFriendGroups)"
		d = ctx.msg.paramstream 
		idx = 0
		cr = None
		cr = self.inst.getFriendGroups(ctx)
		if  cr == None: return True
		d = '' 
		m = tce.RpcMessageReturn()
		m.sequence = ctx.msg.sequence
		m.callmsg = ctx.msg
		m.ifidx = ctx.msg.ifidx
		m.call_id = ctx.msg.call_id
		m.conn = ctx.msg.conn
		m.extra = ctx.msg.extra
		container = UserGroupInfoList_t(cr)
		d += container.marshall()
		if d: m.paramstream += d
		ctx.conn.sendMessage(m)
		return True
	
	def getFriendsInGroup(self,ctx):
		print "callin (getFriendsInGroup)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_group_id = d[idx:idx+size]
		idx+=size
		cr = None
		cr = self.inst.getFriendsInGroup(_p_group_id,ctx)
		if  cr == None: return True
		d = '' 
		m = tce.RpcMessageReturn()
		m.sequence = ctx.msg.sequence
		m.callmsg = ctx.msg
		m.ifidx = ctx.msg.ifidx
		m.call_id = ctx.msg.call_id
		m.conn = ctx.msg.conn
		m.extra = ctx.msg.extra
		container = UserInfoList_t(cr)
		d += container.marshall()
		if d: m.paramstream += d
		ctx.conn.sendMessage(m)
		return True
	
	def getAllFriends(self,ctx):
		print "callin (getAllFriends)"
		d = ctx.msg.paramstream 
		idx = 0
		cr = None
		cr = self.inst.getAllFriends(ctx)
		if  cr == None: return True
		d = '' 
		m = tce.RpcMessageReturn()
		m.sequence = ctx.msg.sequence
		m.callmsg = ctx.msg
		m.ifidx = ctx.msg.ifidx
		m.call_id = ctx.msg.call_id
		m.conn = ctx.msg.conn
		m.extra = ctx.msg.extra
		container = UserInfoList_t(cr)
		d += container.marshall()
		if d: m.paramstream += d
		ctx.conn.sendMessage(m)
		return True
	
	def getUserDetail(self,ctx):
		print "callin (getUserDetail)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_user_id = d[idx:idx+size]
		idx+=size
		cr = None
		cr = self.inst.getUserDetail(_p_user_id,ctx)
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
	
	def renameFriendName(self,ctx):
		print "callin (renameFriendName)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_user_id = d[idx:idx+size]
		idx+=size
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_nickname = d[idx:idx+size]
		idx+=size
		cr = None
		cr = self.inst.renameFriendName(_p_user_id,_p_nickname,ctx)
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
	
	def getUserInfoList(self,ctx):
		print "callin (getUserInfoList)"
		d = ctx.msg.paramstream 
		idx = 0
		_p_userids =[] 
		container = UserIdList_t(_p_userids)
		r,idx = container.unmarshall(d,idx)
		if not r: return False
		cr = None
		cr = self.inst.getUserInfoList(_p_userids,ctx)
		if  cr == None: return True
		d = '' 
		m = tce.RpcMessageReturn()
		m.sequence = ctx.msg.sequence
		m.callmsg = ctx.msg
		m.ifidx = ctx.msg.ifidx
		m.call_id = ctx.msg.call_id
		m.conn = ctx.msg.conn
		m.extra = ctx.msg.extra
		container = UserInfoList_t(cr)
		d += container.marshall()
		if d: m.paramstream += d
		ctx.conn.sendMessage(m)
		return True
	
	def updateUserInfo(self,ctx):
		print "callin (updateUserInfo)"
		d = ctx.msg.paramstream 
		idx = 0
		_p_userinfo = UserInfo_t()
		r,idx = _p_userinfo.unmarshall(d,idx)
		if not r: return False
		cr = None
		cr = self.inst.updateUserInfo(_p_userinfo,ctx)
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
	
	def changeUserPasswd(self,ctx):
		print "callin (changeUserPasswd)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_oldpasswd = d[idx:idx+size]
		idx+=size
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_newpasswd = d[idx:idx+size]
		idx+=size
		cr = None
		cr = self.inst.changeUserPasswd(_p_oldpasswd,_p_newpasswd,ctx)
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
	
	def getUserInfo(self,ctx):
		print "callin (getUserInfo)"
		d = ctx.msg.paramstream 
		idx = 0
		cr = None
		cr = self.inst.getUserInfo(ctx)
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
	
	def getInvitorOfStranger(self,ctx):
		print "callin (getInvitorOfStranger)"
		d = ctx.msg.paramstream 
		idx = 0
		cr = None
		cr = self.inst.getInvitorOfStranger(ctx)
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
	
	def createGroup(self,ctx):
		print "callin (createGroup)"
		d = ctx.msg.paramstream 
		idx = 0
		_p_group = UserGroupInfo_t()
		r,idx = _p_group.unmarshall(d,idx)
		if not r: return False
		cr = None
		cr = self.inst.createGroup(_p_group,ctx)
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
	
	def deleteGroup(self,ctx):
		print "callin (deleteGroup)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_group_id = d[idx:idx+size]
		idx+=size
		cr = None
		cr = self.inst.deleteGroup(_p_group_id,ctx)
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
	
	def addGroupUser(self,ctx):
		print "callin (addGroupUser)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_group_id = d[idx:idx+size]
		idx+=size
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_user_id = d[idx:idx+size]
		idx+=size
		cr = None
		cr = self.inst.addGroupUser(_p_group_id,_p_user_id,ctx)
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
	
	def removeGroupUser(self,ctx):
		print "callin (removeGroupUser)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_group_id = d[idx:idx+size]
		idx+=size
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_user_id = d[idx:idx+size]
		idx+=size
		cr = None
		cr = self.inst.removeGroupUser(_p_group_id,_p_user_id,ctx)
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
	
	def removeFriend(self,ctx):
		print "callin (removeFriend)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_user_id = d[idx:idx+size]
		idx+=size
		cr = None
		cr = self.inst.removeFriend(_p_user_id,ctx)
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
	
	def getTeams(self,ctx):
		print "callin (getTeams)"
		d = ctx.msg.paramstream 
		idx = 0
		cr = None
		cr = self.inst.getTeams(ctx)
		if  cr == None: return True
		d = '' 
		m = tce.RpcMessageReturn()
		m.sequence = ctx.msg.sequence
		m.callmsg = ctx.msg
		m.ifidx = ctx.msg.ifidx
		m.call_id = ctx.msg.call_id
		m.conn = ctx.msg.conn
		m.extra = ctx.msg.extra
		container = TeamInfoList_t(cr)
		d += container.marshall()
		if d: m.paramstream += d
		ctx.conn.sendMessage(m)
		return True
	
	def getUsersInTeam(self,ctx):
		print "callin (getUsersInTeam)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_team_id = d[idx:idx+size]
		idx+=size
		cr = None
		cr = self.inst.getUsersInTeam(_p_team_id,ctx)
		if  cr == None: return True
		d = '' 
		m = tce.RpcMessageReturn()
		m.sequence = ctx.msg.sequence
		m.callmsg = ctx.msg
		m.ifidx = ctx.msg.ifidx
		m.call_id = ctx.msg.call_id
		m.conn = ctx.msg.conn
		m.extra = ctx.msg.extra
		container = UserInfoList_t(cr)
		d += container.marshall()
		if d: m.paramstream += d
		ctx.conn.sendMessage(m)
		return True
	
	def addTeamUser(self,ctx):
		print "callin (addTeamUser)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_team_id = d[idx:idx+size]
		idx+=size
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_user_id = d[idx:idx+size]
		idx+=size
		cr = None
		cr = self.inst.addTeamUser(_p_team_id,_p_user_id,ctx)
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
	
	def removeTeamUser(self,ctx):
		print "callin (removeTeamUser)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_team_id = d[idx:idx+size]
		idx+=size
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_user_id = d[idx:idx+size]
		idx+=size
		cr = None
		cr = self.inst.removeTeamUser(_p_team_id,_p_user_id,ctx)
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
	
	def exitTeam(self,ctx):
		print "callin (exitTeam)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_team_id = d[idx:idx+size]
		idx+=size
		cr = None
		cr = self.inst.exitTeam(_p_team_id,ctx)
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
	
	def createTeam(self,ctx):
		print "callin (createTeam)"
		d = ctx.msg.paramstream 
		idx = 0
		_p_team = TeamInfo_t()
		r,idx = _p_team.unmarshall(d,idx)
		if not r: return False
		cr = None
		cr = self.inst.createTeam(_p_team,ctx)
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
	
	def deleteTeam(self,ctx):
		print "callin (deleteTeam)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_team_id = d[idx:idx+size]
		idx+=size
		cr = None
		cr = self.inst.deleteTeam(_p_team_id,ctx)
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
	
	def updateTeamInfo(self,ctx):
		print "callin (updateTeamInfo)"
		d = ctx.msg.paramstream 
		idx = 0
		_p_team = TeamInfo_t()
		r,idx = _p_team.unmarshall(d,idx)
		if not r: return False
		cr = None
		cr = self.inst.updateTeamInfo(_p_team,ctx)
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
	
	def inviteFriend(self,ctx):
		print "callin (inviteFriend)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_stranger_id = d[idx:idx+size]
		idx+=size
		_p_msg = MimeText_t()
		r,idx = _p_msg.unmarshall(d,idx)
		if not r: return False
		cr = None
		cr = self.inst.inviteFriend(_p_stranger_id,_p_msg,ctx)
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
	
	def inviteFriendReject(self,ctx):
		print "callin (inviteFriendReject)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_seq = d[idx:idx+size]
		idx+=size
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_reason = d[idx:idx+size]
		idx+=size
		cr = None
		self.inst.inviteFriendReject(_p_seq,_p_reason,ctx)
		return True
	
	def inviteFriendAccept(self,ctx):
		print "callin (inviteFriendAccept)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_seq = d[idx:idx+size]
		idx+=size
		cr = None
		self.inst.inviteFriendAccept(_p_seq,ctx)
		return True
	
	def getMessageLogList(self,ctx):
		print "callin (getMessageLogList)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_target_id = d[idx:idx+size]
		idx+=size
		_p_type, = struct.unpack('!i',d[idx:idx+4])
		idx+=4
		_p_timerange = TimeRange_t()
		r,idx = _p_timerange.unmarshall(d,idx)
		if not r: return False
		cr = None
		cr = self.inst.getMessageLogList(_p_target_id,_p_type,_p_timerange,ctx)
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
	
	def setUserStatus(self,ctx):
		print "callin (setUserStatus)"
		d = ctx.msg.paramstream 
		idx = 0
		_p_type, = struct.unpack('!i',d[idx:idx+4])
		idx+=4
		cr = None
		self.inst.setUserStatus(_p_type,ctx)
		return True
	
	def getUserStatus(self,ctx):
		print "callin (getUserStatus)"
		d = ctx.msg.paramstream 
		idx = 0
		cr = None
		cr = self.inst.getUserStatus(ctx)
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
	
	def getUserStatusList(self,ctx):
		print "callin (getUserStatusList)"
		d = ctx.msg.paramstream 
		idx = 0
		_p_userids =[] 
		container = SIDS_t(_p_userids)
		r,idx = container.unmarshall(d,idx)
		if not r: return False
		cr = None
		cr = self.inst.getUserStatusList(_p_userids,ctx)
		if  cr == None: return True
		d = '' 
		m = tce.RpcMessageReturn()
		m.sequence = ctx.msg.sequence
		m.callmsg = ctx.msg
		m.ifidx = ctx.msg.ifidx
		m.call_id = ctx.msg.call_id
		m.conn = ctx.msg.conn
		m.extra = ctx.msg.extra
		container = UserStatusList_t(cr)
		d += container.marshall()
		if d: m.paramstream += d
		ctx.conn.sendMessage(m)
		return True
	
	def inviteStranger(self,ctx):
		print "callin (inviteStranger)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_target = d[idx:idx+size]
		idx+=size
		_p_type, = struct.unpack('!i',d[idx:idx+4])
		idx+=4
		_p_msg = MimeText_t()
		r,idx = _p_msg.unmarshall(d,idx)
		if not r: return False
		cr = None
		cr = self.inst.inviteStranger(_p_target,_p_type,_p_msg,ctx)
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
	
	
class IUserServicePrx:
	# -- INTERFACE PROXY -- 
	def __init__(self,conn):
		self.conn = conn
		self.delta = None
		pass
	
	@staticmethod
	def create(pdest,try_connect=False):
		conn = tce.RpcConnection(pdest=pdest)
		proxy = IUserServicePrx(conn)
		return proxy
	
	@staticmethod
	def createWithMQ(name):
		ep = tce.RpcMqSet.instance().server.findEndPointByName(name)
		if not ep: return None
		conn = ep.impl
		proxy = IUserServicePrx(conn)
		return proxy
	
	#extra must be map<string,string>
	def getFriendGroups(self,timeout=0,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 0
		m.extra.setStrDict(extra)
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
		idx = 0
		d = m.paramstream
		p = None
		r = False
		try:
			p =[]
			container = UserGroupInfoList_t(p)
			r,idx = container.unmarshall(d,idx)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_UNSERIALIZE_FAILED)
		return p
	
	def getFriendGroups_async(self,async,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 0
		m.extra.setStrDict(extra)
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		m.async = async
		m.asyncparser = IUserServicePrx.getFriendGroups_asyncparser
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def getFriendGroups_asyncparser(m,m2):
		# function index: 56 , m2 - callreturn msg.
		
		stream = m2.paramstream
		user = m.async
		prx = m.prx
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC: return 
		try:
			idx = 0
			d = stream
			r = True
			p =[]
			container = UserGroupInfoList_t(p)
			r,idx = container.unmarshall(d,idx)
			if r:
				user(p,prx)
		except:
			traceback.print_exc()
		
	
	#extra must be map<string,string>
	def getFriendsInGroup(self,group_id,timeout=0,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 1
		m.extra.setStrDict(extra)
		d = '' 
		if type(group_id)==type(0) or type(group_id) == type(0.1): group_id=str(group_id)
		if not group_id: group_id=''
		try:
			group_id = group_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(group_id)))
		d += str(group_id)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
		idx = 0
		d = m.paramstream
		p = None
		r = False
		try:
			p =[]
			container = UserInfoList_t(p)
			r,idx = container.unmarshall(d,idx)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_UNSERIALIZE_FAILED)
		return p
	
	def getFriendsInGroup_async(self,group_id,async,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 1
		m.extra.setStrDict(extra)
		d = '' 
		if type(group_id)==type(0) or type(group_id) == type(0.1): group_id=str(group_id)
		if not group_id: group_id=''
		try:
			group_id = group_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(group_id)))
		d += str(group_id)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		m.async = async
		m.asyncparser = IUserServicePrx.getFriendsInGroup_asyncparser
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def getFriendsInGroup_asyncparser(m,m2):
		# function index: 56 , m2 - callreturn msg.
		
		stream = m2.paramstream
		user = m.async
		prx = m.prx
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC: return 
		try:
			idx = 0
			d = stream
			r = True
			p =[]
			container = UserInfoList_t(p)
			r,idx = container.unmarshall(d,idx)
			if r:
				user(p,prx)
		except:
			traceback.print_exc()
		
	
	#extra must be map<string,string>
	def getAllFriends(self,timeout=0,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 2
		m.extra.setStrDict(extra)
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
		idx = 0
		d = m.paramstream
		p = None
		r = False
		try:
			p =[]
			container = UserInfoList_t(p)
			r,idx = container.unmarshall(d,idx)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_UNSERIALIZE_FAILED)
		return p
	
	def getAllFriends_async(self,async,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 2
		m.extra.setStrDict(extra)
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		m.async = async
		m.asyncparser = IUserServicePrx.getAllFriends_asyncparser
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def getAllFriends_asyncparser(m,m2):
		# function index: 56 , m2 - callreturn msg.
		
		stream = m2.paramstream
		user = m.async
		prx = m.prx
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC: return 
		try:
			idx = 0
			d = stream
			r = True
			p =[]
			container = UserInfoList_t(p)
			r,idx = container.unmarshall(d,idx)
			if r:
				user(p,prx)
		except:
			traceback.print_exc()
		
	
	#extra must be map<string,string>
	def getUserDetail(self,user_id,timeout=0,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 3
		m.extra.setStrDict(extra)
		d = '' 
		if type(user_id)==type(0) or type(user_id) == type(0.1): user_id=str(user_id)
		if not user_id: user_id=''
		try:
			user_id = user_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(user_id)))
		d += str(user_id)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
		idx = 0
		d = m.paramstream
		p = None
		r = False
		try:
			p = UserInfoDetail_t()
			r,idx = p.unmarshall(d,idx)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_UNSERIALIZE_FAILED)
		return p
	
	def getUserDetail_async(self,user_id,async,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 3
		m.extra.setStrDict(extra)
		d = '' 
		if type(user_id)==type(0) or type(user_id) == type(0.1): user_id=str(user_id)
		if not user_id: user_id=''
		try:
			user_id = user_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(user_id)))
		d += str(user_id)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		m.async = async
		m.asyncparser = IUserServicePrx.getUserDetail_asyncparser
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def getUserDetail_asyncparser(m,m2):
		# function index: 56 , m2 - callreturn msg.
		
		stream = m2.paramstream
		user = m.async
		prx = m.prx
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC: return 
		try:
			idx = 0
			d = stream
			r = True
			p = UserInfoDetail_t()
			r,idx = p.unmarshall(d,idx)
			if r:
				user(p,prx)
		except:
			traceback.print_exc()
		
	
	#extra must be map<string,string>
	def renameFriendName(self,user_id,nickname,timeout=0,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 4
		m.extra.setStrDict(extra)
		d = '' 
		if type(user_id)==type(0) or type(user_id) == type(0.1): user_id=str(user_id)
		if not user_id: user_id=''
		try:
			user_id = user_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(user_id)))
		d += str(user_id)
		m.paramstream+=d
		d = '' 
		if type(nickname)==type(0) or type(nickname) == type(0.1): nickname=str(nickname)
		if not nickname: nickname=''
		try:
			nickname = nickname.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(nickname)))
		d += str(nickname)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
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
	
	def renameFriendName_async(self,user_id,nickname,async,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 4
		m.extra.setStrDict(extra)
		d = '' 
		if type(user_id)==type(0) or type(user_id) == type(0.1): user_id=str(user_id)
		if not user_id: user_id=''
		try:
			user_id = user_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(user_id)))
		d += str(user_id)
		m.paramstream+=d
		d = '' 
		if type(nickname)==type(0) or type(nickname) == type(0.1): nickname=str(nickname)
		if not nickname: nickname=''
		try:
			nickname = nickname.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(nickname)))
		d += str(nickname)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		m.async = async
		m.asyncparser = IUserServicePrx.renameFriendName_asyncparser
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def renameFriendName_asyncparser(m,m2):
		# function index: 56 , m2 - callreturn msg.
		
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
	def getUserInfoList(self,userids,timeout=0,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 5
		m.extra.setStrDict(extra)
		d = '' 
		container = UserIdList_t(userids)
		d += container.marshall()
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
		idx = 0
		d = m.paramstream
		p = None
		r = False
		try:
			p =[]
			container = UserInfoList_t(p)
			r,idx = container.unmarshall(d,idx)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_UNSERIALIZE_FAILED)
		return p
	
	def getUserInfoList_async(self,userids,async,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 5
		m.extra.setStrDict(extra)
		d = '' 
		container = UserIdList_t(userids)
		d += container.marshall()
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		m.async = async
		m.asyncparser = IUserServicePrx.getUserInfoList_asyncparser
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def getUserInfoList_asyncparser(m,m2):
		# function index: 56 , m2 - callreturn msg.
		
		stream = m2.paramstream
		user = m.async
		prx = m.prx
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC: return 
		try:
			idx = 0
			d = stream
			r = True
			p =[]
			container = UserInfoList_t(p)
			r,idx = container.unmarshall(d,idx)
			if r:
				user(p,prx)
		except:
			traceback.print_exc()
		
	
	#extra must be map<string,string>
	def updateUserInfo(self,userinfo,timeout=0,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 6
		m.extra.setStrDict(extra)
		d = '' 
		d += userinfo.marshall()
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
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
	
	def updateUserInfo_async(self,userinfo,async,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 6
		m.extra.setStrDict(extra)
		d = '' 
		d += userinfo.marshall()
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		m.async = async
		m.asyncparser = IUserServicePrx.updateUserInfo_asyncparser
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def updateUserInfo_asyncparser(m,m2):
		# function index: 56 , m2 - callreturn msg.
		
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
	def changeUserPasswd(self,oldpasswd,newpasswd,timeout=0,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 7
		m.extra.setStrDict(extra)
		d = '' 
		if type(oldpasswd)==type(0) or type(oldpasswd) == type(0.1): oldpasswd=str(oldpasswd)
		if not oldpasswd: oldpasswd=''
		try:
			oldpasswd = oldpasswd.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(oldpasswd)))
		d += str(oldpasswd)
		m.paramstream+=d
		d = '' 
		if type(newpasswd)==type(0) or type(newpasswd) == type(0.1): newpasswd=str(newpasswd)
		if not newpasswd: newpasswd=''
		try:
			newpasswd = newpasswd.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(newpasswd)))
		d += str(newpasswd)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
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
	
	def changeUserPasswd_async(self,oldpasswd,newpasswd,async,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 7
		m.extra.setStrDict(extra)
		d = '' 
		if type(oldpasswd)==type(0) or type(oldpasswd) == type(0.1): oldpasswd=str(oldpasswd)
		if not oldpasswd: oldpasswd=''
		try:
			oldpasswd = oldpasswd.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(oldpasswd)))
		d += str(oldpasswd)
		m.paramstream+=d
		d = '' 
		if type(newpasswd)==type(0) or type(newpasswd) == type(0.1): newpasswd=str(newpasswd)
		if not newpasswd: newpasswd=''
		try:
			newpasswd = newpasswd.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(newpasswd)))
		d += str(newpasswd)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		m.async = async
		m.asyncparser = IUserServicePrx.changeUserPasswd_asyncparser
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def changeUserPasswd_asyncparser(m,m2):
		# function index: 56 , m2 - callreturn msg.
		
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
	def getUserInfo(self,timeout=0,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 8
		m.extra.setStrDict(extra)
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
		idx = 0
		d = m.paramstream
		p = None
		r = False
		try:
			p = UserInfo_t()
			r,idx = p.unmarshall(d,idx)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_UNSERIALIZE_FAILED)
		return p
	
	def getUserInfo_async(self,async,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 8
		m.extra.setStrDict(extra)
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		m.async = async
		m.asyncparser = IUserServicePrx.getUserInfo_asyncparser
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def getUserInfo_asyncparser(m,m2):
		# function index: 56 , m2 - callreturn msg.
		
		stream = m2.paramstream
		user = m.async
		prx = m.prx
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC: return 
		try:
			idx = 0
			d = stream
			r = True
			p = UserInfo_t()
			r,idx = p.unmarshall(d,idx)
			if r:
				user(p,prx)
		except:
			traceback.print_exc()
		
	
	#extra must be map<string,string>
	def getInvitorOfStranger(self,timeout=0,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 9
		m.extra.setStrDict(extra)
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
		idx = 0
		d = m.paramstream
		p = None
		r = False
		try:
			p = UserInfo_t()
			r,idx = p.unmarshall(d,idx)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_UNSERIALIZE_FAILED)
		return p
	
	def getInvitorOfStranger_async(self,async,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 9
		m.extra.setStrDict(extra)
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		m.async = async
		m.asyncparser = IUserServicePrx.getInvitorOfStranger_asyncparser
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def getInvitorOfStranger_asyncparser(m,m2):
		# function index: 56 , m2 - callreturn msg.
		
		stream = m2.paramstream
		user = m.async
		prx = m.prx
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC: return 
		try:
			idx = 0
			d = stream
			r = True
			p = UserInfo_t()
			r,idx = p.unmarshall(d,idx)
			if r:
				user(p,prx)
		except:
			traceback.print_exc()
		
	
	#extra must be map<string,string>
	def createGroup(self,group,timeout=0,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 10
		m.extra.setStrDict(extra)
		d = '' 
		d += group.marshall()
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
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
	
	def createGroup_async(self,group,async,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 10
		m.extra.setStrDict(extra)
		d = '' 
		d += group.marshall()
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		m.async = async
		m.asyncparser = IUserServicePrx.createGroup_asyncparser
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def createGroup_asyncparser(m,m2):
		# function index: 56 , m2 - callreturn msg.
		
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
	def deleteGroup(self,group_id,timeout=0,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 11
		m.extra.setStrDict(extra)
		d = '' 
		if type(group_id)==type(0) or type(group_id) == type(0.1): group_id=str(group_id)
		if not group_id: group_id=''
		try:
			group_id = group_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(group_id)))
		d += str(group_id)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
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
	
	def deleteGroup_async(self,group_id,async,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 11
		m.extra.setStrDict(extra)
		d = '' 
		if type(group_id)==type(0) or type(group_id) == type(0.1): group_id=str(group_id)
		if not group_id: group_id=''
		try:
			group_id = group_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(group_id)))
		d += str(group_id)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		m.async = async
		m.asyncparser = IUserServicePrx.deleteGroup_asyncparser
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def deleteGroup_asyncparser(m,m2):
		# function index: 56 , m2 - callreturn msg.
		
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
	def addGroupUser(self,group_id,user_id,timeout=0,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 12
		m.extra.setStrDict(extra)
		d = '' 
		if type(group_id)==type(0) or type(group_id) == type(0.1): group_id=str(group_id)
		if not group_id: group_id=''
		try:
			group_id = group_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(group_id)))
		d += str(group_id)
		m.paramstream+=d
		d = '' 
		if type(user_id)==type(0) or type(user_id) == type(0.1): user_id=str(user_id)
		if not user_id: user_id=''
		try:
			user_id = user_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(user_id)))
		d += str(user_id)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
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
	
	def addGroupUser_async(self,group_id,user_id,async,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 12
		m.extra.setStrDict(extra)
		d = '' 
		if type(group_id)==type(0) or type(group_id) == type(0.1): group_id=str(group_id)
		if not group_id: group_id=''
		try:
			group_id = group_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(group_id)))
		d += str(group_id)
		m.paramstream+=d
		d = '' 
		if type(user_id)==type(0) or type(user_id) == type(0.1): user_id=str(user_id)
		if not user_id: user_id=''
		try:
			user_id = user_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(user_id)))
		d += str(user_id)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		m.async = async
		m.asyncparser = IUserServicePrx.addGroupUser_asyncparser
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def addGroupUser_asyncparser(m,m2):
		# function index: 56 , m2 - callreturn msg.
		
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
	def removeGroupUser(self,group_id,user_id,timeout=0,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 13
		m.extra.setStrDict(extra)
		d = '' 
		if type(group_id)==type(0) or type(group_id) == type(0.1): group_id=str(group_id)
		if not group_id: group_id=''
		try:
			group_id = group_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(group_id)))
		d += str(group_id)
		m.paramstream+=d
		d = '' 
		if type(user_id)==type(0) or type(user_id) == type(0.1): user_id=str(user_id)
		if not user_id: user_id=''
		try:
			user_id = user_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(user_id)))
		d += str(user_id)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
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
	
	def removeGroupUser_async(self,group_id,user_id,async,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 13
		m.extra.setStrDict(extra)
		d = '' 
		if type(group_id)==type(0) or type(group_id) == type(0.1): group_id=str(group_id)
		if not group_id: group_id=''
		try:
			group_id = group_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(group_id)))
		d += str(group_id)
		m.paramstream+=d
		d = '' 
		if type(user_id)==type(0) or type(user_id) == type(0.1): user_id=str(user_id)
		if not user_id: user_id=''
		try:
			user_id = user_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(user_id)))
		d += str(user_id)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		m.async = async
		m.asyncparser = IUserServicePrx.removeGroupUser_asyncparser
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def removeGroupUser_asyncparser(m,m2):
		# function index: 56 , m2 - callreturn msg.
		
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
	def removeFriend(self,user_id,timeout=0,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 14
		m.extra.setStrDict(extra)
		d = '' 
		if type(user_id)==type(0) or type(user_id) == type(0.1): user_id=str(user_id)
		if not user_id: user_id=''
		try:
			user_id = user_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(user_id)))
		d += str(user_id)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
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
	
	def removeFriend_async(self,user_id,async,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 14
		m.extra.setStrDict(extra)
		d = '' 
		if type(user_id)==type(0) or type(user_id) == type(0.1): user_id=str(user_id)
		if not user_id: user_id=''
		try:
			user_id = user_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(user_id)))
		d += str(user_id)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		m.async = async
		m.asyncparser = IUserServicePrx.removeFriend_asyncparser
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def removeFriend_asyncparser(m,m2):
		# function index: 56 , m2 - callreturn msg.
		
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
	def getTeams(self,timeout=0,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 15
		m.extra.setStrDict(extra)
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
		idx = 0
		d = m.paramstream
		p = None
		r = False
		try:
			p =[]
			container = TeamInfoList_t(p)
			r,idx = container.unmarshall(d,idx)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_UNSERIALIZE_FAILED)
		return p
	
	def getTeams_async(self,async,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 15
		m.extra.setStrDict(extra)
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		m.async = async
		m.asyncparser = IUserServicePrx.getTeams_asyncparser
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def getTeams_asyncparser(m,m2):
		# function index: 56 , m2 - callreturn msg.
		
		stream = m2.paramstream
		user = m.async
		prx = m.prx
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC: return 
		try:
			idx = 0
			d = stream
			r = True
			p =[]
			container = TeamInfoList_t(p)
			r,idx = container.unmarshall(d,idx)
			if r:
				user(p,prx)
		except:
			traceback.print_exc()
		
	
	#extra must be map<string,string>
	def getUsersInTeam(self,team_id,timeout=0,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 16
		m.extra.setStrDict(extra)
		d = '' 
		if type(team_id)==type(0) or type(team_id) == type(0.1): team_id=str(team_id)
		if not team_id: team_id=''
		try:
			team_id = team_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(team_id)))
		d += str(team_id)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
		idx = 0
		d = m.paramstream
		p = None
		r = False
		try:
			p =[]
			container = UserInfoList_t(p)
			r,idx = container.unmarshall(d,idx)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_UNSERIALIZE_FAILED)
		return p
	
	def getUsersInTeam_async(self,team_id,async,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 16
		m.extra.setStrDict(extra)
		d = '' 
		if type(team_id)==type(0) or type(team_id) == type(0.1): team_id=str(team_id)
		if not team_id: team_id=''
		try:
			team_id = team_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(team_id)))
		d += str(team_id)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		m.async = async
		m.asyncparser = IUserServicePrx.getUsersInTeam_asyncparser
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def getUsersInTeam_asyncparser(m,m2):
		# function index: 56 , m2 - callreturn msg.
		
		stream = m2.paramstream
		user = m.async
		prx = m.prx
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC: return 
		try:
			idx = 0
			d = stream
			r = True
			p =[]
			container = UserInfoList_t(p)
			r,idx = container.unmarshall(d,idx)
			if r:
				user(p,prx)
		except:
			traceback.print_exc()
		
	
	#extra must be map<string,string>
	def addTeamUser(self,team_id,user_id,timeout=0,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 17
		m.extra.setStrDict(extra)
		d = '' 
		if type(team_id)==type(0) or type(team_id) == type(0.1): team_id=str(team_id)
		if not team_id: team_id=''
		try:
			team_id = team_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(team_id)))
		d += str(team_id)
		m.paramstream+=d
		d = '' 
		if type(user_id)==type(0) or type(user_id) == type(0.1): user_id=str(user_id)
		if not user_id: user_id=''
		try:
			user_id = user_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(user_id)))
		d += str(user_id)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
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
	
	def addTeamUser_async(self,team_id,user_id,async,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 17
		m.extra.setStrDict(extra)
		d = '' 
		if type(team_id)==type(0) or type(team_id) == type(0.1): team_id=str(team_id)
		if not team_id: team_id=''
		try:
			team_id = team_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(team_id)))
		d += str(team_id)
		m.paramstream+=d
		d = '' 
		if type(user_id)==type(0) or type(user_id) == type(0.1): user_id=str(user_id)
		if not user_id: user_id=''
		try:
			user_id = user_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(user_id)))
		d += str(user_id)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		m.async = async
		m.asyncparser = IUserServicePrx.addTeamUser_asyncparser
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def addTeamUser_asyncparser(m,m2):
		# function index: 56 , m2 - callreturn msg.
		
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
	def removeTeamUser(self,team_id,user_id,timeout=0,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 18
		m.extra.setStrDict(extra)
		d = '' 
		if type(team_id)==type(0) or type(team_id) == type(0.1): team_id=str(team_id)
		if not team_id: team_id=''
		try:
			team_id = team_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(team_id)))
		d += str(team_id)
		m.paramstream+=d
		d = '' 
		if type(user_id)==type(0) or type(user_id) == type(0.1): user_id=str(user_id)
		if not user_id: user_id=''
		try:
			user_id = user_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(user_id)))
		d += str(user_id)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
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
	
	def removeTeamUser_async(self,team_id,user_id,async,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 18
		m.extra.setStrDict(extra)
		d = '' 
		if type(team_id)==type(0) or type(team_id) == type(0.1): team_id=str(team_id)
		if not team_id: team_id=''
		try:
			team_id = team_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(team_id)))
		d += str(team_id)
		m.paramstream+=d
		d = '' 
		if type(user_id)==type(0) or type(user_id) == type(0.1): user_id=str(user_id)
		if not user_id: user_id=''
		try:
			user_id = user_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(user_id)))
		d += str(user_id)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		m.async = async
		m.asyncparser = IUserServicePrx.removeTeamUser_asyncparser
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def removeTeamUser_asyncparser(m,m2):
		# function index: 56 , m2 - callreturn msg.
		
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
	def exitTeam(self,team_id,timeout=0,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 19
		m.extra.setStrDict(extra)
		d = '' 
		if type(team_id)==type(0) or type(team_id) == type(0.1): team_id=str(team_id)
		if not team_id: team_id=''
		try:
			team_id = team_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(team_id)))
		d += str(team_id)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
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
	
	def exitTeam_async(self,team_id,async,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 19
		m.extra.setStrDict(extra)
		d = '' 
		if type(team_id)==type(0) or type(team_id) == type(0.1): team_id=str(team_id)
		if not team_id: team_id=''
		try:
			team_id = team_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(team_id)))
		d += str(team_id)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		m.async = async
		m.asyncparser = IUserServicePrx.exitTeam_asyncparser
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def exitTeam_asyncparser(m,m2):
		# function index: 56 , m2 - callreturn msg.
		
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
	def createTeam(self,team,timeout=0,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 20
		m.extra.setStrDict(extra)
		d = '' 
		d += team.marshall()
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
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
	
	def createTeam_async(self,team,async,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 20
		m.extra.setStrDict(extra)
		d = '' 
		d += team.marshall()
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		m.async = async
		m.asyncparser = IUserServicePrx.createTeam_asyncparser
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def createTeam_asyncparser(m,m2):
		# function index: 56 , m2 - callreturn msg.
		
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
	def deleteTeam(self,team_id,timeout=0,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 21
		m.extra.setStrDict(extra)
		d = '' 
		if type(team_id)==type(0) or type(team_id) == type(0.1): team_id=str(team_id)
		if not team_id: team_id=''
		try:
			team_id = team_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(team_id)))
		d += str(team_id)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
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
	
	def deleteTeam_async(self,team_id,async,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 21
		m.extra.setStrDict(extra)
		d = '' 
		if type(team_id)==type(0) or type(team_id) == type(0.1): team_id=str(team_id)
		if not team_id: team_id=''
		try:
			team_id = team_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(team_id)))
		d += str(team_id)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		m.async = async
		m.asyncparser = IUserServicePrx.deleteTeam_asyncparser
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def deleteTeam_asyncparser(m,m2):
		# function index: 56 , m2 - callreturn msg.
		
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
	def updateTeamInfo(self,team,timeout=0,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 22
		m.extra.setStrDict(extra)
		d = '' 
		d += team.marshall()
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
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
	
	def updateTeamInfo_async(self,team,async,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 22
		m.extra.setStrDict(extra)
		d = '' 
		d += team.marshall()
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		m.async = async
		m.asyncparser = IUserServicePrx.updateTeamInfo_asyncparser
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def updateTeamInfo_asyncparser(m,m2):
		# function index: 56 , m2 - callreturn msg.
		
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
	def inviteFriend(self,stranger_id,msg,timeout=0,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 23
		m.extra.setStrDict(extra)
		d = '' 
		if type(stranger_id)==type(0) or type(stranger_id) == type(0.1): stranger_id=str(stranger_id)
		if not stranger_id: stranger_id=''
		try:
			stranger_id = stranger_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(stranger_id)))
		d += str(stranger_id)
		m.paramstream+=d
		d = '' 
		d += msg.marshall()
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
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
	
	def inviteFriend_async(self,stranger_id,msg,async,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 23
		m.extra.setStrDict(extra)
		d = '' 
		if type(stranger_id)==type(0) or type(stranger_id) == type(0.1): stranger_id=str(stranger_id)
		if not stranger_id: stranger_id=''
		try:
			stranger_id = stranger_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(stranger_id)))
		d += str(stranger_id)
		m.paramstream+=d
		d = '' 
		d += msg.marshall()
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		m.async = async
		m.asyncparser = IUserServicePrx.inviteFriend_asyncparser
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def inviteFriend_asyncparser(m,m2):
		# function index: 56 , m2 - callreturn msg.
		
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
	def inviteFriendReject(self,seq,reason,timeout=0,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 24
		m.extra.setStrDict(extra)
		d = '' 
		if type(seq)==type(0) or type(seq) == type(0.1): seq=str(seq)
		if not seq: seq=''
		try:
			seq = seq.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(seq)))
		d += str(seq)
		m.paramstream+=d
		d = '' 
		if type(reason)==type(0) or type(reason) == type(0.1): reason=str(reason)
		if not reason: reason=''
		try:
			reason = reason.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(reason)))
		d += str(reason)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def inviteFriendReject_oneway(self,seq,reason,extra={}):
		# function index: 56
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 6
			m.opidx = 24
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcMqSet.instance().server.getId()
			m.extra.setStrDict(extra)
			d = '' 
			if type(seq)==type(0) or type(seq) == type(0.1): seq=str(seq)
			if not seq: seq=''
			try:
				seq = seq.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(seq)))
			d += str(seq)
			m.paramstream+=d
			d = '' 
			if type(reason)==type(0) or type(reason) == type(0.1): reason=str(reason)
			if not reason: reason=''
			try:
				reason = reason.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(reason)))
			d += str(reason)
			m.paramstream+=d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	#extra must be map<string,string>
	def inviteFriendAccept(self,seq,timeout=0,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 25
		m.extra.setStrDict(extra)
		d = '' 
		if type(seq)==type(0) or type(seq) == type(0.1): seq=str(seq)
		if not seq: seq=''
		try:
			seq = seq.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(seq)))
		d += str(seq)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def inviteFriendAccept_oneway(self,seq,extra={}):
		# function index: 56
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 6
			m.opidx = 25
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcMqSet.instance().server.getId()
			m.extra.setStrDict(extra)
			d = '' 
			if type(seq)==type(0) or type(seq) == type(0.1): seq=str(seq)
			if not seq: seq=''
			try:
				seq = seq.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(seq)))
			d += str(seq)
			m.paramstream+=d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	#extra must be map<string,string>
	def getMessageLogList(self,target_id,type,timerange,timeout=0,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 26
		m.extra.setStrDict(extra)
		d = '' 
		if type(target_id)==type(0) or type(target_id) == type(0.1): target_id=str(target_id)
		if not target_id: target_id=''
		try:
			target_id = target_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(target_id)))
		d += str(target_id)
		m.paramstream+=d
		d = '' 
		d += struct.pack('!i',type)
		m.paramstream+=d
		d = '' 
		d += timerange.marshall()
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
		idx = 0
		d = m.paramstream
		p = None
		r = False
		try:
			p = QueryMessageLogResult_t()
			r,idx = p.unmarshall(d,idx)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_UNSERIALIZE_FAILED)
		return p
	
	def getMessageLogList_async(self,target_id,type,timerange,async,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 26
		m.extra.setStrDict(extra)
		d = '' 
		if type(target_id)==type(0) or type(target_id) == type(0.1): target_id=str(target_id)
		if not target_id: target_id=''
		try:
			target_id = target_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(target_id)))
		d += str(target_id)
		m.paramstream+=d
		d = '' 
		d += struct.pack('!i',type)
		m.paramstream+=d
		d = '' 
		d += timerange.marshall()
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		m.async = async
		m.asyncparser = IUserServicePrx.getMessageLogList_asyncparser
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def getMessageLogList_asyncparser(m,m2):
		# function index: 56 , m2 - callreturn msg.
		
		stream = m2.paramstream
		user = m.async
		prx = m.prx
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC: return 
		try:
			idx = 0
			d = stream
			r = True
			p = QueryMessageLogResult_t()
			r,idx = p.unmarshall(d,idx)
			if r:
				user(p,prx)
		except:
			traceback.print_exc()
		
	
	#extra must be map<string,string>
	def setUserStatus(self,type,timeout=0,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 27
		m.extra.setStrDict(extra)
		d = '' 
		d += struct.pack('!i',type)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def setUserStatus_oneway(self,type,extra={}):
		# function index: 56
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 6
			m.opidx = 27
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcMqSet.instance().server.getId()
			m.extra.setStrDict(extra)
			d = '' 
			d += struct.pack('!i',type)
			m.paramstream+=d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	#extra must be map<string,string>
	def getUserStatus(self,timeout=0,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 28
		m.extra.setStrDict(extra)
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
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
	
	def getUserStatus_async(self,async,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 28
		m.extra.setStrDict(extra)
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		m.async = async
		m.asyncparser = IUserServicePrx.getUserStatus_asyncparser
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def getUserStatus_asyncparser(m,m2):
		# function index: 56 , m2 - callreturn msg.
		
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
	def getUserStatusList(self,userids,timeout=0,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 29
		m.extra.setStrDict(extra)
		d = '' 
		container = SIDS_t(userids)
		d += container.marshall()
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
		idx = 0
		d = m.paramstream
		p = None
		r = False
		try:
			p =[]
			container = UserStatusList_t(p)
			r,idx = container.unmarshall(d,idx)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_UNSERIALIZE_FAILED)
		return p
	
	def getUserStatusList_async(self,userids,async,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 29
		m.extra.setStrDict(extra)
		d = '' 
		container = SIDS_t(userids)
		d += container.marshall()
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		m.async = async
		m.asyncparser = IUserServicePrx.getUserStatusList_asyncparser
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def getUserStatusList_asyncparser(m,m2):
		# function index: 56 , m2 - callreturn msg.
		
		stream = m2.paramstream
		user = m.async
		prx = m.prx
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC: return 
		try:
			idx = 0
			d = stream
			r = True
			p =[]
			container = UserStatusList_t(p)
			r,idx = container.unmarshall(d,idx)
			if r:
				user(p,prx)
		except:
			traceback.print_exc()
		
	
	#extra must be map<string,string>
	def inviteStranger(self,target,type,msg,timeout=0,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 30
		m.extra.setStrDict(extra)
		d = '' 
		if type(target)==type(0) or type(target) == type(0.1): target=str(target)
		if not target: target=''
		try:
			target = target.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(target)))
		d += str(target)
		m.paramstream+=d
		d = '' 
		d += struct.pack('!i',type)
		m.paramstream+=d
		d = '' 
		d += msg.marshall()
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
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
	
	def inviteStranger_async(self,target,type,msg,async,extra={}):
		# function index: 56
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 6
		m.opidx = 30
		m.extra.setStrDict(extra)
		d = '' 
		if type(target)==type(0) or type(target) == type(0.1): target=str(target)
		if not target: target=''
		try:
			target = target.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(target)))
		d += str(target)
		m.paramstream+=d
		d = '' 
		d += struct.pack('!i',type)
		m.paramstream+=d
		d = '' 
		d += msg.marshall()
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		m.async = async
		m.asyncparser = IUserServicePrx.inviteStranger_asyncparser
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def inviteStranger_asyncparser(m,m2):
		# function index: 56 , m2 - callreturn msg.
		
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
		
	

class UserRegisterInfo_t:
# -- STRUCT -- 
	def __init__(self,name='',passwd='',email=''):
		self.name = name
		self.passwd = passwd
		self.email = email
		
	def __str__(self):
		return 'OBJECT<UserRegisterInfo_t :%s> { name:%s,passwd:%s,email:%s}'%(hex(id(self)),str(self.name),str(self.passwd),str(self.email) ) 
		
	def marshall(self):
		d =''
		if type(self.name)==type(0) or type(self.name) == type(0.1): self.name=str(self.name)
		if not self.name: self.name=''
		try:
			self.name = self.name.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.name)))
		d += str(self.name)
		if type(self.passwd)==type(0) or type(self.passwd) == type(0.1): self.passwd=str(self.passwd)
		if not self.passwd: self.passwd=''
		try:
			self.passwd = self.passwd.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.passwd)))
		d += str(self.passwd)
		if type(self.email)==type(0) or type(self.email) == type(0.1): self.email=str(self.email)
		if not self.email: self.email=''
		try:
			self.email = self.email.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.email)))
		d += str(self.email)
		return d
		
	def unmarshall(self,d,idx_=0):
		idx = idx_
		try:
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.name = d[idx:idx+size]
			idx+=size
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.passwd = d[idx:idx+size]
			idx+=size
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.email = d[idx:idx+size]
			idx+=size
		except:
			traceback.print_exc()
			return False,idx
		return True,idx
		

class ICtrlServer:
	# -- INTERFACE -- 
	def __init__(self):
		self.delegatecls = ICtrlServer_delegate
	
	def registerUser(self,reginfo,ctx):
		return CallReturn_t()
	def deleteUser(self,user_id,ctx):
		return CallReturn_t()
	def dispatchGWA(self,fromtype,ctx):
		return [ ]
	def dispatchTalkingServer(self,ctx):
		return [ ]

class ICtrlServer_delegate:
	def __init__(self,inst,adapter,conn=None):
		self.index = 7
		self.optlist={}
		self.id = '' 
		self.adapter = adapter
		self.optlist[0] = (self.registerUser)
		self.optlist[1] = (self.deleteUser)
		self.optlist[2] = (self.dispatchGWA)
		self.optlist[3] = (self.dispatchTalkingServer)
		
		self.inst = inst
	
	def registerUser(self,ctx):
		print "callin (registerUser)"
		d = ctx.msg.paramstream 
		idx = 0
		_p_reginfo = UserRegisterInfo_t()
		r,idx = _p_reginfo.unmarshall(d,idx)
		if not r: return False
		cr = None
		cr = self.inst.registerUser(_p_reginfo,ctx)
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
	
	def deleteUser(self,ctx):
		print "callin (deleteUser)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_user_id = d[idx:idx+size]
		idx+=size
		cr = None
		cr = self.inst.deleteUser(_p_user_id,ctx)
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
	
	def dispatchGWA(self,ctx):
		print "callin (dispatchGWA)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_fromtype = d[idx:idx+size]
		idx+=size
		cr = None
		cr = self.inst.dispatchGWA(_p_fromtype,ctx)
		if  cr == None: return True
		d = '' 
		m = tce.RpcMessageReturn()
		m.sequence = ctx.msg.sequence
		m.callmsg = ctx.msg
		m.ifidx = ctx.msg.ifidx
		m.call_id = ctx.msg.call_id
		m.conn = ctx.msg.conn
		m.extra = ctx.msg.extra
		container = ServiceURIList_t(cr)
		d += container.marshall()
		if d: m.paramstream += d
		ctx.conn.sendMessage(m)
		return True
	
	def dispatchTalkingServer(self,ctx):
		print "callin (dispatchTalkingServer)"
		d = ctx.msg.paramstream 
		idx = 0
		cr = None
		cr = self.inst.dispatchTalkingServer(ctx)
		if  cr == None: return True
		d = '' 
		m = tce.RpcMessageReturn()
		m.sequence = ctx.msg.sequence
		m.callmsg = ctx.msg
		m.ifidx = ctx.msg.ifidx
		m.call_id = ctx.msg.call_id
		m.conn = ctx.msg.conn
		m.extra = ctx.msg.extra
		container = ServiceURIList_t(cr)
		d += container.marshall()
		if d: m.paramstream += d
		ctx.conn.sendMessage(m)
		return True
	
	
class ICtrlServerPrx:
	# -- INTERFACE PROXY -- 
	def __init__(self,conn):
		self.conn = conn
		self.delta = None
		pass
	
	@staticmethod
	def create(pdest,try_connect=False):
		conn = tce.RpcConnection(pdest=pdest)
		proxy = ICtrlServerPrx(conn)
		return proxy
	
	@staticmethod
	def createWithMQ(name):
		ep = tce.RpcMqSet.instance().server.findEndPointByName(name)
		if not ep: return None
		conn = ep.impl
		proxy = ICtrlServerPrx(conn)
		return proxy
	
	#extra must be map<string,string>
	def registerUser(self,reginfo,timeout=0,extra={}):
		# function index: 58
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 7
		m.opidx = 0
		m.extra.setStrDict(extra)
		d = '' 
		d += reginfo.marshall()
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
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
	
	def registerUser_async(self,reginfo,async,extra={}):
		# function index: 58
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 7
		m.opidx = 0
		m.extra.setStrDict(extra)
		d = '' 
		d += reginfo.marshall()
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		m.async = async
		m.asyncparser = ICtrlServerPrx.registerUser_asyncparser
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def registerUser_asyncparser(m,m2):
		# function index: 58 , m2 - callreturn msg.
		
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
	def deleteUser(self,user_id,timeout=0,extra={}):
		# function index: 58
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 7
		m.opidx = 1
		m.extra.setStrDict(extra)
		d = '' 
		if type(user_id)==type(0) or type(user_id) == type(0.1): user_id=str(user_id)
		if not user_id: user_id=''
		try:
			user_id = user_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(user_id)))
		d += str(user_id)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
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
	
	def deleteUser_async(self,user_id,async,extra={}):
		# function index: 58
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 7
		m.opidx = 1
		m.extra.setStrDict(extra)
		d = '' 
		if type(user_id)==type(0) or type(user_id) == type(0.1): user_id=str(user_id)
		if not user_id: user_id=''
		try:
			user_id = user_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(user_id)))
		d += str(user_id)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		m.async = async
		m.asyncparser = ICtrlServerPrx.deleteUser_asyncparser
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def deleteUser_asyncparser(m,m2):
		# function index: 58 , m2 - callreturn msg.
		
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
	def dispatchGWA(self,fromtype,timeout=0,extra={}):
		# function index: 58
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 7
		m.opidx = 2
		m.extra.setStrDict(extra)
		d = '' 
		if type(fromtype)==type(0) or type(fromtype) == type(0.1): fromtype=str(fromtype)
		if not fromtype: fromtype=''
		try:
			fromtype = fromtype.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(fromtype)))
		d += str(fromtype)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
		idx = 0
		d = m.paramstream
		p = None
		r = False
		try:
			p =[]
			container = ServiceURIList_t(p)
			r,idx = container.unmarshall(d,idx)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_UNSERIALIZE_FAILED)
		return p
	
	def dispatchGWA_async(self,fromtype,async,extra={}):
		# function index: 58
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 7
		m.opidx = 2
		m.extra.setStrDict(extra)
		d = '' 
		if type(fromtype)==type(0) or type(fromtype) == type(0.1): fromtype=str(fromtype)
		if not fromtype: fromtype=''
		try:
			fromtype = fromtype.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(fromtype)))
		d += str(fromtype)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		m.async = async
		m.asyncparser = ICtrlServerPrx.dispatchGWA_asyncparser
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def dispatchGWA_asyncparser(m,m2):
		# function index: 58 , m2 - callreturn msg.
		
		stream = m2.paramstream
		user = m.async
		prx = m.prx
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC: return 
		try:
			idx = 0
			d = stream
			r = True
			p =[]
			container = ServiceURIList_t(p)
			r,idx = container.unmarshall(d,idx)
			if r:
				user(p,prx)
		except:
			traceback.print_exc()
		
	
	#extra must be map<string,string>
	def dispatchTalkingServer(self,timeout=0,extra={}):
		# function index: 58
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 7
		m.opidx = 3
		m.extra.setStrDict(extra)
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
		idx = 0
		d = m.paramstream
		p = None
		r = False
		try:
			p =[]
			container = ServiceURIList_t(p)
			r,idx = container.unmarshall(d,idx)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_UNSERIALIZE_FAILED)
		return p
	
	def dispatchTalkingServer_async(self,async,extra={}):
		# function index: 58
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 7
		m.opidx = 3
		m.extra.setStrDict(extra)
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		m.async = async
		m.asyncparser = ICtrlServerPrx.dispatchTalkingServer_asyncparser
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def dispatchTalkingServer_asyncparser(m,m2):
		# function index: 58 , m2 - callreturn msg.
		
		stream = m2.paramstream
		user = m.async
		prx = m.prx
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC: return 
		try:
			idx = 0
			d = stream
			r = True
			p =[]
			container = ServiceURIList_t(p)
			r,idx = container.unmarshall(d,idx)
			if r:
				user(p,prx)
		except:
			traceback.print_exc()
		
	

class IServiceEventListener:
	# -- INTERFACE -- 
	def __init__(self):
		self.delegatecls = IServiceEventListener_delegate
	
	def serviceStartup(self,svcid,ctx):
		pass
	
	def serviceShutdown(self,svcid,ctx):
		pass
	

class IServiceEventListener_delegate:
	def __init__(self,inst,adapter,conn=None):
		self.index = 8
		self.optlist={}
		self.id = '' 
		self.adapter = adapter
		self.optlist[0] = (self.serviceStartup)
		self.optlist[1] = (self.serviceShutdown)
		
		self.inst = inst
	
	def serviceStartup(self,ctx):
		print "callin (serviceStartup)"
		d = ctx.msg.paramstream 
		idx = 0
		_p_svcid, = struct.unpack('!i',d[idx:idx+4])
		idx+=4
		cr = None
		self.inst.serviceStartup(_p_svcid,ctx)
		return True
	
	def serviceShutdown(self,ctx):
		print "callin (serviceShutdown)"
		d = ctx.msg.paramstream 
		idx = 0
		_p_svcid, = struct.unpack('!i',d[idx:idx+4])
		idx+=4
		cr = None
		self.inst.serviceShutdown(_p_svcid,ctx)
		return True
	
	
class IServiceEventListenerPrx:
	# -- INTERFACE PROXY -- 
	def __init__(self,conn):
		self.conn = conn
		self.delta = None
		pass
	
	@staticmethod
	def create(pdest,try_connect=False):
		conn = tce.RpcConnection(pdest=pdest)
		proxy = IServiceEventListenerPrx(conn)
		return proxy
	
	@staticmethod
	def createWithMQ(name):
		ep = tce.RpcMqSet.instance().server.findEndPointByName(name)
		if not ep: return None
		conn = ep.impl
		proxy = IServiceEventListenerPrx(conn)
		return proxy
	
	#extra must be map<string,string>
	def serviceStartup(self,svcid,timeout=0,extra={}):
		# function index: 59
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 8
		m.opidx = 0
		m.extra.setStrDict(extra)
		d = '' 
		d += struct.pack('!i',svcid)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def serviceStartup_oneway(self,svcid,extra={}):
		# function index: 59
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 8
			m.opidx = 0
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcMqSet.instance().server.getId()
			m.extra.setStrDict(extra)
			d = '' 
			d += struct.pack('!i',svcid)
			m.paramstream+=d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	#extra must be map<string,string>
	def serviceShutdown(self,svcid,timeout=0,extra={}):
		# function index: 59
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 8
		m.opidx = 1
		m.extra.setStrDict(extra)
		d = '' 
		d += struct.pack('!i',svcid)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def serviceShutdown_oneway(self,svcid,extra={}):
		# function index: 59
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 8
			m.opidx = 1
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcMqSet.instance().server.getId()
			m.extra.setStrDict(extra)
			d = '' 
			d += struct.pack('!i',svcid)
			m.paramstream+=d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	

class IUserEventListener:
	# -- INTERFACE -- 
	def __init__(self):
		self.delegatecls = IUserEventListener_delegate
	
	def onUserExitTeam(self,userid,teamid,ctx):
		pass
	
	def onUserIntoTeam(self,userid,teamid,ctx):
		pass
	
	def onUserOnline(self,userid,gwdid,ctx):
		pass
	
	def onUserOffline(self,userid,gwdid,ctx):
		pass
	

class IUserEventListener_delegate:
	def __init__(self,inst,adapter,conn=None):
		self.index = 9
		self.optlist={}
		self.id = '' 
		self.adapter = adapter
		self.optlist[0] = (self.onUserExitTeam)
		self.optlist[1] = (self.onUserIntoTeam)
		self.optlist[2] = (self.onUserOnline)
		self.optlist[3] = (self.onUserOffline)
		
		self.inst = inst
	
	def onUserExitTeam(self,ctx):
		print "callin (onUserExitTeam)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_userid = d[idx:idx+size]
		idx+=size
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_teamid = d[idx:idx+size]
		idx+=size
		cr = None
		self.inst.onUserExitTeam(_p_userid,_p_teamid,ctx)
		return True
	
	def onUserIntoTeam(self,ctx):
		print "callin (onUserIntoTeam)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_userid = d[idx:idx+size]
		idx+=size
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_teamid = d[idx:idx+size]
		idx+=size
		cr = None
		self.inst.onUserIntoTeam(_p_userid,_p_teamid,ctx)
		return True
	
	def onUserOnline(self,ctx):
		print "callin (onUserOnline)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_userid = d[idx:idx+size]
		idx+=size
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_gwdid = d[idx:idx+size]
		idx+=size
		cr = None
		self.inst.onUserOnline(_p_userid,_p_gwdid,ctx)
		return True
	
	def onUserOffline(self,ctx):
		print "callin (onUserOffline)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_userid = d[idx:idx+size]
		idx+=size
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_gwdid = d[idx:idx+size]
		idx+=size
		cr = None
		self.inst.onUserOffline(_p_userid,_p_gwdid,ctx)
		return True
	
	
class IUserEventListenerPrx:
	# -- INTERFACE PROXY -- 
	def __init__(self,conn):
		self.conn = conn
		self.delta = None
		pass
	
	@staticmethod
	def create(pdest,try_connect=False):
		conn = tce.RpcConnection(pdest=pdest)
		proxy = IUserEventListenerPrx(conn)
		return proxy
	
	@staticmethod
	def createWithMQ(name):
		ep = tce.RpcMqSet.instance().server.findEndPointByName(name)
		if not ep: return None
		conn = ep.impl
		proxy = IUserEventListenerPrx(conn)
		return proxy
	
	#extra must be map<string,string>
	def onUserExitTeam(self,userid,teamid,timeout=0,extra={}):
		# function index: 60
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 9
		m.opidx = 0
		m.extra.setStrDict(extra)
		d = '' 
		if type(userid)==type(0) or type(userid) == type(0.1): userid=str(userid)
		if not userid: userid=''
		try:
			userid = userid.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(userid)))
		d += str(userid)
		m.paramstream+=d
		d = '' 
		if type(teamid)==type(0) or type(teamid) == type(0.1): teamid=str(teamid)
		if not teamid: teamid=''
		try:
			teamid = teamid.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(teamid)))
		d += str(teamid)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def onUserExitTeam_oneway(self,userid,teamid,extra={}):
		# function index: 60
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 9
			m.opidx = 0
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcMqSet.instance().server.getId()
			m.extra.setStrDict(extra)
			d = '' 
			if type(userid)==type(0) or type(userid) == type(0.1): userid=str(userid)
			if not userid: userid=''
			try:
				userid = userid.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(userid)))
			d += str(userid)
			m.paramstream+=d
			d = '' 
			if type(teamid)==type(0) or type(teamid) == type(0.1): teamid=str(teamid)
			if not teamid: teamid=''
			try:
				teamid = teamid.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(teamid)))
			d += str(teamid)
			m.paramstream+=d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	#extra must be map<string,string>
	def onUserIntoTeam(self,userid,teamid,timeout=0,extra={}):
		# function index: 60
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 9
		m.opidx = 1
		m.extra.setStrDict(extra)
		d = '' 
		if type(userid)==type(0) or type(userid) == type(0.1): userid=str(userid)
		if not userid: userid=''
		try:
			userid = userid.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(userid)))
		d += str(userid)
		m.paramstream+=d
		d = '' 
		if type(teamid)==type(0) or type(teamid) == type(0.1): teamid=str(teamid)
		if not teamid: teamid=''
		try:
			teamid = teamid.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(teamid)))
		d += str(teamid)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def onUserIntoTeam_oneway(self,userid,teamid,extra={}):
		# function index: 60
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 9
			m.opidx = 1
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcMqSet.instance().server.getId()
			m.extra.setStrDict(extra)
			d = '' 
			if type(userid)==type(0) or type(userid) == type(0.1): userid=str(userid)
			if not userid: userid=''
			try:
				userid = userid.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(userid)))
			d += str(userid)
			m.paramstream+=d
			d = '' 
			if type(teamid)==type(0) or type(teamid) == type(0.1): teamid=str(teamid)
			if not teamid: teamid=''
			try:
				teamid = teamid.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(teamid)))
			d += str(teamid)
			m.paramstream+=d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	#extra must be map<string,string>
	def onUserOnline(self,userid,gwdid,timeout=0,extra={}):
		# function index: 60
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 9
		m.opidx = 2
		m.extra.setStrDict(extra)
		d = '' 
		if type(userid)==type(0) or type(userid) == type(0.1): userid=str(userid)
		if not userid: userid=''
		try:
			userid = userid.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(userid)))
		d += str(userid)
		m.paramstream+=d
		d = '' 
		if type(gwdid)==type(0) or type(gwdid) == type(0.1): gwdid=str(gwdid)
		if not gwdid: gwdid=''
		try:
			gwdid = gwdid.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(gwdid)))
		d += str(gwdid)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def onUserOnline_oneway(self,userid,gwdid,extra={}):
		# function index: 60
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 9
			m.opidx = 2
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcMqSet.instance().server.getId()
			m.extra.setStrDict(extra)
			d = '' 
			if type(userid)==type(0) or type(userid) == type(0.1): userid=str(userid)
			if not userid: userid=''
			try:
				userid = userid.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(userid)))
			d += str(userid)
			m.paramstream+=d
			d = '' 
			if type(gwdid)==type(0) or type(gwdid) == type(0.1): gwdid=str(gwdid)
			if not gwdid: gwdid=''
			try:
				gwdid = gwdid.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(gwdid)))
			d += str(gwdid)
			m.paramstream+=d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	#extra must be map<string,string>
	def onUserOffline(self,userid,gwdid,timeout=0,extra={}):
		# function index: 60
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 9
		m.opidx = 3
		m.extra.setStrDict(extra)
		d = '' 
		if type(userid)==type(0) or type(userid) == type(0.1): userid=str(userid)
		if not userid: userid=''
		try:
			userid = userid.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(userid)))
		d += str(userid)
		m.paramstream+=d
		d = '' 
		if type(gwdid)==type(0) or type(gwdid) == type(0.1): gwdid=str(gwdid)
		if not gwdid: gwdid=''
		try:
			gwdid = gwdid.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(gwdid)))
		d += str(gwdid)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def onUserOffline_oneway(self,userid,gwdid,extra={}):
		# function index: 60
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 9
			m.opidx = 3
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcMqSet.instance().server.getId()
			m.extra.setStrDict(extra)
			d = '' 
			if type(userid)==type(0) or type(userid) == type(0.1): userid=str(userid)
			if not userid: userid=''
			try:
				userid = userid.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(userid)))
			d += str(userid)
			m.paramstream+=d
			d = '' 
			if type(gwdid)==type(0) or type(gwdid) == type(0.1): gwdid=str(gwdid)
			if not gwdid: gwdid=''
			try:
				gwdid = gwdid.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(gwdid)))
			d += str(gwdid)
			m.paramstream+=d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	

class TalkingCreateInfo_t:
# -- STRUCT -- 
	def __init__(self,type=0,delta=0):
		self.type = type
		self.delta = delta
		
	def __str__(self):
		return 'OBJECT<TalkingCreateInfo_t :%s> { type:%s,delta:%s}'%(hex(id(self)),str(self.type),str(self.delta) ) 
		
	def marshall(self):
		d =''
		d += struct.pack('!i',self.type)
		d += struct.pack('!i',self.delta)
		return d
		
	def unmarshall(self,d,idx_=0):
		idx = idx_
		try:
			self.type, = struct.unpack('!i',d[idx:idx+4])
			idx+=4
			self.delta, = struct.unpack('!i',d[idx:idx+4])
			idx+=4
		except:
			traceback.print_exc()
			return False,idx
		return True,idx
		

class TalkingMedia_t:
# -- STRUCT -- 
	def __init__(self,type=0,bytes='',timestamp=0):
		self.type = type
		self.bytes = bytes
		self.timestamp = timestamp
		
	def __str__(self):
		return 'OBJECT<TalkingMedia_t :%s> { type:%s,bytes:%s,timestamp:%s}'%(hex(id(self)),str(self.type),str(self.bytes),str(self.timestamp) ) 
		
	def marshall(self):
		d =''
		d += struct.pack('!i',self.type)
		container = StreamData_t(self.bytes)
		d += container.marshall()
		d += struct.pack('!i',self.timestamp)
		return d
		
	def unmarshall(self,d,idx_=0):
		idx = idx_
		try:
			self.type, = struct.unpack('!i',d[idx:idx+4])
			idx+=4
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.bytes = d[idx:idx+size]
			idx+=size
			self.timestamp, = struct.unpack('!i',d[idx:idx+4])
			idx+=4
		except:
			traceback.print_exc()
			return False,idx
		return True,idx
		

class ITalkingServer:
	# -- INTERFACE -- 
	def __init__(self):
		self.delegatecls = ITalkingServer_delegate
	
	def createTalking(self,info,ctx):
		return CallReturn_t()
	def closeTalking(self,talking_id,ctx):
		pass
	
	def exitTalking(self,talking_id,ctx):
		pass
	
	def joinTalking(self,talking_id,ctx):
		return CallReturn_t()
	def heartbeat(self,talking_id,ctx):
		pass
	
	def post(self,talking_id,media,ctx):
		pass
	

class ITalkingServer_delegate:
	def __init__(self,inst,adapter,conn=None):
		self.index = 10
		self.optlist={}
		self.id = '' 
		self.adapter = adapter
		self.optlist[0] = (self.createTalking)
		self.optlist[1] = (self.closeTalking)
		self.optlist[2] = (self.exitTalking)
		self.optlist[3] = (self.joinTalking)
		self.optlist[4] = (self.heartbeat)
		self.optlist[5] = (self.post)
		
		self.inst = inst
	
	def createTalking(self,ctx):
		print "callin (createTalking)"
		d = ctx.msg.paramstream 
		idx = 0
		_p_info = TalkingCreateInfo_t()
		r,idx = _p_info.unmarshall(d,idx)
		if not r: return False
		cr = None
		cr = self.inst.createTalking(_p_info,ctx)
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
	
	def closeTalking(self,ctx):
		print "callin (closeTalking)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_talking_id = d[idx:idx+size]
		idx+=size
		cr = None
		self.inst.closeTalking(_p_talking_id,ctx)
		return True
	
	def exitTalking(self,ctx):
		print "callin (exitTalking)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_talking_id = d[idx:idx+size]
		idx+=size
		cr = None
		self.inst.exitTalking(_p_talking_id,ctx)
		return True
	
	def joinTalking(self,ctx):
		print "callin (joinTalking)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_talking_id = d[idx:idx+size]
		idx+=size
		cr = None
		cr = self.inst.joinTalking(_p_talking_id,ctx)
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
	
	def heartbeat(self,ctx):
		print "callin (heartbeat)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_talking_id = d[idx:idx+size]
		idx+=size
		cr = None
		self.inst.heartbeat(_p_talking_id,ctx)
		return True
	
	def post(self,ctx):
		print "callin (post)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_talking_id = d[idx:idx+size]
		idx+=size
		_p_media = TalkingMedia_t()
		r,idx = _p_media.unmarshall(d,idx)
		if not r: return False
		cr = None
		self.inst.post(_p_talking_id,_p_media,ctx)
		return True
	
	
class ITalkingServerPrx:
	# -- INTERFACE PROXY -- 
	def __init__(self,conn):
		self.conn = conn
		self.delta = None
		pass
	
	@staticmethod
	def create(pdest,try_connect=False):
		conn = tce.RpcConnection(pdest=pdest)
		proxy = ITalkingServerPrx(conn)
		return proxy
	
	@staticmethod
	def createWithMQ(name):
		ep = tce.RpcMqSet.instance().server.findEndPointByName(name)
		if not ep: return None
		conn = ep.impl
		proxy = ITalkingServerPrx(conn)
		return proxy
	
	#extra must be map<string,string>
	def createTalking(self,info,timeout=0,extra={}):
		# function index: 63
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 10
		m.opidx = 0
		m.extra.setStrDict(extra)
		d = '' 
		d += info.marshall()
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
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
	
	def createTalking_async(self,info,async,extra={}):
		# function index: 63
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 10
		m.opidx = 0
		m.extra.setStrDict(extra)
		d = '' 
		d += info.marshall()
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		m.async = async
		m.asyncparser = ITalkingServerPrx.createTalking_asyncparser
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def createTalking_asyncparser(m,m2):
		# function index: 63 , m2 - callreturn msg.
		
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
	def closeTalking(self,talking_id,timeout=0,extra={}):
		# function index: 63
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 10
		m.opidx = 1
		m.extra.setStrDict(extra)
		d = '' 
		if type(talking_id)==type(0) or type(talking_id) == type(0.1): talking_id=str(talking_id)
		if not talking_id: talking_id=''
		try:
			talking_id = talking_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(talking_id)))
		d += str(talking_id)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def closeTalking_oneway(self,talking_id,extra={}):
		# function index: 63
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 10
			m.opidx = 1
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcMqSet.instance().server.getId()
			m.extra.setStrDict(extra)
			d = '' 
			if type(talking_id)==type(0) or type(talking_id) == type(0.1): talking_id=str(talking_id)
			if not talking_id: talking_id=''
			try:
				talking_id = talking_id.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(talking_id)))
			d += str(talking_id)
			m.paramstream+=d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	#extra must be map<string,string>
	def exitTalking(self,talking_id,timeout=0,extra={}):
		# function index: 63
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 10
		m.opidx = 2
		m.extra.setStrDict(extra)
		d = '' 
		if type(talking_id)==type(0) or type(talking_id) == type(0.1): talking_id=str(talking_id)
		if not talking_id: talking_id=''
		try:
			talking_id = talking_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(talking_id)))
		d += str(talking_id)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def exitTalking_oneway(self,talking_id,extra={}):
		# function index: 63
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 10
			m.opidx = 2
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcMqSet.instance().server.getId()
			m.extra.setStrDict(extra)
			d = '' 
			if type(talking_id)==type(0) or type(talking_id) == type(0.1): talking_id=str(talking_id)
			if not talking_id: talking_id=''
			try:
				talking_id = talking_id.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(talking_id)))
			d += str(talking_id)
			m.paramstream+=d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	#extra must be map<string,string>
	def joinTalking(self,talking_id,timeout=0,extra={}):
		# function index: 63
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 10
		m.opidx = 3
		m.extra.setStrDict(extra)
		d = '' 
		if type(talking_id)==type(0) or type(talking_id) == type(0.1): talking_id=str(talking_id)
		if not talking_id: talking_id=''
		try:
			talking_id = talking_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(talking_id)))
		d += str(talking_id)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
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
	
	def joinTalking_async(self,talking_id,async,extra={}):
		# function index: 63
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 10
		m.opidx = 3
		m.extra.setStrDict(extra)
		d = '' 
		if type(talking_id)==type(0) or type(talking_id) == type(0.1): talking_id=str(talking_id)
		if not talking_id: talking_id=''
		try:
			talking_id = talking_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(talking_id)))
		d += str(talking_id)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		m.async = async
		m.asyncparser = ITalkingServerPrx.joinTalking_asyncparser
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def joinTalking_asyncparser(m,m2):
		# function index: 63 , m2 - callreturn msg.
		
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
	def heartbeat(self,talking_id,timeout=0,extra={}):
		# function index: 63
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 10
		m.opidx = 4
		m.extra.setStrDict(extra)
		d = '' 
		if type(talking_id)==type(0) or type(talking_id) == type(0.1): talking_id=str(talking_id)
		if not talking_id: talking_id=''
		try:
			talking_id = talking_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(talking_id)))
		d += str(talking_id)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def heartbeat_oneway(self,talking_id,extra={}):
		# function index: 63
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 10
			m.opidx = 4
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcMqSet.instance().server.getId()
			m.extra.setStrDict(extra)
			d = '' 
			if type(talking_id)==type(0) or type(talking_id) == type(0.1): talking_id=str(talking_id)
			if not talking_id: talking_id=''
			try:
				talking_id = talking_id.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(talking_id)))
			d += str(talking_id)
			m.paramstream+=d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	#extra must be map<string,string>
	def post(self,talking_id,media,timeout=0,extra={}):
		# function index: 63
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 10
		m.opidx = 5
		m.extra.setStrDict(extra)
		d = '' 
		if type(talking_id)==type(0) or type(talking_id) == type(0.1): talking_id=str(talking_id)
		if not talking_id: talking_id=''
		try:
			talking_id = talking_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(talking_id)))
		d += str(talking_id)
		m.paramstream+=d
		d = '' 
		d += media.marshall()
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def post_oneway(self,talking_id,media,extra={}):
		# function index: 63
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 10
			m.opidx = 5
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcMqSet.instance().server.getId()
			m.extra.setStrDict(extra)
			d = '' 
			if type(talking_id)==type(0) or type(talking_id) == type(0.1): talking_id=str(talking_id)
			if not talking_id: talking_id=''
			try:
				talking_id = talking_id.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(talking_id)))
			d += str(talking_id)
			m.paramstream+=d
			d = '' 
			d += media.marshall()
			m.paramstream+=d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	

class ITalkingClient:
	# -- INTERFACE -- 
	def __init__(self):
		self.delegatecls = ITalkingClient_delegate
	
	def onData(self,talking_id,media,ctx):
		pass
	
	def onClose(self,talking_id,ctx):
		pass
	

class ITalkingClient_delegate:
	def __init__(self,inst,adapter,conn=None):
		self.index = 11
		self.optlist={}
		self.id = '' 
		self.adapter = adapter
		self.optlist[0] = (self.onData)
		self.optlist[1] = (self.onClose)
		
		self.inst = inst
	
	def onData(self,ctx):
		print "callin (onData)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_talking_id = d[idx:idx+size]
		idx+=size
		_p_media = TalkingMedia_t()
		r,idx = _p_media.unmarshall(d,idx)
		if not r: return False
		cr = None
		self.inst.onData(_p_talking_id,_p_media,ctx)
		return True
	
	def onClose(self,ctx):
		print "callin (onClose)"
		d = ctx.msg.paramstream 
		idx = 0
		size, = struct.unpack('!I',d[idx:idx+4])
		idx+=4
		_p_talking_id = d[idx:idx+size]
		idx+=size
		cr = None
		self.inst.onClose(_p_talking_id,ctx)
		return True
	
	
class ITalkingClientPrx:
	# -- INTERFACE PROXY -- 
	def __init__(self,conn):
		self.conn = conn
		self.delta = None
		pass
	
	@staticmethod
	def create(pdest,try_connect=False):
		conn = tce.RpcConnection(pdest=pdest)
		proxy = ITalkingClientPrx(conn)
		return proxy
	
	@staticmethod
	def createWithMQ(name):
		ep = tce.RpcMqSet.instance().server.findEndPointByName(name)
		if not ep: return None
		conn = ep.impl
		proxy = ITalkingClientPrx(conn)
		return proxy
	
	#extra must be map<string,string>
	def onData(self,talking_id,media,timeout=0,extra={}):
		# function index: 64
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 11
		m.opidx = 0
		m.extra.setStrDict(extra)
		d = '' 
		if type(talking_id)==type(0) or type(talking_id) == type(0.1): talking_id=str(talking_id)
		if not talking_id: talking_id=''
		try:
			talking_id = talking_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(talking_id)))
		d += str(talking_id)
		m.paramstream+=d
		d = '' 
		d += media.marshall()
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def onData_oneway(self,talking_id,media,extra={}):
		# function index: 64
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 11
			m.opidx = 0
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcMqSet.instance().server.getId()
			m.extra.setStrDict(extra)
			d = '' 
			if type(talking_id)==type(0) or type(talking_id) == type(0.1): talking_id=str(talking_id)
			if not talking_id: talking_id=''
			try:
				talking_id = talking_id.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(talking_id)))
			d += str(talking_id)
			m.paramstream+=d
			d = '' 
			d += media.marshall()
			m.paramstream+=d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	#extra must be map<string,string>
	def onClose(self,talking_id,timeout=0,extra={}):
		# function index: 64
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 11
		m.opidx = 1
		m.extra.setStrDict(extra)
		d = '' 
		if type(talking_id)==type(0) or type(talking_id) == type(0.1): talking_id=str(talking_id)
		if not talking_id: talking_id=''
		try:
			talking_id = talking_id.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(talking_id)))
		d += str(talking_id)
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
	
	def onClose_oneway(self,talking_id,extra={}):
		# function index: 64
		
		try:
			m = tce.RpcMessageCall()
			m.ifidx = 11
			m.opidx = 1
			m.calltype |= tce.RpcMessage.ONEWAY
			m.prx = self
			m.conn = m.prx.conn
			m.call_id = tce.RpcMqSet.instance().server.getId()
			m.extra.setStrDict(extra)
			d = '' 
			if type(talking_id)==type(0) or type(talking_id) == type(0.1): talking_id=str(talking_id)
			if not talking_id: talking_id=''
			try:
				talking_id = talking_id.encode('utf-8')
			except:pass
			d += struct.pack('!I', len(str(talking_id)))
			d += str(talking_id)
			m.paramstream+=d
			r = self.conn.sendMessage(m)
			if not r:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	

class tq_parameters_t:
# -- STRUCT -- 
	def __init__(self,license='',verifycode='',scope='',cookie='',engine=''):
		self.license = license
		self.verifycode = verifycode
		self.scope = scope
		self.cookie = cookie
		self.engine = engine
		
	def __str__(self):
		return 'OBJECT<tq_parameters_t :%s> { license:%s,verifycode:%s,scope:%s,cookie:%s,engine:%s}'%(hex(id(self)),str(self.license),str(self.verifycode),str(self.scope),str(self.cookie),str(self.engine) ) 
		
	def marshall(self):
		d =''
		if type(self.license)==type(0) or type(self.license) == type(0.1): self.license=str(self.license)
		if not self.license: self.license=''
		try:
			self.license = self.license.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.license)))
		d += str(self.license)
		if type(self.verifycode)==type(0) or type(self.verifycode) == type(0.1): self.verifycode=str(self.verifycode)
		if not self.verifycode: self.verifycode=''
		try:
			self.verifycode = self.verifycode.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.verifycode)))
		d += str(self.verifycode)
		if type(self.scope)==type(0) or type(self.scope) == type(0.1): self.scope=str(self.scope)
		if not self.scope: self.scope=''
		try:
			self.scope = self.scope.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.scope)))
		d += str(self.scope)
		if type(self.cookie)==type(0) or type(self.cookie) == type(0.1): self.cookie=str(self.cookie)
		if not self.cookie: self.cookie=''
		try:
			self.cookie = self.cookie.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.cookie)))
		d += str(self.cookie)
		if type(self.engine)==type(0) or type(self.engine) == type(0.1): self.engine=str(self.engine)
		if not self.engine: self.engine=''
		try:
			self.engine = self.engine.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.engine)))
		d += str(self.engine)
		return d
		
	def unmarshall(self,d,idx_=0):
		idx = idx_
		try:
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.license = d[idx:idx+size]
			idx+=size
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.verifycode = d[idx:idx+size]
			idx+=size
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.scope = d[idx:idx+size]
			idx+=size
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.cookie = d[idx:idx+size]
			idx+=size
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.engine = d[idx:idx+size]
			idx+=size
		except:
			traceback.print_exc()
			return False,idx
		return True,idx
		

class tq_verifyinfo_t:
# -- STRUCT -- 
	def __init__(self,image=MimeImage_t(),cookie=''):
		self.image = image
		self.cookie = cookie
		
	def __str__(self):
		return 'OBJECT<tq_verifyinfo_t :%s> { image:%s,cookie:%s}'%(hex(id(self)),str(self.image),str(self.cookie) ) 
		
	def marshall(self):
		d =''
		d += self.image.marshall()
		if type(self.cookie)==type(0) or type(self.cookie) == type(0.1): self.cookie=str(self.cookie)
		if not self.cookie: self.cookie=''
		try:
			self.cookie = self.cookie.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.cookie)))
		d += str(self.cookie)
		return d
		
	def unmarshall(self,d,idx_=0):
		idx = idx_
		try:
			r,idx = self.image.unmarshall(d,idx)
			if not r: return False,idx
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.cookie = d[idx:idx+size]
			idx+=size
		except:
			traceback.print_exc()
			return False,idx
		return True,idx
		

class tq_record_t:
# -- STRUCT -- 
	def __init__(self,time='',license='',number='',rule='',department='',position='',content='',status=''):
		self.time = time
		self.license = license
		self.number = number
		self.rule = rule
		self.department = department
		self.position = position
		self.content = content
		self.status = status
		
	def __str__(self):
		return 'OBJECT<tq_record_t :%s> { time:%s,license:%s,number:%s,rule:%s,department:%s,position:%s,content:%s,status:%s}'%(hex(id(self)),str(self.time),str(self.license),str(self.number),str(self.rule),str(self.department),str(self.position),str(self.content),str(self.status) ) 
		
	def marshall(self):
		d =''
		if type(self.time)==type(0) or type(self.time) == type(0.1): self.time=str(self.time)
		if not self.time: self.time=''
		try:
			self.time = self.time.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.time)))
		d += str(self.time)
		if type(self.license)==type(0) or type(self.license) == type(0.1): self.license=str(self.license)
		if not self.license: self.license=''
		try:
			self.license = self.license.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.license)))
		d += str(self.license)
		if type(self.number)==type(0) or type(self.number) == type(0.1): self.number=str(self.number)
		if not self.number: self.number=''
		try:
			self.number = self.number.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.number)))
		d += str(self.number)
		if type(self.rule)==type(0) or type(self.rule) == type(0.1): self.rule=str(self.rule)
		if not self.rule: self.rule=''
		try:
			self.rule = self.rule.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.rule)))
		d += str(self.rule)
		if type(self.department)==type(0) or type(self.department) == type(0.1): self.department=str(self.department)
		if not self.department: self.department=''
		try:
			self.department = self.department.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.department)))
		d += str(self.department)
		if type(self.position)==type(0) or type(self.position) == type(0.1): self.position=str(self.position)
		if not self.position: self.position=''
		try:
			self.position = self.position.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.position)))
		d += str(self.position)
		if type(self.content)==type(0) or type(self.content) == type(0.1): self.content=str(self.content)
		if not self.content: self.content=''
		try:
			self.content = self.content.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.content)))
		d += str(self.content)
		if type(self.status)==type(0) or type(self.status) == type(0.1): self.status=str(self.status)
		if not self.status: self.status=''
		try:
			self.status = self.status.encode('utf-8')
		except:pass
		d += struct.pack('!I', len(str(self.status)))
		d += str(self.status)
		return d
		
	def unmarshall(self,d,idx_=0):
		idx = idx_
		try:
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.time = d[idx:idx+size]
			idx+=size
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.license = d[idx:idx+size]
			idx+=size
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.number = d[idx:idx+size]
			idx+=size
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.rule = d[idx:idx+size]
			idx+=size
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.department = d[idx:idx+size]
			idx+=size
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.position = d[idx:idx+size]
			idx+=size
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.content = d[idx:idx+size]
			idx+=size
			size, = struct.unpack('!I',d[idx:idx+4])
			idx+=4
			self.status = d[idx:idx+size]
			idx+=size
		except:
			traceback.print_exc()
			return False,idx
		return True,idx
		

class tq_record_list_t:
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
				o = tq_record_t()
				r,idx = o.unmarshall(d,idx)
				if not r: return False,idx
				self.ds.append(o)
				p+=1
		except:
			traceback.print_exc()
			return False,idx
		return True,idx

class tq_result_t:
# -- STRUCT -- 
	def __init__(self,error=Error_t(),next=tq_verifyinfo_t(),records=[]):
		self.error = error
		self.next = next
		self.records = records
		
	def __str__(self):
		return 'OBJECT<tq_result_t :%s> { error:%s,next:%s,records:%s}'%(hex(id(self)),str(self.error),str(self.next),str(self.records) ) 
		
	def marshall(self):
		d =''
		d += self.error.marshall()
		d += self.next.marshall()
		container = tq_record_list_t(self.records)
		d += container.marshall()
		return d
		
	def unmarshall(self,d,idx_=0):
		idx = idx_
		try:
			r,idx = self.error.unmarshall(d,idx)
			if not r: return False,idx
			r,idx = self.next.unmarshall(d,idx)
			if not r: return False,idx
			self.records = [ ]
			container = tq_record_list_t(self.records)
			r,idx = container.unmarshall(d,idx)
			if not r: return False,idx
		except:
			traceback.print_exc()
			return False,idx
		return True,idx
		

class IAppTrafficeQuery:
	# -- INTERFACE -- 
	def __init__(self):
		self.delegatecls = IAppTrafficeQuery_delegate
	
	def prepareQuery(self,ctx):
		return tq_verifyinfo_t()
	def doQuery(self,p_,ctx):
		return tq_result_t()

class IAppTrafficeQuery_delegate:
	def __init__(self,inst,adapter,conn=None):
		self.index = 12
		self.optlist={}
		self.id = '' 
		self.adapter = adapter
		self.optlist[0] = (self.prepareQuery)
		self.optlist[1] = (self.doQuery)
		
		self.inst = inst
	
	def prepareQuery(self,ctx):
		print "callin (prepareQuery)"
		d = ctx.msg.paramstream 
		idx = 0
		cr = None
		cr = self.inst.prepareQuery(ctx)
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
	
	def doQuery(self,ctx):
		print "callin (doQuery)"
		d = ctx.msg.paramstream 
		idx = 0
		_p_p_ = tq_parameters_t()
		r,idx = _p_p_.unmarshall(d,idx)
		if not r: return False
		cr = None
		cr = self.inst.doQuery(_p_p_,ctx)
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
	
	
class IAppTrafficeQueryPrx:
	# -- INTERFACE PROXY -- 
	def __init__(self,conn):
		self.conn = conn
		self.delta = None
		pass
	
	@staticmethod
	def create(pdest,try_connect=False):
		conn = tce.RpcConnection(pdest=pdest)
		proxy = IAppTrafficeQueryPrx(conn)
		return proxy
	
	@staticmethod
	def createWithMQ(name):
		ep = tce.RpcMqSet.instance().server.findEndPointByName(name)
		if not ep: return None
		conn = ep.impl
		proxy = IAppTrafficeQueryPrx(conn)
		return proxy
	
	#extra must be map<string,string>
	def prepareQuery(self,timeout=0,extra={}):
		# function index: 70
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 12
		m.opidx = 0
		m.extra.setStrDict(extra)
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
		idx = 0
		d = m.paramstream
		p = None
		r = False
		try:
			p = tq_verifyinfo_t()
			r,idx = p.unmarshall(d,idx)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_UNSERIALIZE_FAILED)
		return p
	
	def prepareQuery_async(self,async,extra={}):
		# function index: 70
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 12
		m.opidx = 0
		m.extra.setStrDict(extra)
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		m.async = async
		m.asyncparser = IAppTrafficeQueryPrx.prepareQuery_asyncparser
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def prepareQuery_asyncparser(m,m2):
		# function index: 70 , m2 - callreturn msg.
		
		stream = m2.paramstream
		user = m.async
		prx = m.prx
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC: return 
		try:
			idx = 0
			d = stream
			r = True
			p = tq_verifyinfo_t()
			r,idx = p.unmarshall(d,idx)
			if r:
				user(p,prx)
		except:
			traceback.print_exc()
		
	
	#extra must be map<string,string>
	def doQuery(self,p_,timeout=0,extra={}):
		# function index: 70
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 12
		m.opidx = 1
		m.extra.setStrDict(extra)
		d = '' 
		d += p_.marshall()
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		m2 = m.mtx.waitObject(timeout)
		if not m2:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m2.errcode)
		m = m2
		idx = 0
		d = m.paramstream
		p = None
		r = False
		try:
			p = tq_result_t()
			r,idx = p.unmarshall(d,idx)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_UNSERIALIZE_FAILED)
		return p
	
	def doQuery_async(self,p_,async,extra={}):
		# function index: 70
		
		ecode = tce.RpcConsts.RPCERROR_SUCC
		m = tce.RpcMessageCall()
		m.ifidx = 12
		m.opidx = 1
		m.extra.setStrDict(extra)
		d = '' 
		d += p_.marshall()
		m.paramstream+=d
		m.prx = self
		m.conn = m.prx.conn
		m.call_id = tce.RpcMqSet.instance().server.getId()
		m.async = async
		m.asyncparser = IAppTrafficeQueryPrx.doQuery_asyncparser
		r = self.conn.sendMessage(m)
		if not r:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def doQuery_asyncparser(m,m2):
		# function index: 70 , m2 - callreturn msg.
		
		stream = m2.paramstream
		user = m.async
		prx = m.prx
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC: return 
		try:
			idx = 0
			d = stream
			r = True
			p = tq_result_t()
			r,idx = p.unmarshall(d,idx)
			if r:
				user(p,prx)
		except:
			traceback.print_exc()
		
	

