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
	
	public class IAuthServicePrx extends RpcProxyBase{
		//# -- INTERFACE PROXY -- 
		public var delta:Object = null;
		
		public function  IAuthServicePrx(conn:RpcConnection){
			this.conn = conn;
		}		
		public static function create(host:String,port:int):IAuthServicePrx{
			var conn:RpcConnection = new RpcConnection();
			conn.open(host,port);
			var prx:IAuthServicePrx = new IAuthServicePrx(conn);
			return prx;
		}		
		public static function createWithProxy(proxy:RpcProxyBase):IAuthServicePrx{
			var prx:IAuthServicePrx = new IAuthServicePrx(proxy.conn);
			return prx;
		}		
		
		
		public function userAuth(user_:String,passwd_:String,loginType_:int,async:Function = null,extra:RpcExtraData=null):int{
			//# function index: 0
			
			var r:Boolean = false;
			try{
				var ecode:int = tcelib.RpcConsts.RPCERROR_SUCC;
				ecode = tcelib.RpcConsts.RPCERROR_SUCC;
				var m:tcelib.RpcMessageCall = new tcelib.RpcMessageCall();
				m.ifidx = 3;
				m.opidx = 0;
				if( extra!=null){
					m.extra = extra;
				}				
			var d:ByteArray;
			d = new ByteArray();
			var bytes_26:ByteArray = new ByteArray();
			bytes_26.writeUTFBytes(user_);
			d.writeInt(bytes_26.length);
			d.writeBytes(bytes_26);
			m.addParam(d);
			d = new ByteArray();
			var bytes_27:ByteArray = new ByteArray();
			bytes_27.writeUTFBytes(passwd_);
			d.writeInt(bytes_27.length);
			d.writeBytes(bytes_27);
			m.addParam(d);
			d = new ByteArray();
			d.writeInt(loginType_);
			m.addParam(d);
			m.prx = this as Object;
			m.async = async;
			m.asyncparser = this.userAuth_asyncparser as Function;
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
	
	private  function userAuth_asyncparser(m:RpcMessage,m2:RpcMessage):void{
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
			var _p:String = "";
			{			
				var _d:uint = 0;
				_d = d.readUnsignedInt();
				_p = d.readUTFBytes(_d);
			}			
			user(_p,this);
		}catch(e:Error){
			trace(e.toString());
			return ;
		}		
	}	
	
}

}