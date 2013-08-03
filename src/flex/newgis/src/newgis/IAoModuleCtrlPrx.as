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
	
	public class IAoModuleCtrlPrx extends RpcProxyBase{
		//# -- INTERFACE PROXY -- 
		public var delta:Object = null;
		
		public function  IAoModuleCtrlPrx(conn:RpcConnection){
			this.conn = conn;
		}		
		public static function create(host:String,port:int):IAoModuleCtrlPrx{
			var conn:RpcConnection = new RpcConnection();
			conn.open(host,port);
			var prx:IAoModuleCtrlPrx = new IAoModuleCtrlPrx(conn);
			return prx;
		}		
		public static function createWithProxy(proxy:RpcProxyBase):IAoModuleCtrlPrx{
			var prx:IAoModuleCtrlPrx = new IAoModuleCtrlPrx(proxy.conn);
			return prx;
		}		
		
		
		public function openListen(aoid_:String,phone_:String,async:Function = null,extra:RpcExtraData=null):int{
			//# function index: 0
			
			var r:Boolean = false;
			try{
				var ecode:int = tcelib.RpcConsts.RPCERROR_SUCC;
				ecode = tcelib.RpcConsts.RPCERROR_SUCC;
				var m:tcelib.RpcMessageCall = new tcelib.RpcMessageCall();
				m.ifidx = 9;
				m.opidx = 0;
				if( extra!=null){
					m.extra = extra;
				}				
			var d:ByteArray;
			d = new ByteArray();
			var bytes_28:ByteArray = new ByteArray();
			bytes_28.writeUTFBytes(aoid_);
			d.writeInt(bytes_28.length);
			d.writeBytes(bytes_28);
			m.addParam(d);
			d = new ByteArray();
			var bytes_29:ByteArray = new ByteArray();
			bytes_29.writeUTFBytes(phone_);
			d.writeInt(bytes_29.length);
			d.writeBytes(bytes_29);
			m.addParam(d);
			m.prx = this as Object;
			m.async = async;
			m.asyncparser = this.openListen_asyncparser as Function;
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
	
	private  function openListen_asyncparser(m:RpcMessage,m2:RpcMessage):void{
		//# function index: 0 , m2 - callreturn msg.
		
	}	
	
	
	public function closeListen(aoid_:String,async:Function = null,extra:RpcExtraData=null):int{
		//# function index: 1
		
		var r:Boolean = false;
		try{
			var ecode:int = tcelib.RpcConsts.RPCERROR_SUCC;
			ecode = tcelib.RpcConsts.RPCERROR_SUCC;
			var m:tcelib.RpcMessageCall = new tcelib.RpcMessageCall();
			m.ifidx = 9;
			m.opidx = 1;
			if( extra!=null){
				m.extra = extra;
			}			
		var d:ByteArray;
		d = new ByteArray();
		var bytes_30:ByteArray = new ByteArray();
		bytes_30.writeUTFBytes(aoid_);
		d.writeInt(bytes_30.length);
		d.writeBytes(bytes_30);
		m.addParam(d);
		m.prx = this as Object;
		m.async = async;
		m.asyncparser = this.closeListen_asyncparser as Function;
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

private  function closeListen_asyncparser(m:RpcMessage,m2:RpcMessage):void{
	//# function index: 1 , m2 - callreturn msg.
	
}


public function getVersion(aoid_:String,async:Function = null,extra:RpcExtraData=null):int{
	//# function index: 2
	
	var r:Boolean = false;
	try{
		var ecode:int = tcelib.RpcConsts.RPCERROR_SUCC;
		ecode = tcelib.RpcConsts.RPCERROR_SUCC;
		var m:tcelib.RpcMessageCall = new tcelib.RpcMessageCall();
		m.ifidx = 9;
		m.opidx = 2;
		if( extra!=null){
			m.extra = extra;
		}		
	var d:ByteArray;
	d = new ByteArray();
	var bytes_31:ByteArray = new ByteArray();
	bytes_31.writeUTFBytes(aoid_);
	d.writeInt(bytes_31.length);
	d.writeBytes(bytes_31);
	m.addParam(d);
	m.prx = this as Object;
	m.async = async;
	m.asyncparser = this.getVersion_asyncparser as Function;
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

private  function getVersion_asyncparser(m:RpcMessage,m2:RpcMessage):void{
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


public function onceNamed(aoid_:String,async:Function = null,extra:RpcExtraData=null):int{
	//# function index: 3
	
	var r:Boolean = false;
	try{
		var ecode:int = tcelib.RpcConsts.RPCERROR_SUCC;
		ecode = tcelib.RpcConsts.RPCERROR_SUCC;
		var m:tcelib.RpcMessageCall = new tcelib.RpcMessageCall();
		m.ifidx = 9;
		m.opidx = 3;
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
	m.prx = this as Object;
	m.async = async;
	m.asyncparser = this.onceNamed_asyncparser as Function;
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

private  function onceNamed_asyncparser(m:RpcMessage,m2:RpcMessage):void{
	//# function index: 3 , m2 - callreturn msg.
	
}


public function speedLimit(aoid_:String,high_:int,low_:int,async:Function = null,extra:RpcExtraData=null):int{
	//# function index: 4
	
	var r:Boolean = false;
	try{
		var ecode:int = tcelib.RpcConsts.RPCERROR_SUCC;
		ecode = tcelib.RpcConsts.RPCERROR_SUCC;
		var m:tcelib.RpcMessageCall = new tcelib.RpcMessageCall();
		m.ifidx = 9;
		m.opidx = 4;
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
	d.writeInt(high_);
	m.addParam(d);
	d = new ByteArray();
	d.writeInt(low_);
	m.addParam(d);
	m.prx = this as Object;
	m.async = async;
	m.asyncparser = this.speedLimit_asyncparser as Function;
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

private  function speedLimit_asyncparser(m:RpcMessage,m2:RpcMessage):void{
	//# function index: 4 , m2 - callreturn msg.
	
}


public function oilCtrl(aoid_:String,onoff_:Boolean,async:Function = null,extra:RpcExtraData=null):int{
	//# function index: 5
	
	var r:Boolean = false;
	try{
		var ecode:int = tcelib.RpcConsts.RPCERROR_SUCC;
		ecode = tcelib.RpcConsts.RPCERROR_SUCC;
		var m:tcelib.RpcMessageCall = new tcelib.RpcMessageCall();
		m.ifidx = 9;
		m.opidx = 5;
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
	if(onoff_ == true){
		d.writeByte(1);
	}else{
		d.writeByte(0);
	}	
	m.addParam(d);
	m.prx = this as Object;
	m.async = async;
	m.asyncparser = this.oilCtrl_asyncparser as Function;
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

private  function oilCtrl_asyncparser(m:RpcMessage,m2:RpcMessage):void{
	//# function index: 5 , m2 - callreturn msg.
	
}


public function reset(aoid_:String,async:Function = null,extra:RpcExtraData=null):int{
	//# function index: 6
	
	var r:Boolean = false;
	try{
		var ecode:int = tcelib.RpcConsts.RPCERROR_SUCC;
		ecode = tcelib.RpcConsts.RPCERROR_SUCC;
		var m:tcelib.RpcMessageCall = new tcelib.RpcMessageCall();
		m.ifidx = 9;
		m.opidx = 6;
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
	m.prx = this as Object;
	m.async = async;
	m.asyncparser = this.reset_asyncparser as Function;
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

private  function reset_asyncparser(m:RpcMessage,m2:RpcMessage):void{
	//# function index: 6 , m2 - callreturn msg.
	
}


public function setFreqAccOn(aoid_:String,freq_:int,async:Function = null,extra:RpcExtraData=null):int{
	//# function index: 7
	
	var r:Boolean = false;
	try{
		var ecode:int = tcelib.RpcConsts.RPCERROR_SUCC;
		ecode = tcelib.RpcConsts.RPCERROR_SUCC;
		var m:tcelib.RpcMessageCall = new tcelib.RpcMessageCall();
		m.ifidx = 9;
		m.opidx = 7;
		if( extra!=null){
			m.extra = extra;
		}		
	var d:ByteArray;
	d = new ByteArray();
	var bytes_36:ByteArray = new ByteArray();
	bytes_36.writeUTFBytes(aoid_);
	d.writeInt(bytes_36.length);
	d.writeBytes(bytes_36);
	m.addParam(d);
	d = new ByteArray();
	d.writeInt(freq_);
	m.addParam(d);
	m.prx = this as Object;
	m.async = async;
	m.asyncparser = this.setFreqAccOn_asyncparser as Function;
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

private  function setFreqAccOn_asyncparser(m:RpcMessage,m2:RpcMessage):void{
	//# function index: 7 , m2 - callreturn msg.
	
}


public function setFreqAccOff(aoid_:String,freq_:int,async:Function = null,extra:RpcExtraData=null):int{
	//# function index: 8
	
	var r:Boolean = false;
	try{
		var ecode:int = tcelib.RpcConsts.RPCERROR_SUCC;
		ecode = tcelib.RpcConsts.RPCERROR_SUCC;
		var m:tcelib.RpcMessageCall = new tcelib.RpcMessageCall();
		m.ifidx = 9;
		m.opidx = 8;
		if( extra!=null){
			m.extra = extra;
		}		
	var d:ByteArray;
	d = new ByteArray();
	var bytes_37:ByteArray = new ByteArray();
	bytes_37.writeUTFBytes(aoid_);
	d.writeInt(bytes_37.length);
	d.writeBytes(bytes_37);
	m.addParam(d);
	d = new ByteArray();
	d.writeInt(freq_);
	m.addParam(d);
	m.prx = this as Object;
	m.async = async;
	m.asyncparser = this.setFreqAccOff_asyncparser as Function;
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

private  function setFreqAccOff_asyncparser(m:RpcMessage,m2:RpcMessage):void{
	//# function index: 8 , m2 - callreturn msg.
	
}


public function setBarrierLeave(aoid_:String,x1_:Number,y1_:Number,x2_:Number,y2_:Number,async:Function = null,extra:RpcExtraData=null):int{
	//# function index: 9
	
	var r:Boolean = false;
	try{
		var ecode:int = tcelib.RpcConsts.RPCERROR_SUCC;
		ecode = tcelib.RpcConsts.RPCERROR_SUCC;
		var m:tcelib.RpcMessageCall = new tcelib.RpcMessageCall();
		m.ifidx = 9;
		m.opidx = 9;
		if( extra!=null){
			m.extra = extra;
		}		
	var d:ByteArray;
	d = new ByteArray();
	var bytes_38:ByteArray = new ByteArray();
	bytes_38.writeUTFBytes(aoid_);
	d.writeInt(bytes_38.length);
	d.writeBytes(bytes_38);
	m.addParam(d);
	d = new ByteArray();
	d.writeFloat(x1_);
	m.addParam(d);
	d = new ByteArray();
	d.writeFloat(y1_);
	m.addParam(d);
	d = new ByteArray();
	d.writeFloat(x2_);
	m.addParam(d);
	d = new ByteArray();
	d.writeFloat(y2_);
	m.addParam(d);
	m.prx = this as Object;
	m.async = async;
	m.asyncparser = this.setBarrierLeave_asyncparser as Function;
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

private  function setBarrierLeave_asyncparser(m:RpcMessage,m2:RpcMessage):void{
	//# function index: 9 , m2 - callreturn msg.
	
}


public function setBarrierEnter(aoid_:String,x1_:Number,y1_:Number,x2_:Number,y2_:Number,async:Function = null,extra:RpcExtraData=null):int{
	//# function index: 10
	
	var r:Boolean = false;
	try{
		var ecode:int = tcelib.RpcConsts.RPCERROR_SUCC;
		ecode = tcelib.RpcConsts.RPCERROR_SUCC;
		var m:tcelib.RpcMessageCall = new tcelib.RpcMessageCall();
		m.ifidx = 9;
		m.opidx = 10;
		if( extra!=null){
			m.extra = extra;
		}		
	var d:ByteArray;
	d = new ByteArray();
	var bytes_39:ByteArray = new ByteArray();
	bytes_39.writeUTFBytes(aoid_);
	d.writeInt(bytes_39.length);
	d.writeBytes(bytes_39);
	m.addParam(d);
	d = new ByteArray();
	d.writeFloat(x1_);
	m.addParam(d);
	d = new ByteArray();
	d.writeFloat(y1_);
	m.addParam(d);
	d = new ByteArray();
	d.writeFloat(x2_);
	m.addParam(d);
	d = new ByteArray();
	d.writeFloat(y2_);
	m.addParam(d);
	m.prx = this as Object;
	m.async = async;
	m.asyncparser = this.setBarrierEnter_asyncparser as Function;
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

private  function setBarrierEnter_asyncparser(m:RpcMessage,m2:RpcMessage):void{
	//# function index: 10 , m2 - callreturn msg.
	
}


public function clearAlarms(aoid_:String,async:Function = null,extra:RpcExtraData=null):int{
	//# function index: 11
	
	var r:Boolean = false;
	try{
		var ecode:int = tcelib.RpcConsts.RPCERROR_SUCC;
		ecode = tcelib.RpcConsts.RPCERROR_SUCC;
		var m:tcelib.RpcMessageCall = new tcelib.RpcMessageCall();
		m.ifidx = 9;
		m.opidx = 11;
		if( extra!=null){
			m.extra = extra;
		}		
	var d:ByteArray;
	d = new ByteArray();
	var bytes_40:ByteArray = new ByteArray();
	bytes_40.writeUTFBytes(aoid_);
	d.writeInt(bytes_40.length);
	d.writeBytes(bytes_40);
	m.addParam(d);
	m.prx = this as Object;
	m.async = async;
	m.asyncparser = this.clearAlarms_asyncparser as Function;
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

private  function clearAlarms_asyncparser(m:RpcMessage,m2:RpcMessage):void{
	//# function index: 11 , m2 - callreturn msg.
	
}


public function clearMiles(aoid_:String,miles_:int,async:Function = null,extra:RpcExtraData=null):int{
	//# function index: 12
	
	var r:Boolean = false;
	try{
		var ecode:int = tcelib.RpcConsts.RPCERROR_SUCC;
		ecode = tcelib.RpcConsts.RPCERROR_SUCC;
		var m:tcelib.RpcMessageCall = new tcelib.RpcMessageCall();
		m.ifidx = 9;
		m.opidx = 12;
		if( extra!=null){
			m.extra = extra;
		}		
	var d:ByteArray;
	d = new ByteArray();
	var bytes_41:ByteArray = new ByteArray();
	bytes_41.writeUTFBytes(aoid_);
	d.writeInt(bytes_41.length);
	d.writeBytes(bytes_41);
	m.addParam(d);
	d = new ByteArray();
	d.writeInt(miles_);
	m.addParam(d);
	m.prx = this as Object;
	m.async = async;
	m.asyncparser = this.clearMiles_asyncparser as Function;
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

private  function clearMiles_asyncparser(m:RpcMessage,m2:RpcMessage):void{
	//# function index: 12 , m2 - callreturn msg.
	
}

}

}