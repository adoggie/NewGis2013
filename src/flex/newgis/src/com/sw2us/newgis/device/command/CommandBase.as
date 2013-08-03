package com.sw2us.newgis.device.command
{
	public class CommandBase
	{
		protected var _cmd:Object;
		protected var _type:int;
		
		public function CommandBase(type:int)
		{
			_cmd = new Object();
			_type = type;
		}
		
		public function get command():Object{
			return _cmd;
		}
		
		public function get type():int{
			return _type;
		}
		
		public static const AOCTRL_CMD_SAMPLING_TIMESET:int = 3;
		public static const AOCTRL_CMD_NAMED:int= 5;
		public static const AOCTRL_CMD_SPEEDSET:int=6;
		public static const AOCTRL_CMD_POWER_ONOFF:int=7;
		public static const AOCTRL_CMD_OIL_ONOFF:int = 8;
		public static const AOCTRL_CMD_REBOOT:int = 9;
		public static const AOCTRL_CMD_ACC_ON_TIME:int = 10;
		public static const AOCTRL_CMD_ACC_OFF_TIME:int = 11;
		public static const AOCTRL_CMD_BARRIER_SET:int = 12;
		public static const AOCTRL_CMD_LISTEN_START:int = 14;
		public static const AOCTRL_CMD_COMMADDR_SET:int = 15;
		public static const AOCTRL_CMD_APN_SET:int = 16;
		public static const AOCTRL_CMD_GET_VERSION:int = 17;
		public static const AOCTRL_CMD_CLEAR_ALARMS:int = 18;
		public static const AOCTRL_CMD_CLEAR_MILES:int = 19;
		public static const AOCTRL_CMD_INIT_MILES:int = 20;
		public static const AOCTRL_CMD_UPDATING:int = 21;
		
	}
}

/*
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

*/