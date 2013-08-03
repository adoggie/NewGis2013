# -- coding:utf-8 --

import socket,traceback,os,os.path,sys,time,struct,base64,gzip,array,json,zlib,threading
import datetime
import geotools
from xml.dom.minidom import  parseString as xmlParseString

def getmtime(file):
	try:
		return os.path.getmtime(file)
	except: return 0
	
def getfiledigest(file,bufsize=1024*5,type='md5'):
	import md5
	m = md5.new()
	try:
		fp = open(file,'rb')
		while True:
			data = fp.read(bufsize)
			if not data:break
			m.update(data)
	except:
		traceback.print_exc()
		return ''
	return m.hexdigest()
	
def setmtime(file,tick): # tick - unix timestamp 1970~
	os.utime(file,(tick,tick) )
	
def getdbsequence_pg(dbconn,seqname):
	seq = 0
	try:
		sql = "select nextval('%s')"%seqname
		cr = dbconn.cursor()
		cr.execute(sql)
		seq = cr.fetchone()[0]
	except:
		traceback.print_exc()
	return seq

getdbseq = getdbsequence_pg

def loadjson(file):
	d = None
	try:
		fd = open(file)
		cont = fd.read().strip()
		cont = cont.replace(' ','')
		cont = cont.replace('\'',"\"")
		cont = cont.replace('\t',"")
		cont = cont.replace('(',"[")
		cont = cont.replace(')',"]")
		#print cont
		fd.close()
		d = json.loads(cont)
	except:
		traceback.print_exc()	
		pass #
	
	return d

def loadjson_s(s):
	d = {}
	try:
		d = json.loads(s)
	except:
		pass
	return d



def waitForShutdown():
	while True:
		time.sleep(1*10000*10)

def genTempFileName():
	return str(time.time())

# unix timestamp to datetime.datetime	
def mk_datetime(timestamp):
	timestamp = int(timestamp)
	return datetime.datetime.fromtimestamp(timestamp)

def formatTimestamp(secs):
	try:
		dt = datetime.datetime.fromtimestamp(secs)
		return "%04d%02d%02d %02d:%02d:%02d"%(dt.year,dt.month,dt.day,dt.hour,dt.minute,dt.second)
	except:
		return ''

def formatDateTime(dt):
	if not dt:
		return ''
	return  "%04d%02d%02d %02d:%02d:%02d"%(dt.year,dt.month,dt.day,dt.hour,dt.minute,dt.second)

def formatDateTime_ymd(dt):
	if not dt:
		return ''
	return  "%04d%02d%02d"%(dt.year,dt.month,dt.day)

def formatDateTime_ymd2(dt):
	if not dt:
		return ''
	return  u"%04d年%02d月%02d日"%(dt.year,dt.month,dt.day)

def formatDateTime_ymdhm(dt):
	if not dt:
		return ''
	return  u"%04d年%02d月%02d日%02d时%02d分"%(dt.year,dt.month,dt.day,dt.hour,dt.minute)


def mk_timestamp(dt):
	return time.mktime(dt.timetuple())

def formatTimestamp2(secs):
	try:
		dt = datetime.datetime.fromtimestamp(secs)
		return "%04d.%02d.%02d %02d:%02d:%02d"%(dt.year,dt.month,dt.day,dt.hour,dt.minute,dt.second)
	except:
		return ''
	
#根据datetime产生timestamp	
def maketimestamp(dt):
	return time.mktime(dt.timetuple())

def touchfile(file):
	try:
		fp = open(file,'w')
		fp.close()
	except:
		return False
	return True

def getToDayStr():
	t = time.localtime()
	return "%04d%02d%02d"%(t.tm_year,t.tm_mon,t.tm_mday)


#这个class用于异步等待获取返回对象之用
class MutexObject:
	def __init__(self):
		self.mtx = threading.Condition()
		self.d = None
		
	def waitObject(self,timeout):
		d = None
		self.mtx.acquire()
		if self.d == None:
			self.mtx.wait(timeout)
			d = self.d
			self.d = None
		self.mtx.release()
		return d
		
	def notify(self,d):
		self.mtx.acquire()
		self.d = d
		self.mtx.notify()
		self.mtx.release()


class ThreadGroup:
	def __init__(self,action,threadnum=1):
		self.action = action
		self.num = threadnum
		self.threads=[]

	def start(self,p=None):
		for n in range(self.num):
			thread = threading.Thread(target=self.action,args=(p,))
			self.threads.append(thread)
			thread.start()

	def join(self):
		for thread in self.threads:
			thread.join()



#线程执行消息队列
class Thread_MQ:
	def __init__(self,action,threadnum=5,wait=0):
		self.action = action
		self.mtx = threading.Condition()
		self.threads=[]
		self.exiting=False
		self.q = []
		self.qremove =[]
		self.wait = wait

		for n in range(threadnum):
			t = threading.Thread(target=self.walk)
			t.start()

			
	def walk(self):
		while not self.exiting:
			m = None
			self.mtx.acquire()
			if self.q:
				m = self.q[0]
				del self.q[0]
			else:
				if self.wait:
					self.mtx.wait(wait)
				else:
					self.mtx.wait()
				if self.q:
					m = self.q[0]
					del self.q[0]
			self.mtx.release()
			if m:
				self.action(m)
			
	
	def queueIn(self,m):
		self.mtx.acquire()
		self.q.append(m)
		self.mtx.notifyAll()
		self.mtx.release()

