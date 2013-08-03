package com.sw2us.newgis
{
	import newgis.AlarmInfo_t;
	import newgis.IUserClient;
	import newgis.LocationInfo_t;
	import newgis.MessageText_t;
	
	
	
	import tcelib.RpcContext;
	
	public class UserClientImpl extends IUserClient
	{
		public function UserClientImpl()
		{
			super();
		}
		
		override public function onGetDeviceAlarm(aoid_:String, alarm_:AlarmInfo_t, ctx:RpcContext=null):void
		{
			// TODO Auto Generated method stub
			super.onGetDeviceAlarm(aoid_, alarm_, ctx);
		}
		
		override public function onGetLocation(aoid_:String, loc_:LocationInfo_t, ctx:RpcContext=null):void
		{
			// TODO Auto Generated method stub
			super.onGetLocation(aoid_, loc_, ctx);
			AppCore.instance().getAoCollector().pushGpsData(aoid_,loc_);
		}
		
		override public function onGetMessage(userid_:String, msg_:MessageText_t, ctx:RpcContext=null):void
		{
			// TODO Auto Generated method stub
			super.onGetMessage(userid_, msg_, ctx);
		}
		
		
	}
}