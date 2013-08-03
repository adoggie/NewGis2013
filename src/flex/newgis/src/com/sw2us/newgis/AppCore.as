package com.sw2us.newgis
{
	import com.sw2us.newgis.util.HashMap;
	
	import flash.events.*;
	import flash.system.Security;
	import flash.system.SecurityDomain;
	import flash.system.System;
	import flash.utils.Timer;
	
	import mx.core.Application;
	import mx.core.FlexGlobals;
	import mx.managers.BrowserManager;
	import mx.managers.IBrowserManager;
	import mx.utils.URLUtil;
	
	import newgis.*;
	
	import org.openscales.core.Util;
	import org.openscales.geometry.basetypes.Unit;
	
	import tcelib.*;
	
	public class AppCore
	{
		private var default_hostbase:String = "http://localhost:8521";				//这两个东东根据部署情况改一下
		private var default_wms_url:String = "http://localhost8001/wms";
		private var default_dgw_host:String= "localhost";
		private var default_dgw_port:int = 6655;
		private var _hostbase:String ="" ; // "http://192.168.14.3:9099";
		private var _amfserver:String ="";
		private var _datacolletors:HashMap= new HashMap();
		private var _sysprops:Object  = null;	//系统属性
		private var _appuser:AppUser = null;
		public var _delta:Object = new Object();
		
		private var _prxgwa:IGatewayAdapterPrx = null;
		private var _params:Object = null;
		
		private var _timer:Timer;
		private var _gwalogin:Boolean = false;
		private var _nearheart_time:Number =  new Date().time/1000;
		
		private var _userclientimpl:UserClientImpl = new UserClientImpl();
		private var _adapter:RpcCommAdapter = new RpcCommAdapter();
		
		public function AppCore(){
//			Security.allowDomain("sw2us.com");
			if(1){
				default_hostbase= "http://localhost:9090";				//这两个东东根据部署情况改一下
//				default_wms_url= "http://localhost:8001/wms";
//				default_dgw_host = "sw2us.com";
			}
			_hostbase = default_hostbase;
			_appuser = new AppUser();
			_appuser.id = 1;
			_appuser.user ="user_001";
			_appuser.passwd="123";
			
			
			_timer = new Timer(1000*5);
			_timer.addEventListener(TimerEvent.TIMER,onTimer);
			_timer.start();
//			web_server
			_adapter.addServant( this._userclientimpl);
			
		}
		
		
		
		private function onTimer(e:TimerEvent):void{
			var prxgwa:IGatewayAdapterPrx = getGwaPrx();
			if(prxgwa == null){
				return ;
			}
			
			if(!_gwalogin){
				prxgwa.login(_appuser.token,gwalogin_result);
				return;
			}
			
			var curtime:Number = new Date().time/1000;
			if( curtime - _nearheart_time >=15){
				_gwalogin = false;
				return ;
			}
			// heartbeat
			prxgwa.heartbeat(heartbeat_result);
		}
		
		private function heartbeat_result(cr:int,prx:RpcProxyBase):void{
			if( cr == -1){
				_gwalogin = false;
				return;
			}
			_nearheart_time=  new Date().time/1000;
		}
		
		private function gwalogin_result(cr:CallReturn_t,prx:RpcProxyBase):void{
			_gwalogin = cr.error.succ;
			_nearheart_time=  new Date().time/1000;
		}
		
//		private function getWmsAddress
		public function getGwaPrx():IGatewayAdapterPrx{
			if( _params == null){
				return null;
			}
			if(_prxgwa == null){
				var gwa:String = _params.gwa as String ;
				var addr:Array = gwa.split(":");				
				_prxgwa = IGatewayAdapterPrx.create(addr[0],parseInt(addr[1]));
				_prxgwa.conn.attachAdapter(this._adapter); // important!!
			}
			return _prxgwa;
		}
		
		public function getAppUser():AppUser{
			return _appuser;	
		}
		
		public function setAppUser(au:AppUser):void{
			_appuser = au;
		}
		
		public function setAppParams(params:Object):void{
			_params = params;
			default_wms_url = _params.wms;
		}
		
		public function getDgwServer():Object{
			var server:Object = new Object();
			server.host=default_dgw_host;
			server.port=default_dgw_port;
			return server;
		}
		
		public  function getHostBaseUrl():String{
			if( _hostbase != ""){
				return _hostbase;
			}
			
			var bm:IBrowserManager = BrowserManager.getInstance();
			bm.init();
			var url:String = bm.url;				
			var port:String = String(URLUtil.getPort(url));
			var protocol:String = URLUtil.getProtocol(url);
			var serverName:String  = URLUtil.getServerName(url);			
			if (protocol.toLowerCase() =="http"){
				_hostbase = protocol+"://"+serverName+":"+port;
			}else{
				_hostbase=default_hostbase;
			}
			return _hostbase;
		}	
		
		public function setAmfServerUrl(url:String):void{
			_amfserver = url;
		}
		
		public function getAmfServerUrl():String{
			if(_amfserver==""){
				_amfserver = getHostBaseUrl()+"/gateway/";
			}
			return _amfserver;
		}
		
		
		public function init():Boolean{
			org.openscales.geometry.basetypes.Unit.DOTS_PER_INCH = 92;
			//AoCollector.instance();
			_datacolletors.put(AoCollector.COLLECTOR_DEFAULT ,new AoCollector() );
			_datacolletors.put(AoCollector.COLLECTOR_REPLAY,new AoCollector())
			AppResource.instance();
			return true;
		}
		
		public function getAoCollector(type:int = 1):AoCollector{
			var o:AoCollector = _datacolletors.getValue(type) as AoCollector; 
			return o;
		}
		
		public function getMapServerUrl():String{
			return default_wms_url;
		}
		
		public function set sysProps(props:Object):void{
			_sysprops = props;
		}
		
		public function get sysProps():Object{
			return _sysprops;
		}
		
		public function getSysParamValue(name:String,dft:Object=null):Object{
			var o:Object = null;
			try{
				o = _sysprops[name];
			}catch(e:Error){
				;
			}
			if(o==null){
				o = dft;
			}
			return o;
		}
		
		//private var _aochannel:ActiveObjectChannel = new ActiveObjectChannel();
		
		//public function getAoChannel():ActiveObjectChannel{
		//	return _aochannel;
		//}
		
		private static var _handle:AppCore = null;
		public static function instance():AppCore{
			if( _handle == null){
				_handle = new AppCore();
				_handle.init();
			}
			return _handle;
		}
		
		
	}
}