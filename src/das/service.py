# -- coding:utf-8 --

import socket,traceback,os,os.path,sys,time,struct,base64,gzip,array,threading
import select

import codec
import utils


from gevent.server import StreamServer
from gevent.event import Event

'''
dtu设备通过gprs通信产生问题：
１.dtu连接进入，数据传输几次，dtu端断开，但服务器未收到断开信号，随后dtu再次建立与server的连接
 有时同一个dtu会与服务器同时建立多个连接，随后等待很长时间在select时检测到某些个socket无效，产生异常

'''
class DeviceConnectionUrl:
	#设备连接地址描述信息
	def __init__(self,host,port,proto='tcp'):
		self.host=host
		self.port=port
		self.proto = proto # tcp,udp,rs232
	
	def __str__(self):
		return "%s:%s:%s"%(self.proto,self.host,self.port)

class DeviceConnection_Base:
	uid = utils.UniqueId()
	def __init__(self,url=None):
		self.url = url
		self.aom = None #ActiveObject module
		self.codec = None		 
#		self.handle = None #通信句柄
		self.sock = None
		self.mid = ''	#模块编号
		self.delta = None
		self.mtx = threading.Lock()
		self.id = DeviceConnection_Base.uid.next()	#连接id
		
		#2011.6.13 对于有些设备连接上来时候进行注册设备编号，而不用在
		#后续的消息包中每次携带设备编号
	def close(self):
		self.sock.close()
		self.sock = None
		
	def write(self,bytes):
		try:
			self.sock.send(bytes)
			return True
		except:
			traceback.print_exc()
			return False
	
	def read(self):
		#某些情况将从连接中直接读取 
		pass
	
	def setCodec(self,codec):
		self.codec = codec

class DeviceEvent:
	CONNECTED = 1
	DISCONNECTED = 3
	RECVED_DATA = 2
	SENT_DATA = 4
	INCOMMING_CONNECTED = 5
	UNDEFINED = 0xff
	def __init__(self):
		self.data = None #具体事件数据内容 ActiveObject_Data
		self.type = DeviceEvent.UNDEFINED
		#self.source = None #事件源对象
		self.conn = None #设备连接对象,tcp socket
		self.accept = True



	def newline(self,url,codec=codec.MediaCodec_Null,async= False):
		pass
		
class DaemonService_Tcp:
	''' 连接进入将自动产生DeviceConnection_Tcp对象，并以 DeviceData_Event传递给接收者(sink),sink必须设置对应的解码器
		每个Service绑定一个服务端口，且此service只允许一种数据解码器
	 '''
	def __init__(self,app,addr,event,codecCLS=codec.MediaCodec_Null,connCLS=DeviceConnection_Base):
		#@param addr - (host,port)
		#   event - 消息接收函数
		#   codeCLS - 解码器类
		#   connCLS - 连接类 DeviceConnection_Tcp的子类

		self.app = app
		self.connCLS = connCLS
		self.codecCLS = codecCLS
		self.event = event #接收事件
		self.addr = addr
		self.mtxsocks= threading.Lock()
#		self.exc_mq = utils.Thread_MQ(self.thread_decode,1)
		self.start()

	def start(self):
		self.server = StreamServer(self.addr, self._service)
		self.server.start() #serve_forever()
		print 'socket server started!'


#	'''
#	问题: dtu的连接丢失之后平台服务器无法通过select获取断开事件，但是dtu在gprs网络
#		已经断开，然后dtu再次建立与服务器连接；但之前建立的那个socket连接再后续select
#		的时候会抛出异常，所以本来是多fdset一次进行select，先必须改成对每个fd进行select
#		检测，并加上timeout字段
#	'''
	def _service(self,sock,address):
		print ' new client socket come in :',str(address)
		e = DeviceEvent()
		e.type = DeviceEvent.INCOMMING_CONNECTED
		e.conn = self.connCLS(self)
		e.conn.codec = self.codecCLS(self)
		e.conn.codec.conn = e.conn
		e.conn.sock = sock
		conn = e.conn
		while True:
			d = sock.recv(1024)
			if not d:
				break
			print len(d),repr(d)
			r = conn.codec.queueIn(d,conn)
			packets,retry = conn.codec.decode() #解析出来的完整的 MediaType.*
			#检查包缓冲是否过大，无效连接应该尽早丢弃
#			print packets,retry
			if len(packets):
				for d in packets: # d - (MsgAoModule_Base)指向不同的数据包类型,这些包允许混在同一个连接上接收
					m = conn.codec.parseMessage(d)
#					print m
					if not m: continue
					e = DeviceEvent()
					e.type = DeviceEvent.RECVED_DATA
					e.conn = conn
					e.data = m
					self.event(e) # route to DtuServer.aom_event()
					if e.accept == False: #关联失败，关闭socket
						retry = False
						break
			if not retry : #缓冲无效或者解码错误
				sock.close()
				break

		e = DeviceEvent()
		e.type = DeviceEvent.DISCONNECTED
		e.conn = conn
		self.event(e)      #发送到用户
		sock.close()
		print 'client lost:',str(address)

	
	def newline(self,module,url):
		#主动向外建立tcp连接
		#@param module  MediaDataType.* 通道媒体类型
		#@param codec 解码器 默认的解码器不对数据做任何处理
		#@param async 是否开启异步读的模式,同步方式必须让用户主动在连接对象上调用read()
		#相同的url 返回相同的connection对象
		print 'do not suport so far!'
		return None
	
