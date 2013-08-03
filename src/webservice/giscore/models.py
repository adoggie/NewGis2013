# -*- coding:utf-8 -*-

from django.db import models
import os,sys,struct,datetime

# Create your models here.

#用户信息
#用户登录方式  client.sid "." user.sid  | user.passwd
class AppUser(models.Model):	
	sid = models.CharField(max_length=20,db_index=True)		#用户会员编号
	passwd = models.CharField(max_length=20)	
	name = models.CharField(max_length=20)
	#aos = models.ManyToManyField('ActiveObject')
	#client = models.ForeignKey('AppClient') #
	address = models.CharField(max_length=200,default='')		#地址
	zipcode = models.CharField(max_length=20,default='')	#邮政编码
	phone = models.CharField(max_length=30,default='')		#联系电话
	contactman = models.CharField(max_length=30,default='')	#联系人
	comment = models.CharField(max_length=400,default='')	#备注信息	 users = models.ManyToManyField(AppUser) #a可隶属于多个用户
	aos = models.ManyToManyField('ActiveObject',db_index=True) #多个aos
	delta= models.TextField(null=True,default='{}')
	enable = models.BooleanField(default=True,db_index=True) #是否启用 2012.5.15

class UserPointGroup(models.Model):
	name = models.CharField(max_length=20,db_index=True)
	user = models.ForeignKey(AppUser,db_index=True)
	comment= models.TextField(null=True)
	
#用户兴趣点
#
class UserPoint(models.Model):
	name = models.CharField(max_length=20,db_index=True)	
	type = models.IntegerField() #类型
	lon = models.FloatField() # 经度
	lat = models.FloatField() # 纬度
	wkt = models.TextField(null=True) 
	creatime = models.DateTimeField()
	user = models.ForeignKey(AppUser,db_index=True)
	group = models.ForeignKey('UserPointGroup',db_index=True,null=True)
	grid_x = models.IntegerField()  #点位置信息划分网格，参照原始点 (0,0),规格(0.01,0.01)计算偏移网格编号
	grid_y = models.IntegerField()  #方便快速加载和定位
	res_s = models.FloatField(default=0) 	#显示精度范围
	res_e = models.FloatField(default=0)	# 0 表示任何比例下都显示
	comment= models.TextField(null=True)

#地理信息点信息，用于加载到地图上用于交互
#地图处理之后将点层导入到MapGisPoint表内
class GisMapPoint(models.Model):
	sid = models.IntegerField(db_index=True) 	
	name = models.CharField(max_length=20,db_index=True)	
	type = models.IntegerField() #类型
	lon = models.FloatField() # 经度
	lat = models.FloatField() # 纬度
	delta = models.TextField(null=True) #额外信息json格式，可以是电话，地址，网址等等信息
	grid_x = models.IntegerField() #点位置信息划分网格，参照原始点 (0,0),规格(0.01,0.01)计算偏移网格编号
	grid_y = models.IntegerField() #
	res_s = models.FloatField(default=0) #显示精度范围
	res_e = models.FloatField(default=0) #显示精度结束

#用户留言
class UserMessage(models.Model):
	user = models.ForeignKey(AppUser,db_index=True)
	title = models.CharField(max_length=200,db_index=True)
	content =  models.TextField(null=True)
	time = models.DateTimeField(db_index=True)
	replytime = models.DateTimeField(null=True)
	replycontent = models.TextField(null=True)
	amdin =  models.CharField(null=True,max_length=40,db_index=True) #回复管理员
	delta = models.TextField(null=True)



#系统通告
class SysNotice(models.Model):
	topic = models.TextField()  #主题
	content =  models.TextField(null=True)
	time = models.DateTimeField(db_index=True)
	amdin =  models.CharField(null=True,max_length=40,db_index=True) #发布管理员
	delta = models.TextField(null=True)


#用户地理层
#class UserMapLayer(models.Model):
#	name = models.CharField(max_length=30,db_index=True)
#	resbegin = models.FloatField() #显示精度范围
#	resend = models.FloatField()
#	client = models.ForeignKey('AppUser',db_index=True)

	
#地理访问点分组
class VisitedPointGroup(models.Model):
	name = models.CharField(db_index = True,max_length=40)
	user = models.ForeignKey(AppUser,db_index=True)
	comment= models.TextField(null=True)
	
#地理访问点 
class VisitedPoint(models.Model):
	name = models.CharField(db_index = True,max_length=40)
	group = models.ForeignKey('VisitedPointGroup',db_index=True,null=True)
	zoom = models.SmallIntegerField()		#缩放级别
	lon = models.FloatField() # 经度
	lat = models.FloatField() # 纬度
	wkt = models.TextField(null=True) #冗余的地理点存储 文本描述方式
	user = models.ForeignKey('AppUser',db_index=True)
	comment= models.TextField(null=True)

