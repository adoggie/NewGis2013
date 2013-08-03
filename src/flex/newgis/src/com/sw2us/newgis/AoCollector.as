package com.sw2us.newgis
{
	/**
	 * DataCollecotr
	 * 数据收集器
	 * ao对象的所有从dgw过来的数据都存储在这里
	 * */
	//import com.adobe.utils.ArrayUtil;
	import com.adobe.utils.DictionaryUtil;
	
	import flash.events.EventDispatcher;
	import flash.utils.Dictionary;
	
	import mx.utils.ArrayUtil;
	
	import newgis.*;
	//import com.adobe.utils.ArrayUtil;
	
	[Event(name="aoData",type="ActiveObjectEvent")]
	
	public class AoCollector extends EventDispatcher
	{
		public static const COLLECTOR_DEFAULT:int =1;
		public static const COLLECTOR_REPLAY:int = 2;
		
//		private var _channel:ActiveObjectChannel ;
		
		public function AoCollector()
		{
//			_channel = new ActiveObjectChannel(this);
		}
		
		private static var _handle:AoCollector = null;
		private var _aodict:Dictionary = new Dictionary();
		
		//每一个ao根据每一个
	
		public static function instance():AoCollector{
			if( _handle == null){
				_handle = new AoCollector();
			}
			return _handle;
		}
		
		public  function pushGpsData(aoid:String,loc:LocationInfo_t):Boolean{
			var evt:ActiveObjectEvent = new ActiveObjectEvent("aoData");
			var d:ActiveObjectData = new ActiveObjectData();
			
			
			//d.data = data;
			
//			if( data.msg =="aom_gpsdata"){
//				d.type =ActiveObjectData.GPS;
//				d.data = data.gps;
//			}else if( data.msg =="aom_alarm"){
//				d.type = ActiveObjectData.ALARM;
//			}else{
//				return false;
//			}
			
			
			var keys:Array = DictionaryUtil.getKeys(_aodict);
			if( ArrayUtil.getItemIndex(parseInt(aoid),keys) ==-1){
				//_aodict[data.aoid]= new ActiveObject(data.aoid);  //new AoDataQueue();
				return false;
			}
			//var aodq:AoDataQueue = _aodict[data.aoid] as AoDataQueue;
			//aodq.pushData(data.type,data);
			var ao:ActiveObject = _aodict[parseInt(aoid)];			
			ao.pushGpsData(loc);
			d.ao = ao;
			//触发给接收者
			evt.data = d;
			dispatchEvent(evt);
			return true;
		}
		
		public function getData(aoid:int,module:int):Object{
			var keys:Array  = DictionaryUtil.getKeys(_aodict);
			if( ArrayUtil.getItemIndex(aoid,keys) ==-1){
				return null;		
			}
			//var q:AoDataQueue = _aodict[aoid] as AoDataQueue;
			var ao:ActiveObject = _aodict[aoid];			
			return ao.getModuleData(module);
		}
		
		public function getActiveObject(aoid:int):ActiveObject{
			var keys:Array  = DictionaryUtil.getKeys(_aodict);
			if( ArrayUtil.getItemIndex(aoid,keys) ==-1){
				return null;		
			}
			//var q:AoDataQueue = _aodict[aoid] as AoDataQueue;
			var ao:ActiveObject = _aodict[aoid];			
			return ao;
		}
		
		public function getAcitveObjectList():Array{
			//return new Array();
			return DictionaryUtil.getValues( _aodict);
		}
		
		public function addActiveObject(ao:ActiveObject):void{
			_aodict[ao.getId()] = ao;
		}
		
		
		public function removeActiveObject(aoid:int):void{
			var keys:Array = DictionaryUtil.getKeys(_aodict);
			if( ArrayUtil.getItemIndex(aoid,keys) !=-1){
				var ao:ActiveObject = _aodict[aoid] as ActiveObject;
				ao.deleteThis();  //删除所有地图上关联的path，marker等对象
				delete _aodict[aoid];
			}
		}
		
		public function clear():void{
			var aos:Array;
			aos = DictionaryUtil.getValues( _aodict);
			var n:int;
			var ao:ActiveObject;
			for(n=0;n<aos.length;n++){
				ao = aos[n] as  ActiveObject;
				ao.getDataQueue().clearAll();
				ao.deleteThis();
			}
			_aodict = new Dictionary();
		}
		
//		public function getAoChannel():ActiveObjectChannel{
//			return _channel;	
//		}
//		
		
		
		
	}
}