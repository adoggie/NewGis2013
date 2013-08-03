# -*- coding:utf-8 -*-

import sys,os,os.path

from pycomm import utils
from pycomm import network
from pycomm import message
from pycomm.message import *
from gisbase import *

#请求打开活动对象
class Msg_OpenActiveObject(MessageBase):
	def __init__(self):
		MessageBase.__init__(self,'OpenActiveObject')
		self.aolist=[]

#关闭活动对象
class Msg_CloseActiveObject(MessageBase):
	def __init__(self):
		MessageBase.__init__(self,'CloseActiveObject')
		self.aolist=[]


#flex注册到dwg
#flex user建立与dgw的socket连接之后即刻发送认证请求
class MsgUser_RegisterReq_0(message.MessageBase):
	def __init__(self):
		message.MessageBase.__init__(self,'user_registerreq_0')
		self.attrs['userid']=''	#用户
		self.attrs['passwd']=''	#密码

class MsgUser_Keepalive_0(message.MessageBase):
	def __init__(self):
		message.MessageBase.__init__(self,'user_keepalive_0')



#dwg注册到ctrlserver
class MsgDGW_Register_2(message.MessageBase):
	def __init__(self):
		message.MessageBase.__init__(self,'dgw_register')
		self.attrs['id']=''	#dgw's module id

#dwg到ctrlserver的心跳
class MsgDGW_Keepalive_2(message.MessageBase):
	def __init__(self):
		message.MessageBase.__init__(self,'dgw_keepalive')
		self.attrs['id']=''	#dgw's module id


#das注册到ctrlserver
class MsgDas_Register_2(message.MessageBase):
	def __init__(self):
		message.MessageBase.__init__(self,'das_register')
		self.attrs['id']=''	

#das心跳保活消息
class MsgDas_Keepalive_2(message.MessageBase):
	def __init__(self):
		message.MessageBase.__init__(self,'das_keepalive')
		self.attrs['id']=''	#


#class AlaramSpeed
	
#设置围栏报警
class MsgCtrlSet_Alaram_Add_0(message.MessageBase):
	def __init__(self):
		message.MessageBase.__init__(self,'ctrlset_alaram_add')
		self.attrs['aoid']=''	#dgw's module id
		self.attrs['type']=''		
		self.attrs['params']={}	#报警类型,行驶速度,区域报警...
		# speed - {low,high,}
	
class MsgCtrlSet_Alaram_Add_0(message.MessageBase):
	def __init__(self):
		message.MessageBase.__init__(self,'ctrlset_alaram_add')
		self.attrs['aoid']=''	#dgw's module id
		self.attrs['type']=''		
		self.attrs['params']={}	#报警类型,行驶速度,区域报警...
	


'''
gps接收数据
das接收数据传递到ctrlserver,dgw,sts等系统模块
'''
class MsgAo_GpsData_1(message.MessageBase):
	def __init__(self):
		message.MessageBase.__init__(self,'ao_gpsdata')
		self.attrs['aoid'] = 0
		self.attrs['modlue'] =''	#模块类型,例如: ks108
		self.attrs['recvtime'] = 0 #接收时间
		self.attrs['dasid'] = ''	#接收das服务器编号
		self.attrs['time'] = 0 #gps时间
		self.attrs['satenum'] = 0 #收星数
		self.attrs['sateused'] = 0 #定位星数
		self.attrs['lon'] =0	#
		self.attrs['lat'] =0
		self.attrs['speed'] = 0
		self.attrs['angle'] =0
		#self.attrs['miles'] = 0 	#里程数
		self.attrs['delta'] = {}	#附加属性
		#{miles,power,acc}    里程，电源状态，acc状态
	
#设备端采集上来的图像数据
class MsgAo_ImageData_1(message.MessageBase):
	def __init__(self):
		message.MessageBase.__init__(self,'ao_imagedata')
		self.attrs['aoid'] = 0
		self.attrs['modlue'] =''	#模块类型,例如: ks108

