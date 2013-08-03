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
	
	public class IGatewayAdapterPrx extends RpcProxyBase{
		//# -- INTERFACE PROXY -- 
		public var delta:Object = null;
		
		public function  IGatewayAdapterPrx(conn:RpcConnection){
			this.conn = conn;
		}		
		public static function create(host:String,port:int):IGatewayAdapterPrx{
			var conn:RpcConnection = new RpcConnection();
			conn.open(host,port);
			var prx:IGatewayAdapterPrx = new IGatewayAdapterPrx(conn);
			return prx;
		}		
		public static function createWithProxy(proxy:RpcProxyBase):IGatewayAdapterPrx{
			var prx:IGatewayAdapterPrx = new IGatewayAdapterPrx(proxy.conn);
			return prx;
		}		
		
		
		public function login(token_:String,async:Function = null,extra:RpcExtraData=null):int{
			//# function index: 0
			
			var r:Boolean = false;
			try{
				var ecode:int = tcelib.RpcConsts.RPCERROR_SUCC;
				ecode = tcelib.RpcConsts.RPCERROR_SUCC;
				var m:tcelib.RpcMessageCall = new tcelib.RpcMessageCall();
				m.ifidx = 1;
				m.opidx = 0;
				if( extra!=null){
					m.extra = extra;
				}				
			var d:ByteArray;
			d = new ByteArray();
			var bytes_21:ByteArray = new ByteArray();
			bytes_21.writeUTFBytes(token_);
			d.writeInt(bytes_21.length);
			d.writeBytes(bytes_21);
			m.addParam(d);
			m.prx = this as Object;
			m.async = async;
			m.asyncparser = this.login_asyncparser as Function;
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
	
	private  function login_asyncparser(m:RpcMessage,m2:RpcMessage):void{
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
			var _p:CallReturn_t = new CallReturn_t();
			_p.unmarshall(d);
			user(_p,this);
		}catch(e:Error){
			trace(e.toString());
			return ;
		}		
	}	
	
	
	public function logout(async:Function = null,extra:RpcExtraData=null):int{
		//# function index: 1
		
		var r:Boolean = false;
		try{
			var ecode:int = tcelib.RpcConsts.RPCERROR_SUCC;
			ecode = tcelib.RpcConsts.RPCERROR_SUCC;
			var m:tcelib.RpcMessageCall = new tcelib.RpcMessageCall();
			m.ifidx = 1;
			m.opidx = 1;
			if( extra!=null){
				m.extra = extra;
			}			
		var d:ByteArray;
		m.prx = this as Object;
		m.async = async;
		m.asyncparser = this.logout_asyncparser as Function;
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

private  function logout_asyncparser(m:RpcMessage,m2:RpcMessage):void{
	//# function index: 1 , m2 - callreturn msg.
	
}


public function heartbeat(async:Function = null,extra:RpcExtraData=null):int{
	//# function index: 2
	
	var r:Boolean = false;
	try{
		var ecode:int = tcelib.RpcConsts.RPCERROR_SUCC;
		ecode = tcelib.RpcConsts.RPCERROR_SUCC;
		var m:tcelib.RpcMessageCall = new tcelib.RpcMessageCall();
		m.ifidx = 1;
		m.opidx = 2;
		if( extra!=null){
			m.extra = extra;
		}		
	var d:ByteArray;
	m.prx = this as Object;
	m.async = async;
	m.asyncparser = this.heartbeat_asyncparser as Function;
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

private  function heartbeat_asyncparser(m:RpcMessage,m2:RpcMessage):void{
	//# function index: 2 , m2 - callreturn msg.
	
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
		var _p:int = 0;
		_p = d.readInt();
		user(_p,this);
	}catch(e:Error){
		trace(e.toString());
		return ;
	}	
}

}

}