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
	
	public class ITaskServicePrx extends RpcProxyBase{
		//# -- INTERFACE PROXY -- 
		public var delta:Object = null;
		
		public function  ITaskServicePrx(conn:RpcConnection){
			this.conn = conn;
		}		
		public static function create(host:String,port:int):ITaskServicePrx{
			var conn:RpcConnection = new RpcConnection();
			conn.open(host,port);
			var prx:ITaskServicePrx = new ITaskServicePrx(conn);
			return prx;
		}		
		public static function createWithProxy(proxy:RpcProxyBase):ITaskServicePrx{
			var prx:ITaskServicePrx = new ITaskServicePrx(proxy.conn);
			return prx;
		}		
		
		
		public function getProps(async:Function = null,extra:RpcExtraData=null):int{
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
			m.prx = this as Object;
			m.async = async;
			m.asyncparser = this.getProps_asyncparser as Function;
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
	
	private  function getProps_asyncparser(m:RpcMessage,m2:RpcMessage):void{
		//# function index: 0 , m2 - callreturn msg.
		
		var stream:ByteArray;
		stream = m2.paramstream;
		var user:Function;
		user = m.async;
		if(m2.errcode != tcelib.RpcConsts.RPCERROR_SUCC) return; 
		if(stream.length == 0){ 
			user(this);
			return;
		}		
		try{
			var d:ByteArray;
			d = stream;
			var _p:HashMap = new HashMap();
			var _c:Properties_thlp = new Properties_thlp(_p);
			_c.marshall(d);
			user(_p,this);
		}catch(e:Error){
			trace(e.toString());
			return ;
		}		
	}	
	
}

}