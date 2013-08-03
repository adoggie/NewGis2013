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
	
	public class INotificationServicePrx extends RpcProxyBase{
		//# -- INTERFACE PROXY -- 
		public var delta:Object = null;
		
		public function  INotificationServicePrx(conn:RpcConnection){
			this.conn = conn;
		}		
		public static function create(host:String,port:int):INotificationServicePrx{
			var conn:RpcConnection = new RpcConnection();
			conn.open(host,port);
			var prx:INotificationServicePrx = new INotificationServicePrx(conn);
			return prx;
		}		
		public static function createWithProxy(proxy:RpcProxyBase):INotificationServicePrx{
			var prx:INotificationServicePrx = new INotificationServicePrx(proxy.conn);
			return prx;
		}		
		
		
		public function sendSMS(target_:String,content_:String,async:Function = null,extra:RpcExtraData=null):int{
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
			var bytes_28:ByteArray = new ByteArray();
			bytes_28.writeUTFBytes(target_);
			d.writeInt(bytes_28.length);
			d.writeBytes(bytes_28);
			m.addParam(d);
			d = new ByteArray();
			var bytes_29:ByteArray = new ByteArray();
			bytes_29.writeUTFBytes(content_);
			d.writeInt(bytes_29.length);
			d.writeBytes(bytes_29);
			m.addParam(d);
			m.prx = this as Object;
			m.async = async;
			m.asyncparser = this.sendSMS_asyncparser as Function;
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
	
	private  function sendSMS_asyncparser(m:RpcMessage,m2:RpcMessage):void{
		//# function index: 0 , m2 - callreturn msg.
		
	}	
	
	
	public function sendMail(target_:String,content_:String,async:Function = null,extra:RpcExtraData=null):int{
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
		var bytes_30:ByteArray = new ByteArray();
		bytes_30.writeUTFBytes(target_);
		d.writeInt(bytes_30.length);
		d.writeBytes(bytes_30);
		m.addParam(d);
		d = new ByteArray();
		var bytes_31:ByteArray = new ByteArray();
		bytes_31.writeUTFBytes(content_);
		d.writeInt(bytes_31.length);
		d.writeBytes(bytes_31);
		m.addParam(d);
		m.prx = this as Object;
		m.async = async;
		m.asyncparser = this.sendMail_asyncparser as Function;
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

private  function sendMail_asyncparser(m:RpcMessage,m2:RpcMessage):void{
	//# function index: 1 , m2 - callreturn msg.
	
}

}

}