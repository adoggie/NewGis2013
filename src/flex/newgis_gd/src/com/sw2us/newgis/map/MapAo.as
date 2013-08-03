/**
 * Mapao - Map ActiveObject
 * 
 * 2011.6.13 睡不着，现在0:12
 *     1. 添加mao对象居中，图随ao而动
 */ 
package com.sw2us.newgis.map
{
	import com.mapabc.maps.api.MFlexMap;
	import com.mapabc.maps.api.basetypes.MLngLat;
	import com.sw2us.newgis.ActiveObject;
	import com.sw2us.newgis.AppResource;
	import com.sw2us.newgis.assets.comps.start;
	
	import flash.display.Bitmap;
	import flash.display.BitmapData;
	import flash.display.DisplayObject;
	import flash.events.Event;
	
	import newgis.GpsData_t;
	
	import org.openscales.core.Map;
	import org.openscales.core.feature.*;
	import org.openscales.core.layer.FeatureLayer;
	import org.openscales.core.layer.Layer;
	import org.openscales.core.request.DataRequest;
	import org.openscales.core.style.Style;
	import org.openscales.geometry.Point;
	import org.openscales.geometry.basetypes.Location;
	
	
	public class MapAo 
	{
		private var _layer:MapAoLayer= null;
		private var _ao:ActiveObject = null;
		private var _ispathshow:Boolean = false;
		private var _marker:MapAoMarker = null; //图上运动对象图标
		private var _text:String;
		private var _path:MapAoPath = null;	//路径
		private var _modeCenter:Boolean = false;
		
		[Embed(source="../assets/images/ao_car_green_48x48_180.png")]
		private var _defaultImage:Class;
		
		public static const STYLE_DEFAULT:String ="default"; //gps，gprs正常
		public static const STYLE_ALARM:String = "alarm";	//
		public static const STYLE_OFFLINE:String ="offline";	//无法联机状态，默认显示为灰色
		
		private var _gpsdata:GpsData_t = null;
		private var _status:String = STYLE_DEFAULT;
		private var _name:String = "map active object";
		
		public function MapAo(ao:ActiveObject,layer:MapAoLayer)
		{			
			_ao = ao;						
			_layer = layer;
			ao.addMapObject(this);
			
			layer.addMapAo(this);
			var loc:Location = new Location(0,0);
			//第一次创建，ao如果携带的gps数据有效则直接设置其位置信息
			var info:Object;
			info = _ao.getInfo();
			if( info.gps !=null && info.gps.lon!=0 && info.gps.lat!=0){
				loc = new Location(info.gps.lon,info.gps.lat);				
			}
			
			_marker = MapAoMarker.create(this,AppResource.instance().getAoBitmapUrlByAngle(180),loc );
			_path = new MapAoPath(this,layer);					
		}
		
		public function get marker():MapAoMarker{
			return _marker;
		}
		
		public function destroyThis():void{
			deleteThis();
		}
		
		public function deleteThis():void{
			_marker.deleteThis();
			_path.deleteThis();
		}
		
		public function  get layer():MapAoLayer{
			return _layer;
		}
		
		public function get name():String{
			return _name;
		}
		public  function set visible(v:Boolean):void{
			//this._marker.visible = v;
		}
		
		public function get visible():Boolean{
			return true;
			//return _marker.visible;
		}
		
		//显示ao对象名称
		public function set textVisible(v:Boolean):void{
			
		}
		
		public function get textVisible():Boolean{
			return true;
		}
		
		//
		public function setFocus(b:Boolean):void{
			/*
			var layer:MapAoLayer = _marker.layer as MapAoLayer;
			var features:Vector.<Feature> = layer.features;
			var n:int;
			if( b == false){
				if( layer.getFocusAo() == this){
					layer.setFocusAo(null);
				}
				_marker.drawFocused = false;
				return;
			}
			// b = true
			for(n=0;n<features.length;n++){
				var m:MapAoMarker = features[n] as MapAoMarker;
				if( m && m.getMapAo() != this){
					m.drawFocused = false;
				}
			}
			_marker.drawFocused = true;
			layer.setFocusAo(this);
			*/
		}
		
		
		
		public function getMarker():MapAoMarker{
			return _marker;
		}

		public function getPath():MapAoPath{
			return _path;
		}
		
		public function getMap():MapControl{
			//return this._marker.layer.map;
			return _layer.map;
		}
		
		//是否显示轨迹
		public function showPath(v:Boolean = true):void{
			getPath().setVisible(v);
		}
		
		//gps位置改变传送到此，改变在地图上的位置 
		public function setGpsData(d:GpsData_t):void{
			if(d== null){
				return;
			}
			this._ao.getInfo().gps = d;
			
			if( d.lon > 0 && d.lat >0){
				_marker.visible = true;
			}else{
				_marker.visible = false; //非法经纬度信息，隐藏ao对象显示
				return;
			}
			//setLonLat(new Location(d.lon,d.lat) ); //设置经纬度坐标
			setLocation(d.lon,d.lat);			
			//切换 角度
			setAngle(d.direction);
						
			//更改路径数据
			//_path.reload();	
			_gpsdata = d;
		}
		// d - 报警信息内容, 5分钟内没有连续报警则清除报警状态
		/*public function setAlarm(alarm:Object):void{
			
		}*/
		
		//设置ao运动方向
		public function setAngle(a:Number):void{
			//_marker.loadDisplayObject(AppResource.instance().getAoBitmapByAngle(a));
			_marker.setAngle(a);
		}
		
		//设置ao当前状态， 正常还是报警
		public function setStatus(s:String=STYLE_DEFAULT):void{
			setGpsData(_gpsdata);
		}
		public function getStatus():String{
			return _status;	
		}
		
		public function getActiveObject():ActiveObject{
			return _ao;
		}
		
		public function getText():String{
			return _text;
		}
		
		public function setText(text:String):void{
			_text = text;
		}
		
		private function _setLonLat(ll:Location):void{
			if( ll.lat ==0 || ll.lon == 0){
				return;
			}
			//_marker.geometry = new Point(ll.lon,ll.lat);
			//_marker.draw();
			//_marker.marker.lnglat = new MLngLat(ll.lon,ll.lat);
			_marker.marker.moveTo(new MLngLat(ll.lon,ll.lat));
		}
		
		public function setLocation(x:Number,y:Number):void{
			_setLonLat(new Location(x,y));
			if(_modeCenter){
				moveCenter();
			}
		}
		
		/*
		//将地图移动到此ao对象为中心点
		public function moveTo():void{
			_layer.map.moveTo( _marker.lonlat );
		}*/
	
		//设置ao在地图中心点
		public function moveCenter():void{
			var loc:Location;
			loc = _ao.getLocation();
			if(loc.lat==0 || loc.lon == 0){
				return;
			}
			_layer.map.moveTo(loc.lon,loc.lat);
		}
		
		//设置地图居中模式
		public function setCenterMode(b:Boolean):void{
			if( b == false){
				if(_layer.getCurrentCenterAo() == this){
					_layer.setCurrentCenterAo(null);
				}
			}else{
				if( _layer.getCurrentCenterAo()!=this && _layer.getCurrentCenterAo() !=null){
					_layer.getCurrentCenterAo().setCenterMode(false);
					_layer.setCurrentCenterAo(this);
				}
			}			
			_modeCenter = b;
			if(_modeCenter){
				moveCenter();
			}
		}
		
		//地图是否图随车动 
		public function getCenterMode():Boolean{
			return _modeCenter;
		}
		
		
	}
}