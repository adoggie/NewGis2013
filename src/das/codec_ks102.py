# -- coding:utf-8 --
#TK102 解码器定义
#这个设备没有包头包尾格式定义，假定一次读取一个完整数据包

#from aobject import *
import os,os.path,sys,time,datetime,copy,struct,array,traceback
#import codec

#MediaCodecType = MediaDataType
class MediaDataType:	
	GPS   = 1<<0
	AUDIO = 1<<1
	VIDEO = 1<<2
	IMAGE = 1<<3
	TEXT =  1<<4
	IODATA = 1<<5
	RAWBLOB = 1<<6	
	COMMAND = 1<<7	#通用命令
	ALARM =  1<<8  #报警信息
	UNDEFINED = 0xff
	

AOCTRL_CMD_SHAKE_ACK =1 	#应答握手信号信息
AOCTRL_CMD_REG_ACK= 2	#终端注册响应消息
AOCTRL_CMD_SAMPLING_TIMESET = 3 	#等时连续回传设置
AOCTRL_CMD_ALARM_ACK = 4	#应答报警消息
AOCTRL_CMD_NAMED = 5 	#一次点名消息
AOCTRL_CMD_SPEEDSET = 6 #设置车速上下限
AOCTRL_CMD_POWER_ONOFF = 7 #电路控制信号
AOCTRL_CMD_OIL_ONOFF = 8  #油路控制信号
AOCTRL_CMD_REBOOT = 9 		#控制设备重启消息
AOCTRL_CMD_ACC_ON_TIME = 10 #设置ACC开发送数据间隔
AOCTRL_CMD_ACC_OFF_TIME = 11 #设置ACC关发送数据间隔
AOCTRL_CMD_BARRIER_SET = 12 	#设置电子围栏消息
AOCTRL_CMD_GETLOCATION = 13 		#应答获取终端所在位置消息
AOCTRL_CMD_LISTEN_START = 14 		#监听命令
AOCTRL_CMD_COMMADDR_SET = 15 	#设置终端IP地址和端口
AOCTRL_CMD_APN_SET = 16			# 设置APN消息
AOCTRL_CMD_GET_VERSION = 17 	# 读取终端版本消息
AOCTRL_CMD_CLEAR_ALARMS = 18 	#取消所有报警消息
AOCTRL_CMD_CLEAR_MILES = 19 	#里程清零消息
AOCTRL_CMD_INIT_MILES = 20 		#里程初始化消息
AOCTRL_CMD_UPDATING = 21 		#启动升级消息

AOCTRL_CMD_SHACK_REQ =31 #握手信号消息
AOCTRL_CMD_REG_REQ =32 	#终端注册信息
AOCTRL_CMD_SAMPLING_TIMESET_ACK = 32 #应答等时连续回传设置
AOCTRL_CMD_ALARM_REQ = 33 		#警报消息
AOCTRL_CMD_NAMED_ACK = 34 		#应答点名信息
AOCTRL_CMD_SIMPLING_GPSDATA = 35 		#等时连续回传消息
AOCTRL_CMD_SIMPLING_END = 36 	#连续回传结束消息
AOCTRL_CMD_SPEEDSET_ACK = 37 	#应答设置车速上下限
AOCTRL_CMD_POWERCTRL_ACK = 38   #应答电路控制
AOCTRL_CMD_OILCTRL_ACK = 39 	#应答油路控制
AOCTRL_CMD_REBOOT_ACK = 40 		#应答设备重启消息
AOCTRL_CMD_ACCON_TIMESET_ACK = 41 #应答设置ACC开发送数据间隔
AOCTRL_CMD_ACCOFF_TIMESET_ACK=42 #应答设置ACC关发送数据间隔
AOCTRL_CMD_BARRIER_SET_ACK =  43 #应答设置电子围栏消息
AOCTRL_CMD_GETLOCATION_ACK = 44  #获取终端所在位置消息
AOCTRL_CMD_LISTEN_ACK = 45 		#应答监听命令
AOCTRL_CMD_COMMADDR_SET_ACK=46	#应答设置终端IP地址和端口
AOCTRL_CMD_APN_SET_ACK=47		#应答设置APN消息
AOCTRL_CMD_GETVERSION_ACK=48	#应答读取终端版本消息
AOCTRL_CMD_CLEAR_ALARMS_ACK=49	#应答取消所有报警消息
AOCTRL_CMD_CLEAR_MILES_ACK=50 	#应答里程清零消息
AOCTRL_CMD_UPDATING_ACK = 61 	#应答启动升级消息
AOCTRL_CMD_INIT_MILES_ACK = 62	#应答初始化里程消息	