#围栏组
#允许没有组的围栏
class TrackBarrierGroup(models.Model):
	name = models.CharField(db_index = True,max_length=20)
	user = models.ForeignKey('AppUser',db_index=True)
	comment= models.TextField(null=True)

#多边形围栏  
class TrackBarrier(models.Model):
	name = models.CharField(max_length=20,db_index=True)
	wkt = models.TextField() #x,y,w,h gps真实坐标
	fill = models.CharField(max_length=20,default='0xff0000')  #颜色
	color = models.CharField(max_length=20,default='0xff0000') #线框颜色
	opacity = models.FloatField(default=0.5)#填充透明度
	user = models.ForeignKey(AppUser,db_index=True)
	group = models.ForeignKey('TrackBarrierGroup',db_index=True,null=True)
	comment= models.TextField(null=True)

#activeObject group
#客户对ao的分组
#客户的分组是平面的，不支持组嵌套组
class AO_AppGroup(models.Model):
	name = models.CharField(max_length=40,db_index=True)		#组名称 
	iconurl = models.CharField(max_length=40)								#图标资源	
	user = models.ForeignKey(AppUser,db_index=True) 	#组隶属于某一个具体的用户
	aos = models.ManyToManyField('ActiveObject',db_index=True) #组内包含的ActiveObject
	#组属性如果添加到ActiveObject内的话，就限制了AO只能隶属于一个组了，且被限制在同一个user了
	comment = models.TextField(null=True)	#备注


class AO_UserAlarmSettings(models.Model):
	name = models.CharField(max_length=40,db_index=True)
	user = models.ForeignKey(AppUser,db_index=True)
#	type = models.CharField(max_length = 40,db_index=True) #报警类型,speed,barrier
	enable = models.BooleanField(default=True) #报警是否启用
	creatime = models.DateTimeField()
	actions= models.TextField(null=True) #报警产生联动
	#concurrency = models.BooleanField(default=False) #多个actions是否被并发执行
	'''
	actions=[action1,..]
	action{  报警触发将action信息写入AO_TaskQueue表
		type:  - mail,sms,asi_detach,poweroff,oiloff
		module: -  指定触发的外部加载模块 alaram action
		times: - 执行次数
		freq: - 执行时间间隔
		params:{}  - 其他参数
			sms|mail: {tolist:'',
					content:''}
			asi_detach:{}  取消ao与asi的绑定
			poweroff:{} 断电
			oiloff:{} 断油

		内置标志 $time - 当前时间
				$ao - 设备对象名称
				$reason - 报警触发内容
	}
	例如 ：超速报警联动触发动作，改变采集频率30s->5s，持续n秒，发送改变采集频率5s->30s
	'''
	filter = models.TextField(null=True) #报警产生的条件
	'''
	filter - { 满足filter则进行触发
		suppress_duration - 抑制时长，连续报警时间达到上限才进行报警触发,0表示检测一次报警条件成立，马上触发联动
		suppress_wait - 触发报警之后等待时间，防止再次连续触发，导致报警不断,默认为0：不等待
		time:{timerange:(start,end),weekdays:(1,1,1,1,1,1,1),daytimes:(8,10)}
		params:
			[
				{name:'barrier_in',param:[name,(x,y,w,h),.. ]}   bid-围栏系统编号 ，围栏矩形采用地图坐标，在报警检测时需要转换为gps坐标
				{name:'speedover',param:(from,to)}
				{name:'gpslost',param:timeout}
				{name:'powerlost',param:None}
				{name:'offline',param:timeout}
				{name:'sos',param:None}
				{name:'acc_on',param:None}
				{name:'acc_off',param:None}
			]
	}


	suppress_times - (非0有效) 抑制上报次数 , 第一次触发报警，抑制后续n-1次报警触发，超过伐值则从新触发报警
	timerange:[start,end] - 有效的时间周期 ,如果为空则weekdays有效
		weekdays:[1,0,0,0,0,1,1] - 周天掩码,null失效，允许每一天
		daytimes:(8,10) - 一天内的时间段， null允许任何时间
	'''

