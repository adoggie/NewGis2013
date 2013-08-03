package com.sw2us.newgis
{
	import com.adobe.utils.*;
	import com.sw2us.newgis.map.MapAo;
	import com.sw2us.newgis.util.HashMap;
	
	import newgis.*;
	
	import org.openscales.geometry.basetypes.Location;
	
	public class ActiveObject
	{
		/*
		public function ActiveObject(id:int)
		{
			_id = id;
			_dq = new AoDataQueue();
		}*/
		
		//车辆定义
		public static const VEHICLE:int = 0;		
		public static const VEHICLE_CAR:int = 		VEHICLE + 0x01; 		//#小车
		public static const VEHICLE_GOODS:int = 	VEHICLE+ 0x02; //#货车
		public static const VEHICLE_BUS:int = 		VEHICLE + 0x03; 		// #公交
		public static const VEHICLE_ENGINE:int= 	VEHICLE+0x04;  //工程车
		public static const VEHICLE_MOTO:int =		VEHICLE+0x05; //助动车
		public static const VEHICLE_BIKE:int = VEHICLE+0x06; //助动车或自行车
		
		public static const PEOPLE:int = 1<<4 ;	//#人物或者动物
		public static const PEOPLE_PERSON:int = PEOPLE+0x01; // 人物
		public static const PEOPLE_DOG:int =  PEOPLE+0x02; // #宠物
		
		
		public function ActiveObject(ao:Object){
			_ao = ao;
			_dq = new AoDataQueue();
			_mapaos = new Array();
			//解析 ao.gps 为 GpsData_t 
			if( ao.gps != null){
				var gps:newgis.GpsData_t = new GpsData_t();
				gps.lon = ao.gps.lon;
				gps.lat = ao.gps.lat;
				gps.direction = ao.gps.angle;
				gps.speed = ao.gps.speed;
				gps.time = ao.gps.gpstime;
				gps.extra.power = ao.gps.power;
				gps.extra.acc = ao.gps.acc;
				gps.extra.miles = ao.gps.miles;
				gps.extra.av = ao.gps.av;
				_ao.gps = gps;
			}
		}
			
		//private var _id:int;
		private var _dq:AoDataQueue=null;
		private var _mapaos:Array;	//图上地图对象列表 
		private var _ao:Object;
		
		private var _options:HashMap = new HashMap();
		
		public function setOption(key:String,val:Object):void{
			_options.put(key,val);
			
		}
		
		public function getOption(key:String,dft:Object = null):Object{
			if(_options.containsKey(key)){
				return _options[key];
			}
			return dft;
		}
		
		
		public function getInfo():Object{
			return _ao;	
		}
		
		public function getId():int{
			return _ao.id;
		}
		
		//获取图上ao对象
		public function getMapObjects():Array{
			return _mapaos;
		}
		
		public function addMapObject(mao:MapAo):void{
			_mapaos.push(mao);
		}
		
		public function deleteThis():void{
			var n:int;
			for(n=0;n<_mapaos.length;n++){
				var mao:MapAo = _mapaos[n];
				mao.deleteThis();
			}
			_mapaos = null;
		}
		
		public function removeMapObject(mao:MapAo):void{
			ArrayUtil.removeValueFromArray(_mapaos,mao);
		}
		
		public function getDataQueue():AoDataQueue{
			return _dq;
		}
		
//		public function pushModuleData(module:int,data:Object):void{
//			_dq.pushData(module,data);
//			//hook is here，这里要做数据分类处理
//			//gps数据需要分派到 MapAo去
//			if( module & ActiveObjectData.GPS){ //位置移动信息
//				trace("mao num:",_mapaos.length);
//				for(var n:int=0;n<_mapaos.length;n++){
//					var mao:MapAo = _mapaos[n] as MapAo;
//					if( data.lon!=0 && data.lat != 0){ //有效的gps信息放入数据队列
//						_ao.gps = data;		
//						mao.setGpsData(data);						
//					} 
//				}
//			}
//		}
		
		public function pushGpsData(loc:LocationInfo_t):void{
			_dq.pushData(ActiveObjectData.GPS,loc.gps);
			for(var n:int=0;n<_mapaos.length;n++){
				var mao:MapAo = _mapaos[n] as MapAo;
				if( loc.gps.lon!=0 && loc.gps.lat != 0){ //有效的gps信息放入数据队列
					_ao.gps = loc.gps;
					mao.setGpsData(loc.gps);						
				} 
			}
			
		}
		
		//设置ao对象经纬度坐标
		public function setLocation(x:Number,y:Number):void{
			for(var n:int=0;n<_mapaos.length;n++){
				var mao:MapAo = _mapaos[n] as MapAo;
				mao.setLocation(x,y);
			}
		}
		
		public function getLocation():Location{
			var loc:Location = new Location(0,0);
			if( _ao.gps!=null){
				loc = new Location(_ao.gps.lon,_ao.gps.lat);
			}
			return loc;
		}
		
		//最新的模块数据
		public function getModuleData(module:int):Object{
			return _dq.getData(module);			
		}
		
		//获取指定时间模块数据 tick -  timestamp
		public function getModuleDataByTime(module:int,tick:int):Object{
			return _dq.getModuleDataByTime(module,tick);
		}
		
		//获取最近的ao有效的定位信息
		public function getGpsData():GpsData_t{			 
			return _ao.gps as GpsData_t;			
		}
		
		
	}
}