AOCTRL_CMD_LIST={
	AOCTRL_CMD_SHAKE_ACK:u'应答握手信号信息',
	AOCTRL_CMD_REG_ACK:u'终端注册响应消息',
	AOCTRL_CMD_SAMPLING_TIMESET:u'等时连续回传设置',
	AOCTRL_CMD_ALARM_ACK:u'应答报警消息',
	AOCTRL_CMD_NAMED:u'一次点名消息',
	AOCTRL_CMD_SPEEDSET:u'设置车速上下限',
	
	AOCTRL_CMD_POWER_ONOFF:u'电路控制信号',
	AOCTRL_CMD_OIL_ONOFF:u'油路控制信号',
	AOCTRL_CMD_REBOOT:u'控制设备重启消息',
	AOCTRL_CMD_ACC_ON_TIME :u'设置ACC开发送数据间隔',
	AOCTRL_CMD_ACC_OFF_TIME :u'设置ACC关发送数据间隔',
	AOCTRL_CMD_BARRIER_SET :u'设置电子围栏消息',
	AOCTRL_CMD_GETLOCATION :u'应答获取终端所在位置消息',
	AOCTRL_CMD_LISTEN_START :u'监听命令',
	AOCTRL_CMD_COMMADDR_SET :u'设置终端IP地址和端口',
	AOCTRL_CMD_APN_SET :u'设置APN消息',
	AOCTRL_CMD_GET_VERSION :u'读取终端版本消息',
	AOCTRL_CMD_CLEAR_ALARMS :u'取消所有报警消息',
	AOCTRL_CMD_CLEAR_MILES :u'里程清零消息',
	AOCTRL_CMD_INIT_MILES :u'里程初始化消息',
	AOCTRL_CMD_UPDATING :u'启动升级消息',
	
	AOCTRL_CMD_SHACK_REQ :u'握手信号消息',
	AOCTRL_CMD_REG_REQ :u'终端注册信息',
	AOCTRL_CMD_SAMPLING_TIMESET_ACK :u'应答等时连续回传设置',
	AOCTRL_CMD_ALARM_REQ :u'警报消息',
	AOCTRL_CMD_NAMED_ACK :u'应答点名信息',
	AOCTRL_CMD_SIMPLING_GPSDATA :u'等时连续回传消息',
	AOCTRL_CMD_SIMPLING_END :u'连续回传结束消息',
	AOCTRL_CMD_SPEEDSET_ACK :u'应答设置车速上下限',
	AOCTRL_CMD_POWERCTRL_ACK :u'应答电路控制',
	AOCTRL_CMD_OILCTRL_ACK :u'应答油路控制',
	AOCTRL_CMD_REBOOT_ACK :u'应答设备重启消息',
	AOCTRL_CMD_ACCON_TIMESET_ACK :u'应答设置ACC开发送数据间隔',
	AOCTRL_CMD_ACCOFF_TIMESET_ACK:u'应答设置ACC关发送数据间隔',
	AOCTRL_CMD_BARRIER_SET_ACK :u'应答设置电子围栏消息',
	AOCTRL_CMD_GETLOCATION_ACK :u'获取终端所在位置消息',
	AOCTRL_CMD_LISTEN_ACK :u'应答监听命令',
	AOCTRL_CMD_COMMADDR_SET_ACK:u'应答设置终端IP地址和端口',
	AOCTRL_CMD_APN_SET_ACK:u'应答设置APN消息',
	AOCTRL_CMD_GETVERSION_ACK:u'应答读取终端版本消息',
	AOCTRL_CMD_CLEAR_ALARMS_ACK:u'应答取消所有报警消息',
	AOCTRL_CMD_CLEAR_MILES_ACK:u'应答里程清零消息',
	AOCTRL_CMD_UPDATING_ACK :u'应答启动升级消息',
	AOCTRL_CMD_INIT_MILES_ACK :u'应答初始化里程消息',	
}
	
	
ALARM_TYPELIST={
	0:u'车辆断电',
	1:u'电子围栏入界报警',
	2:u'车辆劫警（SOS求助）',
	3:u'车辆防盗器警报',
	4:u'车辆低速报警',
	5:u'车辆超速报警',
	6:u'电子围栏出界报警'
}


def parseTime(dmy,hms):
	d,mon,y = map(int, map(float,[dmy[:2],dmy[2:4],dmy[4:]]) )
	h,min,s = map(int, map(float,[hms[:2],hms[2:4],hms[4:]]) )
	print d,mon,y,h,min,s
	return time.mktime((2000+y,mon,d,h,min,s,0,0,0))

def parseDegree(v):
	pp = v.split('.')
	mm1 = pp[0][-2:]
	mm2 = '0'
	if len(pp)>1:
		mm2 = pp[1]
	dd = pp[0][:-2]
	mm = mm1 + "." + mm2
	degree = float(dd)+ float(mm)/60.0
	return degree