#系统活动对象	
class ActiveObject(models.Model):
	name = models.CharField(max_length=40)
	#user = models.ForeignKey(AppUser,db_index=True)	#设备隶属的客户
	dasid = models.CharField(max_length=40,db_index=True,null=True) #接入服务器编号
	#enabled = models.BooleanField(default=False,db_index=True) # 0 - 未监控 ; 1 - 已监控中																
	devtype = models.CharField(max_length=20,default='sw-k101') #
	comment = models.TextField(null=True) # 描述ao信息 ,可以设置联系人、电话...
	telphone = models.CharField(max_length=30,null=True)	#联系电话
	zipcode = models.CharField(max_length=30,null=True) #邮政编码
	address = models.CharField(max_length=120,null=True) #地址
	contact = models.CharField(max_length=40,null=True) #联系人
	active_time = models.DateTimeField(null=True)	#开通时间
	expire_time = models.DateTimeField(null=True)	#到期时间
	type = models.IntegerField(default=0)	# ao 对象类型 AO_VEHICLE_* ,AO_PEOPLE_*

	status = models.IntegerField(default=0)	# 0 - 未使用 ； 1 - 已启用 ; 2 -维护中

	alarms = models.IntegerField(default=0)#报警掩码
	
	speed_high = models.IntegerField(default=0) #高速限制
	speed_low = models.IntegerField(default=0) #低速限制
	enable = models.BooleanField(default=False) #是否启用
	alarmsettings = models.ManyToManyField(AO_UserAlarmSettings,db_index=True) #报警配置项目
	delta = models.TextField(null=True)

#定位模块
class AO_Module(models.Model):
	ao = models.ForeignKey(ActiveObject,db_index=True)	
	idx = models.IntegerField(default=0)		#模块编号	
	type =  models.IntegerField(db_index=True)				#模块类型 MediaDataType各种类型的掩码组合 GPS|IODATA
	sid = models.CharField(max_length = 40,db_index=True) #设备模块的硬件标示
	svcname = models.CharField(max_length = 40,db_index=True,default='') #接入的服务类型名称，具体指向哪个tcp服务名称(dtuconfig.txt:services)	
	ver = models.CharField(null=True,max_length = 40,db_index=True) #版本信息	
	settings = models.TextField(null=True)	#不同的设备类型(GPS|CAMERA...)可以分别设定不同的参数类型	
	'''
	settings:{ 这些参数设置之后，设备连接进来必须要执行设置这些参数进去 
		acc_on_freq:30,		
		acc_off_freq:30
	}
	'''
	
#ao对象隶属于系统内部分组
#系统分组内的设备可以分配给client
class AO_SysGroup(models.Model):
	name = models.CharField(max_length=40)		#组名称 
	iconurl = models.CharField(max_length=40,null=True)								#图标资源
	aos = models.ManyToManyField(ActiveObject,db_index=True) #组内包含的ActiveObject
	comment = models.TextField(null=True)	#备注
	
	
#活动对象控制日志
#控制包含了例如: 设备参数设置、报警设置...
'''
TaskQueue
考虑计划任务，例如: 围栏和超速会结合时间进行周期性的执行（每天上午9点到14点设置围栏报警)
报警产生时候为了加速gps采集频点，也可以置入taskqueue

taskqueue包含所有系统执行任务，可以是访问ao的，也可以是些系统级的计划任务
.exec_module 是动态挂载的执行模块 ，AO_TaskQueue的纪录信息都将被传递到module被执行

'''

class AO_TaskQueue(models.Model):
	type = models.CharField(max_length = 40,db_index=True) #任务名称 
	status = models.IntegerField(default=0)	# 0 - 等待处理  ; 1 - 开始处理 ; 2 - 被终止
	action = models.TextField(null=True)
	'''
	action:{
			type: action type
			module:
			params:
			times: 执行次数
			freq: 执行频率	
		}
	'''
	starttime = models.DateTimeField(db_index=True) #执行计划时间
	endtime  = models.DateTimeField(db_index=True) #执行结束时间
	seqno = models.IntegerField(default=0)	#流水号
	taskplan = models.IntegerField(null=True)		#隶属的计划 ,null表示不是计划产生的 
	alarmsetting =  models.IntegerField(null=True) #任务可以是由报警某个报警配置产生

'''
TaskPlan
'''
class AO_TaskPlanTable(models.Model):
	type = models.CharField(max_length = 40,db_index=True)			#任务类型
	target = models.TextField(null=True)			#作用对象,例如 ao集合
	creator = models.IntegerField()					#计划创建者 0 表示系统
	creattime = models.DateTimeField(db_index=True) #创建时间
	status =  models.IntegerField()				# 0 - 未启用; 1 - 启用但未执行; 2 - 执行中

