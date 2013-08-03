package newgis{

	import tcelib.RpcConsts;
	import tcelib.RpcConnection;
	import tcelib.utils.HashMap;
	import flash.utils.ByteArray;
	import flash.utils.Endian;
	import tcelib.utils.HashMapEntry;
	
	import tcelib.*;
	import tcelib.utils.HashMap;
	import flash.utils.ByteArray;
	import flash.utils.Endian;
	import tcelib.RpcServantDelegate;
	
	public class IUserClient_delegate extends RpcServantDelegate {
		
		public var conn:RpcConnection = null;
		
		public function IUserClient_delegate(inst:IUserClient,adapter:RpcCommAdapter=null,conn:RpcConnection=null){
			this.adapter = adapter;
			this.index = 0;
			this.optlist.put(0,this.onGetLocation);
			this.optlist.put(1,this.onGetMessage);
			this.optlist.put(2,this.onGetDeviceAlarm);
			this.inst = inst;
		}		
		
		public function onGetLocation(ctx:RpcContext = null):Boolean{
			var d:ByteArray;
			d = ctx.msg.paramstream; 
			var r:Boolean = false;
			var aoid_:String;
			{			
				var _d:uint = 0;
				_d = d.readUnsignedInt();
				aoid_ = d.readUTFBytes(_d);
			}			
			var loc_:LocationInfo_t = new LocationInfo_t();
			r = loc_.unmarshall(d);
			if(!r) return false;
			var servant:IUserClient = this.inst as IUserClient;
			servant.onGetLocation(aoid_,loc_,ctx)
			if( ctx.msg.calltype & tcelib.RpcMessage.CALL_ONE_WAY){
				return false;
			}			
			
			d = new ByteArray();
			d.endian = Endian.BIG_ENDIAN;
			var m:RpcMessageReturn = new RpcMessageReturn();
			m.sequence = ctx.msg.sequence;
			if(d.length) m.addParam(d);
			ctx.conn.sendMessage(m);
			return true;
		}		
		
		public function onGetMessage(ctx:RpcContext = null):Boolean{
			var d:ByteArray;
			d = ctx.msg.paramstream; 
			var r:Boolean = false;
			var userid_:String;
			{			
				var _d:uint = 0;
				_d = d.readUnsignedInt();
				userid_ = d.readUTFBytes(_d);
			}			
			var msg_:MessageText_t = new MessageText_t();
			r = msg_.unmarshall(d);
			if(!r) return false;
			var servant:IUserClient = this.inst as IUserClient;
			servant.onGetMessage(userid_,msg_,ctx)
			if( ctx.msg.calltype & tcelib.RpcMessage.CALL_ONE_WAY){
				return false;
			}			
			
			d = new ByteArray();
			d.endian = Endian.BIG_ENDIAN;
			var m:RpcMessageReturn = new RpcMessageReturn();
			m.sequence = ctx.msg.sequence;
			if(d.length) m.addParam(d);
			ctx.conn.sendMessage(m);
			return true;
		}		
		
		public function onGetDeviceAlarm(ctx:RpcContext = null):Boolean{
			var d:ByteArray;
			d = ctx.msg.paramstream; 
			var r:Boolean = false;
			var aoid_:String;
			{			
				var _d:uint = 0;
				_d = d.readUnsignedInt();
				aoid_ = d.readUTFBytes(_d);
			}			
			var alarm_:AlarmInfo_t = new AlarmInfo_t();
			r = alarm_.unmarshall(d);
			if(!r) return false;
			var servant:IUserClient = this.inst as IUserClient;
			servant.onGetDeviceAlarm(aoid_,alarm_,ctx)
			if( ctx.msg.calltype & tcelib.RpcMessage.CALL_ONE_WAY){
				return false;
			}			
			
			d = new ByteArray();
			d.endian = Endian.BIG_ENDIAN;
			var m:RpcMessageReturn = new RpcMessageReturn();
			m.sequence = ctx.msg.sequence;
			if(d.length) m.addParam(d);
			ctx.conn.sendMessage(m);
			return true;
		}		
		
	}	

}