#1节等于每小时 1海里，也就是每小时行驶1.852千米（公里）
def parseSpeed(s):
	km =0
	km = float(s)*1.852
	return km


#简单的模拟gps接收解码器
#gps接收程序解析之后连接本地的TcpService端口，并传送过来
#只有简单的gps数据，模拟端口打开
class MediaCodec_KS102:
	def __init__(self):
		self.buf =''
		self.conn = None
		self.errtimes=0	#解析出错次数达到指定数则断开连接
	

	
	# parse - codec 必须实现
	#对于某些设备的请求消息，这里必须进行默认的应答
	#如果出现大量数据包的要发送回设备的情况，考虑建立队列，用工作线程
	# 慢慢发送，因为parse还在socket接收线程中
	def parse(self,aom,d):
		pass 

	def crc_16_result(self,d):
		#struct.unpack('I')
		print d
		i=0
		j=0
		c=0
		treat =0
		bcrc = 0
		crc =0
		s =array.array('B')
		s.fromstring(d)
		#print len(s)
		for i in range(len(s)):			
			c = s[i]
			for j in range(8):
				treat = c&0x80
				c = (c<<1)&0xff
				
				bcrc = ( crc >>8 )&0xff
				bcrc = bcrc&0x80
				#print crc
				crc = (crc << 1) & 0xffff
				#print crc
				if treat != bcrc:
					crc = (crc^0x1021) &0xffff
					#print '..',crc			
			
		return crc
	
	 
	def decode(self,s,conn):			
		#@return: 	packets,retry		
		#解码出多个消息包，并返回是否
		# imei 视为设备唯一编号 mid
		self.conn = conn		
		msglist=[]
		retry = True
		print s
		try:
			p = s.find(',')
			d = s[p+1:-2]
			crc = s[-2:]
			sum, = struct.unpack('H',crc)			
			if self.crc_16_result(d) != sum:
				print 'crc error'
				return (),True
			#13145826175,GPRMC,022011.000,A,2234.0200,N,11403.0754,E,0.00,189.47,040310,,,A*6F,F, battery,imei:354776030402512,114
			print d
			#print d.split(',')[-1]
			#tel,gprmc,hms,av,lat,ns,lon,ew,speed,angle,dmy,p1,p2,mode,FL,battery,imei,msglen, = d.split(',')
			tel,gprmc,hms,av,lat,ns,lon,ew,speed,angle,dmy,p1,p2,mode,FL,imei,msglen, = d.split(',')
			imei = imei.split(':')[1]			
			angle = float(angle)
			speed = float(speed)*1.852 # 节到km转换
			lon = parseDegree(lon)
			lat = parseDegree(lat)
			time = parseTime(dmy,hms)+3600*8	#时间加上GMT8
			gps = {
				'time':time,
				'lon':lon,
				'lat':lat,
				'speed':speed,
				'angle':angle,
				'power':0,
				'acc':0,
				'miles':0
			}
			msg = {
				'mid':imei,
				'cmd':AOCTRL_CMD_SIMPLING_GPSDATA,
				'gps':gps,				
			}
			msglist.append(msg)
		except:
			traceback.print_exc()
			msglist=()
			retry = True
			self.errtimes+=1
			if self.errtimes > 4: #解析错误次数过多，断开连接
				return (),False
		return msglist,retry


	
	#执行设备命令
	def command(self,aom,msg):
		# cmd - object (json decoded)
		#@return:  返回命令控制消息
		cmd = msg['cmd']
		code=''
		params=''
		if not msg.has_key('seq'):
			msg['seq'] = '0'*12
			
		if cmd == AOCTRL_CMD_REG_ACK: #注册响应
			code = "(%sAP05)"%(msg['seq'])

		#save to ctrl log 		
		log = aom.gm.AO_CtrlLog()
		log.ao = aom.ao.dbobj
		log.cmd = cmd
		log.time = datetime.datetime.now()
		text = "%s: %s"%(AOCTRL_CMD_LIST[log.cmd],params)
		log.comment = text[:200]
		log.save()
		
		return code
	
	#将d数据写入db中
	# 根据不同的数据进行hash分派 目前之后gps和告警信息进行分派
	def save(self,aom,d):		
		#log = aom.gm.AO_CtrlLog()
		#log.ao = aom.ao.dbobj
		#log.cmd = d['cmd']
		#log.time = datetime.datetime.now()
		#text = "%s: %s"%(AOCTRL_CMD_LIST[log.cmd],d['params'])
		#log.comment = text[:200]
		#log.save()
		#以下存储gps数据和设备状态数据
		print 'save:',d
		gps = d['gps']
		if True:
			# save to db
			timestamp = gps['time']
			g = aom.gm.AOMData_Gps()
			g.ao = aom.ao.dbobj
			g.savetime = datetime.datetime.fromtimestamp(timestamp)
			g.lon = gps['lon']
			g.lat = gps['lat']
			g.speed = gps['speed']
			g.angle = gps['angle']
			g.power = 0
			g.acc = 0
			g.miles = 0
			g.save()
			#for dispatch
			t = timestamp  #time.mktime(g.savetime.timetuple())
			s = {'type':MediaDataType.GPS,'hwid':aom.id,
			 'lon':g.lon,'lat':g.lat,
			 'speed':g.speed,'angle':g.angle,
			 'satenum':0,'sateused':0,
			 'time':t,
			 'power':g.power,
			 'acc':g.acc,
			 'miles':g.miles}	
			aom.dispatch(s) #分派到 cached server
	
	
