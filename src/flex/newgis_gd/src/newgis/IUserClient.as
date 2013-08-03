package newgis{

	import tcelib.RpcConsts;
	import tcelib.RpcConnection;
	import tcelib.utils.HashMap;
	import flash.utils.ByteArray;
	import flash.utils.Endian;
	import tcelib.utils.HashMapEntry;
	
	import tcelib.RpcServant;
	import tcelib.RpcContext;
	import newgis.IUserClient_delegate;
	
	public class IUserClient extends RpcServant{
		//# -- INTERFACE -- 
		public function IUserClient(){
			this.delegate = new IUserClient_delegate(this);
		}		
		
		
		public function onGetLocation(aoid_:String,loc_:LocationInfo_t,ctx:RpcContext = null):void{
		}		
		
		public function onGetMessage(userid_:String,msg_:MessageText_t,ctx:RpcContext = null):void{
		}		
		
		public function onGetDeviceAlarm(aoid_:String,alarm_:AlarmInfo_t,ctx:RpcContext = null):void{
		}		
	}	

}