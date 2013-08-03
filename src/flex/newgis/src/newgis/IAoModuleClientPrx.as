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
	
	public class IAoModuleClientPrx extends RpcProxyBase{
		//# -- INTERFACE PROXY -- 
		public var delta:Object = null;
		
		public function  IAoModuleClientPrx(conn:RpcConnection){
			this.conn = conn;
		}		
		public static function create(host:String,port:int):IAoModuleClientPrx{
			var conn:RpcConnection = new RpcConnection();
			conn.open(host,port);
			var prx:IAoModuleClientPrx = new IAoModuleClientPrx(conn);
			return prx;
		}		
		public static function createWithProxy(proxy:RpcProxyBase):IAoModuleClientPrx{
			var prx:IAoModuleClientPrx = new IAoModuleClientPrx(proxy.conn);
			return prx;
		}		
		
		
		public function onGetGpsData(aoid_:String,gps_:GpsData_t,async:Function = null,extra:RpcExtraData=null):int{
			//# function index: 0
			
			var r:Boolean = false;
			try{
				var ecode:int = tcelib.RpcConsts.RPCERROR_SUCC;
				ecode = tcelib.RpcConsts.RPCERROR_SUCC;
				var m:tcelib.RpcMessageCall = new tcelib.RpcMessageCall();
				m.ifidx = None;
				m.opidx = 0;
				if( extra!=null){
					m.extra = extra;
				}				
			var d:ByteArray;
			d = new ByteArray();
			var bytes_34:ByteArray = new ByteArray();
			bytes_34.writeUTFBytes(aoid_);
			d.writeInt(bytes_34.length);
			d.writeBytes(bytes_34);
			m.addParam(d);
			d = new ByteArray();
			gps_.marshall(d);
			m.addParam(d);
			m.prx = this as Object;
			m.async = async;
			m.asyncparser = this.onGetGpsData_asyncparser as Function;
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
	
	private  function onGetGpsData_asyncparser(m:RpcMessage,m2:RpcMessage):void{
		//# function index: 0 , m2 - callreturn msg.
		
	}	
	
	
	public function onGetAlarm(aoid_:String,alarm_:AlarmInfo_t,async:Function = null,extra:RpcExtraData=null):int{
		//# function index: 1
		
		var r:Boolean = false;
		try{
			var ecode:int = tcelib.RpcConsts.RPCERROR_SUCC;
			ecode = tcelib.RpcConsts.RPCERROR_SUCC;
			var m:tcelib.RpcMessageCall = new tcelib.RpcMessageCall();
			m.ifidx = None;
			m.opidx = 1;
			if( extra!=null){
				m.extra = extra;
			}			
		var d:ByteArray;
		d = new ByteArray();
		var bytes_35:ByteArray = new ByteArray();
		bytes_35.writeUTFBytes(aoid_);
		d.writeInt(bytes_35.length);
		d.writeBytes(bytes_35);
		m.addParam(d);
		d = new ByteArray();
		alarm_.marshall(d);
		m.addParam(d);
		m.prx = this as Object;
		m.async = async;
		m.asyncparser = this.onGetAlarm_asyncparser as Function;
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

private  function onGetAlarm_asyncparser(m:RpcMessage,m2:RpcMessage):void{
	//# function index: 1 , m2 - callreturn msg.
	
}


public function onModuleData(json_:String,async:Function = null,extra:RpcExtraData=null):int{
	//# function index: 2
	
	var r:Boolean = false;
	try{
		var ecode:int = tcelib.RpcConsts.RPCERROR_SUCC;
		ecode = tcelib.RpcConsts.RPCERROR_SUCC;
		var m:tcelib.RpcMessageCall = new tcelib.RpcMessageCall();
		m.ifidx = None;
		m.opidx = 2;
		if( extra!=null){
			m.extra = extra;
		}		
	var d:ByteArray;
	d = new ByteArray();
	var bytes_36:ByteArray = new ByteArray();
	bytes_36.writeUTFBytes(json_);
	d.writeInt(bytes_36.length);
	d.writeBytes(bytes_36);
	m.addParam(d);
	m.prx = this as Object;
	m.async = async;
	m.asyncparser = this.onModuleData_asyncparser as Function;
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

private  function onModuleData_asyncparser(m:RpcMessage,m2:RpcMessage):void{
	//# function index: 2 , m2 - callreturn msg.
	
}

}

}