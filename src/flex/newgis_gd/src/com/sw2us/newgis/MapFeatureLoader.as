package com.sw2us.newgis
{
	/**
	 * MapPointLoader - 地图上用户点和地理点对象加载器
	 * 封装的地图对象都存在一个MapPointLoader对象
	 */
	import com.sw2us.newgis.util.HashMap;
	
	import mx.rpc.AbstractOperation;
	import mx.rpc.events.FaultEvent;
	import mx.rpc.events.ResultEvent;
	import mx.rpc.remoting.Operation;
	import mx.rpc.remoting.RemoteObject;
	
	import org.openscales.core.Map;
	import org.openscales.core.events.TileEvent;
	
	public class MapFeatureLoader
	{
		private var _name:String;
		private var _box:MapBox = null;
		private var _loadfunc:Function = null;		//架子啊
		
		private var _remote:RemoteObject = new RemoteObject("gis");
		private var _getUserPoints:AbstractOperation;;
		private var _getUserPolygons:AbstractOperation;;
		private var _getUserLines:AbstractOperation;;
		private var _getGeoPoints:AbstractOperation;; //获取地图层点
		private var _enablefeatures:uint;
		
		public static var FEATURE_LOAD_USERPOINT:uint = 0x01;
		public static var FEATURE_LOAD_USERPOLYGON:uint = 0x02;
		public static var FEATURE_LOAD_USERLINE:uint = 0x04;
		public static var FEATURE_LOAD_ALL:uint = 0xff;
		public static var FEATURE_LOAD_GEOPOINT:uint = 0x 08 ; //地图地理点信息
		
		public function MapFeatureLoader(box:MapBox,enablefeatures:uint =FEATURE_LOAD_ALL, name:String="pointloader",loadfunc:Function=null)
		{
			_name = name;
			_box = box;
			_loadfunc = loadfunc;  
			_enablefeatures = enablefeatures;
			
			var wmclayer:WMSC =box.bglayer.layer as WMSC;
			wmclayer.addEventListener(TileEvent.TILE_LOAD_START,onMapTileLoad);
			wmclayer.addEventListener(TileEvent.TILE_DESTROY,onMapTileDestroy);
			_remote.endpoint = AppCore.instance().getAmfServerUrl();
			_remote.showBusyCursor = true;
			_getUserPoints = _remote.getOperation("getUserPointList");
			_getUserPoints.addEventListener(FaultEvent.FAULT,onLoadFault);
			_getUserPoints.addEventListener(ResultEvent.RESULT,onUserPointsSucc);
			
			_getGeoPoints = _remote.getOperation("getGeoPointList");
			_getGeoPoints.addEventListener(FaultEvent.FAULT,onLoadFault);
			_getGeoPoints.addEventListener(ResultEvent.RESULT,onGeoPointsSucc);
			
			
			
			
		}
		
		private function onLoadFault(evt:FaultEvent):void{
			//var result:Array = 
		}
		
		private function onUserPointsSucc(evt:ResultEvent):void{
			var features:Array = evt.result as Array;
			_box.onFeaturesLoad(MapFeatureLoader.FEATURE_LOAD_USERPOINT,features);
		}
		
		/**
		 * onMapTileLoad
		 * 地图网格被创建，意味着新的地理区域的对象要被请求
		 */ 
		private function onMapTileLoad(e:TileEvent):void{
			var rect:Array = new Array();
			rect.push(e.tile.bounds.left); rect.push(e.tile.bounds.bottom);
			rect.push(e.tile.bounds.width); rect.push(e.tile.bounds.height);
			if( _enablefeatures& MapFeatureLoader.FEATURE_LOAD_USERPOINT){
				_getUserPoints.send(_box.fxmap.map.resolution,rect); //发送请求
			}
			
		}
		
		/**
		 * onMapTileDestroy
		 * 地图网格删除，此区域内的用户点对象应该被删除
		 */ 
		private function onMapTileDestroy(e:TileEvent):void{
			_box.onFeaturesDestroy(e.tile.bounds);
		}
	}
}