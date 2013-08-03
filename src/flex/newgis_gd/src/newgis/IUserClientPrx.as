package newgis{

	import tcelib.RpcConsts;
	import tcelib.RpcConnection;
	import tcelib.utils.HashMap;
	import flash.utils.ByteArray;
	import flash.utils.Endian;
	import tcelib.utils.HashMapEntry;
	
	import tcelib.RpcProxyBase;
	import tcelib.RpcMessageCall;
	import tcelib.RpcMessage;
	import tcelib.RpcExtraData;
	
	public class IUserClientPrx extends RpcProxyBase{
		//# -- INTERFACE PROXY -- 
		public var delta:Object = null;
		
		public function  IUserClientPrx(conn:RpcConnection){
			this.conn = conn;
		}		
		public static function create(host:String,port:int):IUserClientPrx{
			var conn:RpcConnection = new RpcConnection();
			conn.open(host,port);
			var prx:IUserClientPrx = new IUserClientPrx(conn);
			return prx;
		}		
		public static function createWithProxy(proxy:RpcProxyBase):IUserClientPrx{
			var prx:IUserClientPrx = new IUserClientPrx(proxy.conn);
			return prx;
		}		
		
		
		public function onGetLocation(aoid_:String,loc_:LocationInfo_t,async:Function = null,extra:RpcExtraData=null):int{
			//# function index: 0
			
			var r:Boolean = false;
			try{
				var ecode:int = tcelib.RpcConsts.RPCERROR_SUCC;
				ecode = tcelib.RpcConsts.RPCERROR_SUCC;
				var m:tcelib.RpcMessageCall = new tcelib.RpcMessageCall();
				m.ifidx = 0;
				m.opidx = 0;
				if( extra!=null){
					m.extra = extra;
				}				
			var d:ByteArray;
			d = new ByteArray();
			var bytes_18:ByteArray = new ByteArray();
			bytes_18.writeUTFBytes(aoid_);
			d.writeInt(bytes_18.length);
			d.writeBytes(bytes_18);
			m.addParam(d);
			d = new ByteArray();
			loc_.marshall(d);
			m.addParam(d);
			m.prx = this as Object;
			m.async = async;
			m.asyncparser = this.onGetLocation_asyncparser as Function;
			r = this.conn.sendMessage(m);
			if(!r){
				ecode = tcelib.RpcConsts.RPCERROR_SENDFAILED;
				return ecode;
			}			
		}catch(e:Error){
			return tcelib.RpcConsts.RPCERROR_DATADIRTY;
		}		
		return tcelib.RpcConsts.RPCERROR_SUCC;
	}	
	
	private  function onGetLocation_asyncparser(m:RpcMessage,m2:RpcMessage):void{
		//# function index: 0 , m2 - callreturn msg.
		
	}	
	
	
	public function onGetMessage(userid_:String,msg_:MessageText_t,async:Function = null,extra:RpcExtraData=null):int{
		//# function index: 1
		
		var r:Boolean = false;
		try{
			var ecode:int = tcelib.RpcConsts.RPCERROR_SUCC;
			ecode = tcelib.RpcConsts.RPCERROR_SUCC;
			var m:tcelib.RpcMessageCall = new tcelib.RpcMessageCall();
			m.ifidx = 0;
			m.opidx = 1;
			if( extra!=null){
				m.extra = extra;
			}			
		var d:ByteArray;
		d = new ByteArray();
		var bytes_19:ByteArray = new ByteArray();
		bytes_19.writeUTFBytes(userid_);
		d.writeInt(bytes_19.length);
		d.writeBytes(bytes_19);
		m.addParam(d);
		d = new ByteArray();
		msg_.marshall(d);
		m.addParam(d);
		m.prx = this as Object;
		m.async = async;
		m.asyncparser = this.onGetMessage_asyncparser as Function;
		r = this.conn.sendMessage(m);
		if(!r){
			ecode = tcelib.RpcConsts.RPCERROR_SENDFAILED;
			return ecode;
		}		
	}catch(e:Error){
		return tcelib.RpcConsts.RPCERROR_DATADIRTY;
	}	
	return tcelib.RpcConsts.RPCERROR_SUCC;
}

private  function onGetMessage_asyncparser(m:RpcMessage,m2:RpcMessage):void{
	//# function index: 1 , m2 - callreturn msg.
	
}


public function onGetDeviceAlarm(aoid_:String,alarm_:AlarmInfo_t,async:Function = null,extra:RpcExtraData=null):int{
	//# function index: 2
	
	var r:Boolean = false;
	try{
		var ecode:int = tcelib.RpcConsts.RPCERROR_SUCC;
		ecode = tcelib.RpcConsts.RPCERROR_SUCC;
		var m:tcelib.RpcMessageCall = new tcelib.RpcMessageCall();
		m.ifidx = 0;
		m.opidx = 2;
		if( extra!=null){
			m.extra = extra;
		}		
	var d:ByteArray;
	d = new ByteArray();
	var bytes_20:ByteArray = new ByteArray();
	bytes_20.writeUTFBytes(aoid_);
	d.writeInt(bytes_20.length);
	d.writeBytes(bytes_20);
	m.addParam(d);
	d = new ByteArray();
	alarm_.marshall(d);
	m.addParam(d);
	m.prx = this as Object;
	m.async = async;
	m.asyncparser = this.onGetDeviceAlarm_asyncparser as Function;
	r = this.conn.sendMessage(m);
	if(!r){
		ecode = tcelib.RpcConsts.RPCERROR_SENDFAILED;
		return ecode;
	}	
}catch(e:Error){
	return tcelib.RpcConsts.RPCERROR_DATADIRTY;
}
return tcelib.RpcConsts.RPCERROR_SUCC;
}

private  function onGetDeviceAlarm_asyncparser(m:RpcMessage,m2:RpcMessage):void{
	//# function index: 2 , m2 - callreturn msg.
	
}

}

}