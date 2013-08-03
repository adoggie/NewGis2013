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
	
	public class IAlarmServicePrx extends RpcProxyBase{
		//# -- INTERFACE PROXY -- 
		public var delta:Object = null;
		
		public function  IAlarmServicePrx(conn:RpcConnection){
			this.conn = conn;
		}		
		public static function create(host:String,port:int):IAlarmServicePrx{
			var conn:RpcConnection = new RpcConnection();
			conn.open(host,port);
			var prx:IAlarmServicePrx = new IAlarmServicePrx(conn);
			return prx;
		}		
		public static function createWithProxy(proxy:RpcProxyBase):IAlarmServicePrx{
			var prx:IAlarmServicePrx = new IAlarmServicePrx(proxy.conn);
			return prx;
		}		
		
		
		public function addItem(aoid_:String,asid_:int,async:Function = null,extra:RpcExtraData=null):int{
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
			var bytes_32:ByteArray = new ByteArray();
			bytes_32.writeUTFBytes(aoid_);
			d.writeInt(bytes_32.length);
			d.writeBytes(bytes_32);
			m.addParam(d);
			d = new ByteArray();
			d.writeInt(asid_);
			m.addParam(d);
			m.prx = this as Object;
			m.async = async;
			m.asyncparser = this.addItem_asyncparser as Function;
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
	
	private  function addItem_asyncparser(m:RpcMessage,m2:RpcMessage):void{
		//# function index: 0 , m2 - callreturn msg.
		
	}	
	
	
	public function removeItem(aoid_:String,asid_:int,async:Function = null,extra:RpcExtraData=null):int{
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
		var bytes_33:ByteArray = new ByteArray();
		bytes_33.writeUTFBytes(aoid_);
		d.writeInt(bytes_33.length);
		d.writeBytes(bytes_33);
		m.addParam(d);
		d = new ByteArray();
		d.writeInt(asid_);
		m.addParam(d);
		m.prx = this as Object;
		m.async = async;
		m.asyncparser = this.removeItem_asyncparser as Function;
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

private  function removeItem_asyncparser(m:RpcMessage,m2:RpcMessage):void{
	//# function index: 1 , m2 - callreturn msg.
	
}

}

}