class MsgAo_VideoData_1(message.MessageBase):
	def __init__(self):
		message.MessageBase.__init__(self,'ao_videodata')
		self.attrs['aoid']=0
		self.attrs['modlue'] =''
		self.attrs['vcodec']=0
		self.attrs['width'] = 0
		self.attrs['height']=0
		
		#视频数据通过self.bin携带
		
class MsgAo_Alaram_1(message.MessageBase):
	def __init__(self):
		message.MessageBase.__init__(self,'ao_alarmdata')
		self.attrs['aoid'] = 0
		self.attrs['modlue'] =''	#模块类型,例如: ks108
		self.attrs['type'] = 0 		#报警类型
		self.attrs['reason'] = '' 	#报警内容描述
		self.attrs['delta']={}		#报警参数
		

class MsgAo_ParamQueryReturnmessage(MessageBase):
	def __init__(self):
		message.MessageBase.__init__(self,'ao_alarmdata')
		self.attrs['aoid'] = 0
		self.attrs['modlue'] =''	#模块类型,例如: ks108


##------------------ das message ----------------------------------

class MsgAoModule_Base(MessageBase):
	def __init__(self,msg='aom_data'):
		MessageBase.__init__(self,msg)
		self.attrs['cmd'] = None
		self.attrs['seq'] = ''
		self.attrs['mid'] = None
		self.attrs['params']= {}
		self.attrs['gps'] = {} #gps数据
		self.attrs['alarm']='' #报警参数
	
	def __unicode__(self):
		return str(self.attrs)
	
	def __str__(self):
		return unicode(self)

class MsgAoModule_Alarm(MessageBase):
	MSG='aom_alarm'
	def __init__(self,type):
		MessageBase.__init__(self,MSG)
		self.attrs['aoid'] = None	#ao对象
		self.attrs['aomid'] =  None	#aom对象
		self.attrs['type'] = type # =>>AlarmType.*
		self.attrs['params']={}

class MsgAoModule_GpsData(MessageBase):
	def __init__(self):
		MessageBase.__init__(self,'aom_gpsdata')
		self.attrs['aoid'] = None	#ao对象
		self.attrs['aomid'] =  None	#aom对象
		self.attrs['gps'] = {}
		
#系统到设备的控制命令
#命令就是些 xxx_xxx_5的消息
class MsgAom_Command(MessageBase):
	def __init__(self,aoid=None,cmd=None):
		MessageBase.__init__(self,'aom_command')
		self.attrs['aoid'] =  aoid	#aom对象
		self.attrs['command'] = cmd	#


'''
AP15 通知设备拨打监听电话
20120422 20:55:34 DEBUG send to device:(013661940344AP1513916624477) 
20120422 20:55:39 DEBUG (013661940344BS20)
'''
class MsgAom_Listen_5(MessageBase):
	def __init__(self):
		MessageBase.__init__(self,'aom_listen_5')
		self.attrs['aoid'] = None	#ao对象
		self.attrs['phone']=''		#监听拨打的电话号码



'''
AP07 查询设备版本信息
20120422 20:54:49 DEBUG send to device:(013661940344AP07) 
20120422 20:54:55 DEBUG (013661940344BP01GPS138,Mar 14 2011) 
'''
class MsgAom_GetVersion_5(MessageBase):
	def __init__(self):
		MessageBase.__init__(self,'aom_getversion_5')
		self.attrs['aoid'] = None	#ao对象

'''
AP00 一次点名 设备接收即刻返回BP04
20120422 21:14:47 DEBUG send to device:(013661940344AP00) 
20120422 21:14:53 DEBUG (013661940344BP04120422A3104.1965N12130.0536E000.0131442320.1900000000L000F2ACF) 
'''
class MsgAom_OnceNamed_5(MessageBase):
	def __init__(self):
		MessageBase.__init__(self,'aom_oncenamed_5')
		self.attrs['aoid'] = None	#ao对象

'''
AR00 等时持续回传设置
'''
class MsgAom_ContinuedSet_5(MessageBase):
	def __init__(self):
		MessageBase.__init__(self,'aom_continuedset_5')
		self.attrs['aoid'] = None	#ao对象
		self.attrs['freq'] = 0  #上传间隔 (s) 0 表示取消等时上传
		self.attrs['duration'] = 0 #时常 (s)