#ao_ctrllog
#设备控制日志，包含对设备的控制
class AO_ModuleLog(models.Model):
	ao = models.ForeignKey(ActiveObject,db_index=True)
	module = models.ForeignKey(AO_Module,db_index=True)	
	type = models.IntegerField()	# 1 - 系统到设备; 2-设备到系统
	time = models.DateTimeField(db_index=True)
	msgtype = models.TextField(db_index=True) 	#命令控制类型
	params = models.TextField(null=True) 		#设备控制参数
	rawmsg = models.TextField(null=True) 		#设备原始通信参数
	seq = models.TextField(db_index=True,null=True) #控制流水号，便于匹配上
	
#系统设置设备参数预先存放在此，当设备连接进入便读取发送到设备
class AO_CtrlSetPrepare(models.Model):
	ao = models.ForeignKey(ActiveObject,db_index=True)
	module = models.ForeignKey(AO_Module,db_index=True)	
	time = models.DateTimeField(db_index=True)	#命令提交时间
	msgtype = models.TextField(db_index=True) 	#命令控制类型
	params = models.TextField() 		#设备控制参数
	status = models.IntegerField() 		#0 -未发送 ； 1 -已发送

	
#活动对象报警日志
#之后通过AlarmSetting处理过的日志才会比存储进来
#class AO_AlarmLog(models.Model):
#	ao = models.ForeignKey(ActiveObject,db_index=True)
#	issue_time = models.DateTimeField(db_index=True)  #本次报警时间
#	status = models.IntegerField()		# 0 - 未处理; 1-已处理;
#	type =  models.CharField(max_length = 40,db_index=True)	#报警类型,例如: 手动按键报警、速度报警、围栏报警
#	detail = models.TextField(null=False)	#报警详细参数, json编码，不同消息采用不同定义 2012.3.30

class AO_AlarmLog(models.Model):
	ao = models.ForeignKey(ActiveObject,db_index=True)
	name =models.CharField(max_length = 40,db_index=True)	#报警类型,例如: 手动按键报警、速度报警、围栏报警
	filter = models.TextField() #触发条件
	actions = models.TextField() #触发行为
	filter_text = models.TextField(null=True) #触发条件
	actions_text = models.TextField(null=True) #触发行为
	time = models.DateTimeField(db_index=True)  #触发时间
	delta = models.TextField(null=True)

#一次触发报警引发多次动作
class AO_AlarmActionLog(models.Model):
	alarmlog = models.ForeignKey(AO_AlarmLog,db_index=True)
	time = models.DateTimeField(db_index=True)  #触发时间
	type = models.CharField(max_length = 40,db_index=True) # sms,mail
	target = models.TextField(null=True)    #发送接收对象
	text = models.TextField(null=True)     #发送内容
	delta = models.TextField(null=True)

#
#之后通过AlarmSetting处理过的日志才会比存储进来
class UserLoginLog(models.Model):
	login =  models.CharField(max_length = 40,db_index=True) #系统登录名
	name =  models.CharField(max_length = 40,db_index=True) #用户名
	passwd =  models.CharField(max_length = 40,db_index=True)   #口令
	time = models.DateTimeField(db_index=True)  #本次报警时间
	ipaddr = models.CharField(null=True,max_length = 20,db_index=True)
	region = models.CharField(max_length = 40,null=True,db_index=True) #地理区域
	succ = models.BooleanField()
	usertype =  models.IntegerField(default=1) #用户类型 1- user, 2 - admin
	detail =  models.TextField(null=True) #原因

##报警设置
##支持报警在指定时间段有效
##报警触发将产生alarmlog记录，并产生task到taskqueue
## 2012.6.2 此表作废
## ao的报警运行状态都缓存在内存
#class AO_AlarmSettings(models.Model):
#	ao = models.ForeignKey(ActiveObject,db_index=True)
#	type = models.CharField(max_length = 40,db_index=True) #报警类型,speed,barrier
#	enable = models.BooleanField(default=True) #报警是否启用
#	actions= models.TextField(null=True) #报警产生联动
#	#concurrency = models.BooleanField(default=False) #多个actions是否被并发执行
#	'''
#	actions=[action1,..]
#	action{  报警触发将action信息写入AO_TaskQueue表
#		type:  -
#		module: -  指定触发的外部加载模块 alaram action
#		times: - 执行次数
#		freq: - 执行时间间隔
#		params:{}  - 其他参数
#	}
#	例如 ：超速报警联动触发动作，改变采集频率30s->5s，持续n秒，发送改变采集频率5s->30s
#	'''
#	filter = models.TextField(null=True) #报警产生的条件
#	'''
#	filter - { 满足filter则进行触发
#		suppress_times - (非0有效) 抑制上报次数 , 第一次触发报警，抑制后续n-1次报警触发，超过伐值则从新触发报警
#		suppress_duration - 抑制时长，连续报警时间达到上限才进行报警触发
#		timerange:[start,end] - 有效的时间周期 ,如果为空则weekdays有效
#		weekdays:[1,2,3,4,5,6,7] - 周天掩码,null失效，允许每一天
#		daytimes:[(8,10),(14,18),..] - 一天内的时间段， null允许任何时间
#		params:{barriers:[barrier_id,..],..} - 当type是围栏报警时有效,围栏记录编号集合
#	}
#	'''



