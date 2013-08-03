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
	
	public class IUserServicePrx extends RpcProxyBase{
		//# -- INTERFACE PROXY -- 
		public var delta:Object = null;
		
		public function  IUserServicePrx(conn:RpcConnection){
			this.conn = conn;
		}		
		public static function create(host:String,port:int):IUserServicePrx{
			var conn:RpcConnection = new RpcConnection();
			conn.open(host,port);
			var prx:IUserServicePrx = new IUserServicePrx(conn);
			return prx;
		}		
		public static function createWithProxy(proxy:RpcProxyBase):IUserServicePrx{
			var prx:IUserServicePrx = new IUserServicePrx(proxy.conn);
			return prx;
		}		
		
		
		public function userLogin(userid_:String,gwaid_:String,async:Function = null,extra:RpcExtraData=null):int{
			//# function index: 0
			
			var r:Boolean = false;
			try{
				var ecode:int = tcelib.RpcConsts.RPCERROR_SUCC;
				ecode = tcelib.RpcConsts.RPCERROR_SUCC;
				var m:tcelib.RpcMessageCall = new tcelib.RpcMessageCall();
				m.ifidx = 2;
				m.opidx = 0;
				if( extra!=null){
					m.extra = extra;
				}				
			var d:ByteArray;
			d = new ByteArray();
			var bytes_22:ByteArray = new ByteArray();
			bytes_22.writeUTFBytes(userid_);
			d.writeInt(bytes_22.length);
			d.writeBytes(bytes_22);
			m.addParam(d);
			d = new ByteArray();
			var bytes_23:ByteArray = new ByteArray();
			bytes_23.writeUTFBytes(gwaid_);
			d.writeInt(bytes_23.length);
			d.writeBytes(bytes_23);
			m.addParam(d);
			m.prx = this as Object;
			m.async = async;
			m.asyncparser = this.userLogin_asyncparser as Function;
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
	
	private  function userLogin_asyncparser(m:RpcMessage,m2:RpcMessage):void{
		//# function index: 0 , m2 - callreturn msg.
		
	}	
	
	
	public function userLogout(userid_:String,gwaid_:String,async:Function = null,extra:RpcExtraData=null):int{
		//# function index: 1
		
		var r:Boolean = false;
		try{
			var ecode:int = tcelib.RpcConsts.RPCERROR_SUCC;
			ecode = tcelib.RpcConsts.RPCERROR_SUCC;
			var m:tcelib.RpcMessageCall = new tcelib.RpcMessageCall();
			m.ifidx = 2;
			m.opidx = 1;
			if( extra!=null){
				m.extra = extra;
			}			
		var d:ByteArray;
		d = new ByteArray();
		var bytes_24:ByteArray = new ByteArray();
		bytes_24.writeUTFBytes(userid_);
		d.writeInt(bytes_24.length);
		d.writeBytes(bytes_24);
		m.addParam(d);
		d = new ByteArray();
		var bytes_25:ByteArray = new ByteArray();
		bytes_25.writeUTFBytes(gwaid_);
		d.writeInt(bytes_25.length);
		d.writeBytes(bytes_25);
		m.addParam(d);
		m.prx = this as Object;
		m.async = async;
		m.asyncparser = this.userLogout_asyncparser as Function;
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

private  function userLogout_asyncparser(m:RpcMessage,m2:RpcMessage):void{
	//# function index: 1 , m2 - callreturn msg.
	
}

}

}