'''
高速或低速报警设置
(080830141830AP12 H050L030 )
设置车速上限为50km/h,下限为30km/h.。上限为000表示取消上限报警，下限为000表示取消下限报警。
'''
class MsgAom_SpeedLimitSet_5(MessageBase):
	def __init__(self):
		MessageBase.__init__(self,'aom_speedlimit_set_5')
		self.attrs['aoid'] = None	#ao对象
		self.attrs['high'] = 0  #上传间隔 (s) 0 表示取消等时上传
		self.attrs['low'] = 0 #时常 (s)


'''
电路控制信号
'''
class MsgAom_PowerSet_5(MessageBase):
	def __init__(self):
		MessageBase.__init__(self,'aom_power_set_5')
		self.attrs['aoid'] = None	#ao对象
		self.attrs['value'] = 0  #“1”表示开电路，“0”表示关电路

'''
油路控制信号
'''
class MsgAom_OilSet_5(MessageBase):
	def __init__(self):
		MessageBase.__init__(self,'aom_oil_set_5')
		self.attrs['aoid'] = None	#ao对象
		self.attrs['value'] = 0  #“1”表示开油路，“0”表示关油路。
		
'''
控制设备重启消息
(080830141830AT00)
'''
class MsgAom_Reset_5(MessageBase):
	def __init__(self,aoid = None):
		MessageBase.__init__(self,'aom_reset_5')
		self.attrs['aoid'] = aoid	#ao对象
		
'''
设置ACC开发送数据间隔
(080830141830AR050014)
在ACC开的时候20秒传一次数据。
'''
class MsgAom_AccOnContinuedSet_5(MessageBase):
	def __init__(self):
		MessageBase.__init__(self,'aom_accon_continued_5')
		self.attrs['aoid'] = None	#ao对象
		self.attrs['value'] = 0 
'''
设置ACC关发送数据间隔
(080830141830AR06003C)
在ACC关的时候60秒传一次数据。
'''
class MsgAom_AccOffContinuedSet_5(MessageBase):
	def __init__(self):
		MessageBase.__init__(self,'aom_accoff_continued_5')
		self.attrs['aoid'] = None	#ao对象
		self.attrs['value'] = 0 

'''
设置电子围栏消息
(080830141830AX051, N,2245.318,2246.452,E,11233.232,11355.175)
设置出界电子围栏，纬度下限为22度45．318分，纬度上限为２２度４６．４５２分．经度下限为１１２度３３．２３２分，经度上限为１１３度55．１７５分．
'''
class MsgAom_BarrierSet_5(MessageBase):
	def __init__(self):
		MessageBase.__init__(self,'aom_barrier_set_5')
		self.attrs['aoid'] = None	#ao对象

		
'''
取消所有报警消息
（081129141830AV02）	
响应：	BS21	
'''
class MsgAom_ClearAlarms_5(MessageBase):
	def __init__(self):
		MessageBase.__init__(self,'aom_clear_alarms_5')
		self.attrs['aoid'] = None	#ao对象

'''
里程清零消息
（081129141830AX01）	
响应：	BS04	
'''
class MsgAom_ClearMiles_5(MessageBase):
	def __init__(self):
		MessageBase.__init__(self,'aom_clear_miles_5')
		self.attrs['aoid'] = None	#ao对象


'''
里程初始化消息
（081129141830AX030000ABCD）
表示设置初始里程为A * 0x1000 + B * 0x100 + C * 0x10 + D = 43.981公里。
'''
class MsgAom_InitMiles_5(MessageBase):
	def __init__(self):
		MessageBase.__init__(self,'aom_init_miles_5')
		self.attrs['aoid'] = None	#ao对象
		self.attrs['miles']=0 	#单位: meter


	