class UniqueId:
	def __init__(self,init=0):
		self.init = init
		self.value = self.init
		self.mtx = threading.Lock()
		
	def inc(self):
		self.mtx.acquire()
		self.value+=1
		self.mtx.release()
		
	def dec(self):
		self.mtx.acquire()
		self.value-=1
		self.mtx.release()
	
	def next(self):
		self.inc()
		return self.value
	
def geo_rect2wktpolygon(rc):
	# rc - (x,y,w,h)
	x,y,w,h = rc
	return "POLYGON((%s %s,%s %s,%s %s,%s %s,%s %s))"%\
		(x,y,x+w,y,x+w,y+h,x,y+h,x,y)

def readImageTimes(imagefile,ffmpeg='ffmpeg.exe'):
	import re
	
	rst = () # (creattime,lastmodifytime) timestamp time ticks
	detail = os.popen3('%s -i %s'%(ffmpeg,imagefile) )[2].read()
	tt = re.findall('Duration: (\d{1,2}:\d{1,2}:\d{1,2}\.\d{0,4}),',detail,re.M)
	if tt:
		tt = tt[0]
	else:
		return ()
	h,m,s = map(int, map(float,tt.split(':')) )
	duration_secs =  int ( h*3600 + m * 60 + s)
	lastmodify = os.path.getmtime(imagefile)
	createsecs =  lastmodify - duration_secs
	return (int(createsecs),int(lastmodify))

def statevfs(path):
	import win32api
	import os.path
	path = os.path.normpath(path)
	if path[-1]=='\\':
		path = path[:-1]
	try:
		f,all,user = win32api.GetDiskFreeSpaceEx(path)
		return all,user
	except:return 0,0
	
def hashobject(obj):
	attrs = [s for  s in dir(obj) if not s.startswith('__')]
	kvs={}

	for k in attrs:
		#print 'sss:',k
		if k=='objects':continue
		if k.startswith('_'):continue
		o = getattr(obj, k)

		if unicode(o).find('django.db')!=-1:
			continue
		if callable(o):
			continue
		kvs[k] = o
	#kvs = {k:getattr(obj, k) for k in attrs}
	return kvs

MB_SIZE = 1024.*1024.
def formatfilesize(size):
	mb = round(size/MB_SIZE,3)
	return mb

#判别pt点是否落在多边形内
def isPtInRect(pt,rc):
	x,y = pt
	x1,y1,x2,y2 = rc
	if x>=x1 and x<=x2 and y>=y1 and y<=y2:
		return True
	return False


def initdb_pg(db):
	import psycopg2 as pg2
	try:
		dbconn = pg2.connect(host=db['host'],
							database=db['name'],
							port=db['port'],
							user=db['user'],
							password=db['passwd'])
		return dbconn
	except:
		
		traceback.print_exc()
		return None

def serial_jsonzlib(obj):
	"""
	数据对象json编码并压缩
	"""
	d = json.dumps(obj)
	d = zlib.compress(d)
	return d


def trim_hms(dt):
	"""
	获取ymd，不包含hms (000)
	"""
	d = datetime.datetime(dt.year,dt.month,dt.day)
	return d

def localtime(dt,tzoff=8):
	"""
	获取加上指定时区差的时间对象
	"""
	return dt+datetime.timedelta(hours=tzoff)

def normalize_querytime2(start,end):
	"""

	"""
	if not start:
		start = datetime.datetime(2000,1,1)
	else:
		start = localtime(start)
	if not end:
		end = datetime.datetime.now()
	else:
		end = localtime(end) + datetime.timedelta(days=1)
	return start,end

def add_index(rs):
	c=1
	for r in rs:
		r['idx'] = c
		c+=1

def between(p,p1,p2):
	return p>=p1 and p<=p2

def inet_aton(ip):
	net = socket.inet_aton( ip )
	return struct.unpack('!I',net)[0]

def inet_ntoa(net):
	return socket.inet_ntoa( struct.pack('!I',net))

class TT:
	def __init__(self):
		self.name='abc'

	def test(self):
		pass


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

def app_init(name):
	if not os.path.exists('/var/run/newgis'):
		os.mkdir('/var/run/newgis')
	f = open('/var/run/newgis/%s'%name,'w')
	f.write( str(os.getpid()))
	f.close()


def app_kill(name):
	lock = '/var/run/newgis/%s'%name
	if not os.path.exists(lock):
		return
	f = open(lock)
	pid = f.readline().strip()
	cmd = 'kill -9 %s'%pid
	os.system(cmd)


if __name__=='__main__':
	#print loadjson('node.txt')
	#print statevfs('d:/temp4/')
	#print getfiledigest('D:/test_dvr_data/stosync/file0014.trp')
	print hashobject(TT())
	pass