#Gps定位信息	
class AOMData_Gps(models.Model):
	ao = models.ForeignKey(ActiveObject,db_index=True,null=True) #隶属对象
	aom = models.ForeignKey(AO_Module,db_index=True,null=True)
	savetime = models.DateTimeField( db_index=True,default=datetime.datetime.now())		#保存时间
	satenum = models.SmallIntegerField(default=0) 	#收星数
	sateused = models.SmallIntegerField(default=0) #定位星数
	lon = models.FloatField(default=0) #经度
	lat = models.FloatField(default=0)
	speed = models.FloatField(default=0) #速度
	angle = models.FloatField(default=0) #方向
	gpstime = models.IntegerField(default=0) #gps时间戳
	
	power = models.IntegerField(default=0)	#电源开启 2011.6.13
	acc = models.IntegerField(default=0)	#点火状态
	miles  = models.FloatField(default=0)	#里程计数
	av = models.IntegerField(default=0)  # 0 - 未定位, 1 -已定位
	
#拍照信息
#class AOMData_Image(models.Model):
#	ao = models.ForeignKey('ActiveObject',db_index=True)
#	savetime = models.DateTimeField(db_index=True)
#	imgtype = models.CharField(max_length=10)
#	imgwidth = models.IntegerField()
#	imgheight = models.IntegerField()
#	imgsize = models.IntegerField() 
#	imgfile  = models.CharField(max_length=256) #图片文件路径

#系统服务器
class SysModule(models.Model):
	sid = models.CharField(max_length=64,unique=True,db_index=True) #服务器编号
	type = models.CharField(max_length=40,db_index=True) # ctrlserver,das,sts,dgw(datagateway)	
	uptime =  models.DateTimeField(null=True) 	#更新时间
	commstr = models.CharField(max_length=60,default='')	#通信参数, tcp -h x.x.x.x -p 1234 
	
	
	
#服务系统日志
class SysModuleLog(models.Model):
	type = models.CharField(max_length=40) # ctrlserver,das,sts,dgw(datagateway)
	sid = models.CharField(max_length=64) #服务器编号
	time =  models.DateTimeField(null=True) 	#更新时间
	logtype = models.IntegerField()		#日志类型
	loglevel = models.IntegerField() 	#日志级别
	logtext = models.TextField() 			#日志内容
	
#客户信息
# 客户->用户
#客户创建时自动创建新客户的管理用户账号super,super可创建新的用户账号并分配权限和车辆
#class AppClient(models.Model):
#	sid = models.CharField(max_length=20,db_index=True,unique=True)		#系统编号
#	name = models.CharField(max_length=100)					#客户名称
#	address = models.CharField(max_length=200,default='')		#地址
#	zipcode = models.CharField(max_length=20,default='')	#邮政编码
#	phone = models.CharField(max_length=30,default='')		#联系电话
#	manager = models.CharField(max_length=30,default='')	#联系人
#	comment = models.CharField(max_length=400,default='')	#备注信息	
	

#用户登录历史记录
#class AppUserLoginLog(models.Model):
#	login = models.CharField(max_length=20,db_index=True)
#	passwd = models.CharField(max_length=20)#登录口令和密码
#	user = models.CharField(max_length=40,db_index=True)
#	time = models.DateTimeField()
#	ip = models.CharField(max_length=20,db_index=True)
#

#系统参数定义
class SystemGlobalSettings(models.Model):
	name = models.CharField(max_length=200,db_index = True,unique=True)
	value = models.TextField()
	type = models.CharField(max_length=32,null=True,default='string') #数据类型定义: string,numeric
	comment = models.TextField(null=True)
	
###############################################


class qiyexinxi(models.Model):
	name = models.TextField(null=True,db_index=True)
	addr = models.TextField(null=True,db_index=True)
	zipcode = models.TextField(null=True,db_index=True)
	money = models.IntegerField(null=True,db_index=True)
	money_s = models.TextField(null=True,db_index=True)
	manager = models.TextField(null=True,db_index=True)
	tel = models.TextField(null=True,db_index=True)
	content = models.TextField(null=True)
	fileno = models.IntegerField(null=True,db_index=True)