#
#
#'''
#主动拨打进行监听，并数字化录音
#'''
#class MsgAom_set_DigitListen_begin_5(MessageBase):
#	def __init__(self):
#		MessageBase.__init__(self,'aom_set_listen_begin_5')
#		self.attrs['aoid'] = None	#ao对象
#		self.attrs['phone']=''		#监听拨打的电话号码
#
#'''
#主动拨打进行监听，并数字化录音
#'''
#class MsgAom_set_DigitListen_end_5(MessageBase):
#	def __init__(self):
#		MessageBase.__init__(self,'aom_set_listen_end_5')
#		self.attrs['aoid'] = None	#ao对象		
#
#


# _9 传递到报警系统的报警消息

##报警配置项改变
##系统必须检查与此报警项目关联的ao对象的报警条目，触发则必须重新加载配置项
#class MsgSys_AlarmSettingChanged_9(MessageBase):
#	def __init__(self):
#		MessageBase.__init__(self,'sys_alarmsetting_changed_9')
#		self.attrs['id'] = None	#ao对象
#		self.attrs['reason']= 'create' # create,update,delete 	#单位: meter

# ao对象添加或者删除报警配置策略
# 需通知后台报警服务器 alertServer
class MsgSys_AsiAttachAo_9(MessageBase):
	def __init__(self):
		MessageBase.__init__(self,'sys_asi_attach_ao_9')
		self.attrs['aoid'] = None	#aoid
		self.attrs['asid'] = None #报警配置项

class MsgSys_AsiDetachAo_9(MessageBase):
	def __init__(self):
		MessageBase.__init__(self,'sys_asi_detach_ao_9')
		self.attrs['aoid'] = None	#aoid
		self.attrs['asid'] = None #报警配置项

#如果ao的通信参数改变，需要unload之后再load
#通知das服务器加载ao对象
class MsgAo_DasLoad_6(MessageBase):
	def __init__(self):
		MessageBase.__init__(self,'ao_das_load_6')
		self.attrs['aoid'] = None

#通知das服务器卸载ao对象
class MsgAo_DasUnload_6(MessageBase):
	def __init__(self):
		MessageBase.__init__(self,'ao_das_unload_6')
		self.attrs['aoid'] = None
		self.attrs['dasid'] = None


#报警消息从报警服务器产生，并传送到dgw->flex user
# _10
class MsgAoAlarm_Trigger_10(MessageBase):
	def __init__(self):
		MessageBase.__init__(self,'ao_alarm_trigger_10')
		self.attrs['aoid'] = None
		self.attrs['aoname'] = None
		self.attrs['asiname'] =''   # 报警条目项名称

		self.attrs['time'] = None   #触发时间
		self.attrs['filter']=''     #触发条件

#报警产生执行联动操作
class MsgAoAlarm_Action_10(MessageBase):
	def __init__(self):
		MessageBase.__init__(self,'ao_alarm_trigger_10')
		self.attrs['aoid'] = None
		self.attrs['aoname'] = None
		self.attrs['asiname'] ='' # 报警条目项名称
		self.attrs['time'] = None
		self.attrs['type']='' #报警动作 mail,sms
		self.attrs['text']='' #联动动作的内容


#报警产生短信消息
#发送短信
class Msg_SMS_Put_11(MessageBase):
	def __init__(self):
		MessageBase.__init__(self,'sms_put_11')
		self.attrs['id'] = 0    #记录编号
		self.attrs['target'] = ''   #目标电话
		self.attrs['content'] =''   # 消息内容

#发送短信 结果反馈
class Msg_SMS_SendResult_11(MessageBase):
	def __init__(self):
		MessageBase.__init__(self,'sms_sendresult_11')
		self.attrs['id'] = 0    #记录编号
		self.attrs['from_id'] = ''   #短信发送者
		self.attrs['succ'] =False   # 成功还是失败
		self.attrs['msg'] = ''      #发送结果描述


#请求短信
class Msg_SMS_Get_11(MessageBase):
	def __init__(self):
		MessageBase.__init__(self,'sms_get_11')
		self.attrs['from_id'] = ''    #发送短信的请求者编号


class Msg_Keepalive_11(message.MessageBase):
	def __init__(self):
		message.MessageBase.__init__(self,'keepalive_11')
		self.attrs['id']=''	#