'''
TK102方案GPRS通讯协议
上传数据
“1003040220,13145826175,GPRMC,022011.000,A,2234.0200,N,11403.0754,E,0.00,189.47,040310,,,A*6F,F, battery,imei:354776030402512,114迁”

19个,分隔数据段

数据解析
“1003040220”		
时间流水号:  2010年03月04日02时22分

“13145826175”      
手机号码：授权情况下为授权号码，否则为最后操作tracker的手机号码，或则为空.
“GPRMC,022011.000,A,2234.0200,N,11403.0754,E,0.00,189.47,040310,,,A*
6F”    
GPRMC数据：GPS模块数据完整数据，单片机没有对其进行修改.
	
“F”                当前GPS是否有信号：   F,表示有，L表示没有
“battery”          报警信息：【SOS报警：”help me”;电子砸烂报警:” Stockade”;移位报警:” move”;超速报警;” speed”;低电报警;” bat:”】,非报警数据此位置为空.
“imei:354776030402512”   GPRS 模块IMEI号
“114”                                     数据长度【13145826175,GPRMC,022011.000,A,2234.0200,N,11403.0754,E,0.00,189.47,040310,,,A*6F,F, battery,imei:354776030402512,】，括号内部的数据的长度，单位字节.
“迁”                CRC检验：这是两个字节的十六进制数据，有时显示为乱码，又是显示为空，因为他是十六进制。
                                                                              计算范围【13145826175,GPRMC,022011.000,A,2234.0200,N,11403.0754,E,0.00,189.47,040310,,,A*6F,F, battery,imei:354776030402512,114】
                                  算法如下：
注意：此系统unsigned int  为16bits,对于PC软件，需要对结果做 &0XFFFF运算。
unsigned int CRC_16(unsigned char *buf, unsigned int datalen)
{
    unsigned int i;
	unsigned char j;
    unsigned char c, treat, bcrc;
    unsigned int crc = 0;

    for (i = 0; i < datalen; i++)
    {
        c = buf[i];
        for (j = 0; j < 8; j++)
        {
            treat = c & 0x80;
            c <<= 1;
            bcrc = (crc >> 8);
			bcrc &= 0x80;
            crc <<= 1;
            if (treat != bcrc)
                crc ^= 0x1021;
        }
    }
    return crc;
}

附:GPS模块数据解释说明：

　　$GPRMC,<1>,<2>,<3>,<4>,<5>,<6>,<7>,<8>,<9>,<10>,<11>,<12>*hh 
　　<1> UTC时间，hhmmss.sss(时分秒.毫秒)格式 
　　<2> 定位状态，A=有效定位，V=无效定位 
　　<3> 纬度ddmm.mmmm(度分)格式(前面的0也将被传输) 
　　<4> 纬度半球N(北半球)或S(南半球) 
　　<5> 经度dddmm.mmmm(度分)格式(前面的0也将被传输) 
　　<6> 经度半球E(东经)或W(西经) 
　　<7> 地面速率(000.0~999.9节，前面的0也将被传输) 
　　<8> 地面航向(000.0~359.9度，以正北为参考基准，前面的0也将被传输) 
　　<9> UTC日期，ddmmyy(日月年)格式 
　　<10> 磁偏角(000.0~180.0度，前面的0也将被传输) 
　　<11> 磁偏角方向，E(东)或W(西) 
　　<12> 模式指示(仅NMEA0183 3.00版本输出，A=自主定位，D=差分，E=估算，N=数据无效)

'''
#c = MediaCodec_KS102()
#d="1106160039,13916624477,GPRMC,163905.000,A,3104.2062,N,12130.0542,E,0.33,347.69,150611,,,D*6C,F,imei:354779033883985,105"
#d="13916624477,GPRMC,163905.000,A,3104.2062,N,12130.0542,E,0.33,347.69,150611,,,D*6C,F,imei:354779033883985,105"
#
#log = open('ks102_data.txt','rb')
#s = log.read()
#print c.decode(s,None)

