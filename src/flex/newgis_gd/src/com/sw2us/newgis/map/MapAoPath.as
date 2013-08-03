/**
 * 
 *  MapAoPath - ao对象运动轨迹
 *   单线 , 考虑应用的负责可以修改为MultiLineStringFeature
 * 
 * 
 * */
package com.sw2us.newgis.map
{	
	import com.mapabc.maps.api.MFlexMap;
	import com.mapabc.maps.api.basetypes.MLngLat;
	import com.mapabc.maps.api.events.MMapEvent;
	import com.mapabc.maps.api.events.MMapMoveEvent;
	import com.mapabc.maps.api.events.MMapZoomEvent;
	import com.mapabc.maps.api.overlays.MLabel;
	import com.mapabc.maps.api.overlays.MMarker;
	import com.mapabc.maps.api.overlays.MPolyline;
	import com.mapabc.maps.api.overlays.options.MLineOptions;
	import com.mapabc.maps.api.overlays.options.MTipOptions;
	import com.mapabc.maps.api.styles.MFontStyle;
	import com.mapabc.maps.api.styles.MLineStyle;
	import com.sw2us.newgis.ActiveObjectData;
	
	import flash.display.Sprite;
	import flash.events.EventDispatcher;
	import flash.geom.Point;
	import flash.geom.Rectangle;
	import flash.text.TextField;
	import flash.text.TextFormat;
	import flash.text.TextFormatAlign;
	
	import org.openscales.core.StringUtils;
	import org.openscales.core.basetypes.maps.HashMap;
	import org.openscales.core.events.MapEvent;
	import org.openscales.core.feature.*;
	import org.openscales.core.layer.FeatureLayer;
	import org.openscales.core.layer.Layer;
	import org.openscales.core.style.*;
	import org.openscales.core.style.stroke.*;
	import org.openscales.core.style.symbolizer.*;
	import org.openscales.geometry.*;
	import org.openscales.geometry.basetypes.Location;
	import org.openscales.geometry.basetypes.Pixel;
	
	//public class MapAoPath extends LineStringFeature
	public class MapAoPath extends EventDispatcher
	{
		private var _mao:MapAo;
		//private var _ticks:Array; //时间标签
		private var _tickgap:int=0;	//时间间隔 
		//private var _visible:Boolean = false;
		private var _tickvisible:Boolean = false;
		private var _markers:Array= new Array(); //路径时间标记
		private var _arrows:Array = new Array();
		private var _tickshowmode:int = MapAoPathMarker.SHOWMODE_DEFAULT;
		private var _pathlinevisible:Boolean = true;	//是否显示行驶轨迹线
		
		private static const LOSTPATH_DISTANCE:Number = 1/50;	// degree 
		
		private var _path:MPolyline = null;
		
		public function MapAoPath(mao:MapAo,layer:MapAoLayer)
		{
			//super(new LineString(new Vector.<Number>() ),null,this.getDefaultStyle());
			_mao = mao;
			
			//layer.addFeature(this);			
			_tickgap = 60;	//默认间隔5分钟			
			setVisible(false);
			//_tickvisible = true;
		}
		
		public function get mao():MapAo{
			return _mao;
		}
		//设置时钟标签时间间隔
		public function setTickTimeGap(gap:int):void{
			_tickgap = gap;
			setTicksVisible(_tickgap > 0);
		
		}
		
		public function getTickTimeGap():int{
			return _tickgap;
		}
		
		public function setPathLineVisible(v:Boolean):void{
			_pathlinevisible = v;
			setTicksVisible(v);	
			//reload();
		}
		
		public function pathLineVisible():Boolean{
			return _pathlinevisible;
		}
		
		public  function setVisible(v:Boolean):void{
			//var t:Boolean = super.visible;			
			//super.visible = v;
			//if( v == false){
			this.setPathLineVisible(v);
			
			//}
			var map:MFlexMap;
			map =this.mao.layer.map.getMap() as MFlexMap; 
			if(v){
				//绑定地图缩放事件
				 
				map.removeEventListener(MMapMoveEvent.MOVE_END,onMapMoveEnd);
				map.removeEventListener(MMapZoomEvent.ZOOM_END,onMapZoomEnd);
				map.removeEventListener(MMapZoomEvent.ZOOM_START,onMapZoomStart);
				map.removeEventListener(MMapMoveEvent.MOVE_START,onMapMoveStart);
				
				map.addEventListener(MMapMoveEvent.MOVE_END,onMapMoveEnd);
				map.addEventListener(MMapZoomEvent.ZOOM_END,onMapZoomEnd);
				map.addEventListener(MMapZoomEvent.ZOOM_START,onMapZoomStart);
				map.addEventListener(MMapMoveEvent.MOVE_START,onMapMoveStart);
				 
				trace(">>++++ bind event to ao",_mao.getActiveObject().getId());
			}else{
				//this.layer.map.removeEventListener(MapEvent.MOVE_END,onMapMoveEnd);
				 
				map.removeEventListener(MMapMoveEvent.MOVE_END,onMapMoveEnd);
				map.removeEventListener(MMapZoomEvent.ZOOM_END,onMapZoomEnd);
				map.removeEventListener(MMapZoomEvent.ZOOM_START,onMapZoomStart);
				map.removeEventListener(MMapMoveEvent.MOVE_START,onMapMoveStart);
				 
				trace(">>----detach event to ao",_mao.getActiveObject().getId());
			}			
		}
	
		//private function onMapMoveEnd(event:MapEvent):void{
		private function onMapMoveEnd(event:MMapMoveEvent):void{
			trace("map move end..",_markers.length);
		//	var path:MapAoPath = event.currentTarget as MapAoPath;
				
			reload();			
		}
		
		private function onMapZoomEnd(event:MMapZoomEvent):void{
			
			reload();			
		}
		
		private function onMapMoveStart(event:MMapMoveEvent):void{
			return ;
			trace("map movestart..");
			var map:MFlexMap;
			map = _mao.layer.map.getMap() as MFlexMap;
			if( _path!=null){
				map.removeOverlay(_path);
			}
			
			clearArrows();
			clearTickMarkers();		
		}
		
		private function onMapZoomStart(event:MMapZoomEvent):void{			
			var map:MFlexMap;
			map = _mao.layer.map.getMap() as MFlexMap;
			if( _path!=null){
				map.removeOverlay(_path);
			}
			clearArrows();
			clearTickMarkers();	
		}
		
		public function getVisible():Boolean{
			//return this.visible;
			return true;
		}
		
		
		//设置时间标签可见
		public function setTicksVisible(b:Boolean):void{
			/*
			var f:Feature;
			var layer:FeatureLayer = this.layer as FeatureLayer;			
			if( _tickvisible == false){
				for(var n:int=0;n<this._markers.length;n++){
					f = _markers[n] as Feature;
					layer.removeFeature(f);				
				}
				_markers.splice(0);				
				if(b == true){
					_tickvisible = b;								
					reload();
				}
			}	*/
			_tickvisible = b;	
			
			/*
			var map:MFlexMap;
			map =this.mao.layer.map.getMap() as MFlexMap; 
			if(b){
				//绑定地图缩放事件
				//this.layer.map.addEventListener(MapEvent.MOVE_END,onMapMoveEnd);
				map.addEventListener(MMapMoveEvent.MOVE_END,onMapMoveEnd);
				map.addEventListener(MMapZoomEvent.ZOOM_END,onMapZoomEnd);
				map.addEventListener(MMapZoomEvent.ZOOM_START,onMapZoomStart);
				map.addEventListener(MMapMoveEvent.MOVE_START,onMapMoveStart);
			}else{
				//this.layer.map.removeEventListener(MapEvent.MOVE_END,onMapMoveEnd);
				map.removeEventListener(MMapMoveEvent.MOVE_END,onMapMoveEnd);
				map.removeEventListener(MMapZoomEvent.ZOOM_END,onMapZoomEnd);
				map.removeEventListener(MMapZoomEvent.ZOOM_START,onMapZoomStart);
				map.removeEventListener(MMapMoveEvent.MOVE_START,onMapMoveStart);
				
			}	*/	
			
			reload();
		}
		//
		public function ticksVisible():Boolean{
			/*
			if(this.visible == false){
				return false;
			}
			*/
			return _tickvisible ;
		}
		
		//显示方向标记还是时间
		public function setTickShowMode(mode:int):void{
			var n:int;
			for(n=0;n<_markers.length;n++){
				var m:MapAoPathMarker =_markers[n]  as MapAoPathMarker;
				m.setShowMode(mode);
			}
			_tickshowmode = mode;
		}
		
		public function tickShowMode():int{
			return _tickshowmode;
		}
		
		
		//public function load
		//读取ao路径
		/*
			1. 要检测中间无效gps定位信息并过滤
			2. 对于两点之间大区域的跳跃，只选择跳跃之后的连续gps信息
		
		2012.5.4 增加线段的方向箭头
		*/
		public function reload():void{
			
			
			//this.visible = true;
			trace("path reload()",_mao.getActiveObject().getId());
			//var ptset:Vector.<Number> = new Vector.<Number>();
			var ptset:Array = new Array();
			
			var gpsdata:Array = _mao.getActiveObject().getDataQueue().getDataList(ActiveObjectData.GPS);
			var lastloc:Location = null;
			
			//var lstr:LineString = this.geometry as LineString;			
			
		//	lstr.components = null;
			var tick:int = 0;
			
			
			var map:MFlexMap;
			map = _mao.layer.map.getMap() as MFlexMap;
			if( _path!=null){
				map.removeOverlay(_path);
			}
			
			clearArrows();
			clearTickMarkers();
			if(pathLineVisible()==false || gpsdata.length==0){
			//	this.draw();
				return ;
			}
			//tick = gpsdata[0].gpstime; //开始时间
				
			var ticks:Array = new Array(); //路径标签  time tags
			var segs:Array = new Array();
			
			/*
			2012.5.27  考虑 当速度连续为0，但经纬度有效的情况下，第一条速度为0的记录有效
			*/
			var speedzero:Boolean = false;
			var d:newgis.GpsData_t;
			var lastd:Object = null;
			for(var n:int=0; n< gpsdata.length;n++){
				d = gpsdata[n] as newgis.GpsData_t;				
				//trace(d.lon,d.lat,d.speed);
				//trace("::",d.gpstime,d.lon,d.lat,d.speed);
				if( d.lon * d.lat == 0 ){ // || d.speed==0){
					continue; //无效gps信息过滤
				}
				if( d.speed == 0){ //
					if(speedzero){
						//continue; //连续速度为0则忽略本条记录
					}else{
						speedzero = true; //置标识0速度开始
					}					
				}else{
					speedzero = false;
				}
				
				
				if( lastloc != null){
					var thisloc:Location = new Location(d.lon,d.lat);
					var o:Object = new Object();
					o.first = lastloc;
					o.second = thisloc;
					segs.push(o);
				}				
				//trace(">>",d.gpstime,d.lon,d.lat,d.speed);
				lastloc = new Location( d.lon,d.lat );	
				
				ptset.push(new MLngLat(d.lon,d.lat));
				//ptset.push(d.lon);
				//ptset.push(d.lat);
								
				lastd =d ;
				//创建时间标签轨迹, 这个遍历是倒序的所以要将gps数据插入队列头部
				if( _tickvisible && _tickgap>0){					
					if( d.time - tick > this._tickgap){
						tick = d.time;
						ticks.push(d);
					}
				}				
			}
			
			
			//if( this._tickvisible  && ticks.length ){
			createArrows(segs);
			createTickMarkers(ticks);
			
			
			//}
			
			
			
			
			var lineOptions:MLineOptions=new MLineOptions();  //新建线参数选项对象 			
			lineOptions.lineStyle.alpha=0.6;   //设置线的透明度 			
			lineOptions.lineStyle.color=0xff0000;   //设置线的颜色 			
			lineOptions.lineStyle.thickness=3;    //设置线的粗细
			
			
			lineOptions.lineStyle.lineType= MLineStyle.LINE_SOLID; //LINE_DASHED ; //MLineStyle.LINE_SOLID;  //设置线的样式：实线、虚线 
			
			
			
			if(ptset.length<4){								
				//this.draw();
				return;
			}
			
			_path =new MPolyline(ptset,lineOptions);  //新建线对象，线的参数选项为系统默认方式 
			map.addOverlay(_path,false);   //在地图上添加线 
			
			trace("ptset size:",ptset.length);
			
		//	lstr.components = ptset;
			
		//	this.draw();
			try{
		//		this.layer.setChildIndex(this,0); // 道路必须设置在mao下面
			}catch(e:Error){
				
			}
			
			//_mao.getMarker().marker.setToTop();
		}	
	
		public function deleteThis():void{
			/*
			layer.map.removeEventListener(MapEvent.MOVE_END,onMapMoveEnd);
			
			var flayer:FeatureLayer = this.layer as FeatureLayer;
			clearTickMarkers();
			clearArrows();
		
			flayer.removeFeature(this);
			*/
		}
		
		private function createArrows(segs:Array):void{
			
			var ar:MapAoPathArrow;
			var n:int;
			//trace("create arrows...");
			var rclast:Rectangle = null;
			//var layer:FeatureLayer = null;
			for(n=0;n<segs.length;n++){	
				ar = new MapAoPathArrow(this,segs[n].first,segs[n].second);
				var rc:Rectangle = ar.getBounds_();
				var rc3:Rectangle = this._mao.getMarker().getBounds();
				if( rc.intersects(rc3)){ //防止与aomarker 车辆图标碰撞
					//layer = this.layer as FeatureLayer;
					//layer.removeFeature(ar);
					ar.clear();
					continue;	
				}
				if(rclast!=null){//判别与上一个arrow是否碰撞
					if(rc.intersects(rclast)){
						//layer= this.layer as FeatureLayer;
						//layer.removeFeature(ar);
						ar.clear();
						continue;
					}
				}
				rclast = rc;
				_arrows.push(ar);
			}
			
		}
		
		private function clearArrows():void{
			
			var n:int;
			var ar:MapAoPathArrow
			//var layer:FeatureLayer = this.layer as FeatureLayer;
			
			for(n=0;n< this._arrows.length;n++){
				ar = _arrows[n] as MapAoPathArrow;
				//layer.removeFeature(ar);
				ar.clear();
				
				ar = null;
			}
			_arrows.splice(0); // empty array
			_arrows = new Array();
			
		}
		
		private function clearTickMarkers():void{
			
			var n:int;
			var f:MapAoPathMarker ;
			//var layer:FeatureLayer = this.layer as FeatureLayer;
			trace("clear Tick Markers:",_markers.length);
			for(n=0;n<this._markers.length;n++){
				f = _markers[n] as MapAoPathMarker;
				f.clear();
				//layer.removeFeature(f);				
			}
			_markers.splice(0); // empty array
			_markers = new Array();
			
		}
		
		//显示时间标记 
		private function createTickMarkers(ticks:Array):void{
			var label:MLabel;
			//var m:MMarker;
			
			
			var f:MapAoPathMarker ;
			var n:int;
			//var layer:FeatureLayer = this.layer as FeatureLayer;
			
			//clearTickMarkers()867439497
			//27037387 春纪
			
			var d:Object;
			var lasttick:Object = null;
			for(n=0;n<ticks.length;n++){				
				d = ticks[n];

				//检查两个 marker是否相碰撞
				var rc1:Rectangle ;
				var rc2:Rectangle;
				var rc3:Rectangle;

				var m:MapAoPathMarker;
				m = new MapAoPathMarker(this);
				m.setData(d);
				
				rc1 = m.getBounds();
				rc3 = this._mao.getMarker().getBounds();
				//trace("mao marker bounds:",rc3.toString());
				
				//不允许timeticker 与 map ao图标对象相交
				if( rc1.intersects(rc3) ){
					//layer.removeFeature(m);
					m.clear();
					m = null;					
					continue;
				}
				
				var collison:Boolean = false;
				//与之前的markers进行碰撞检测
				for( var nn:int=0;nn<_markers.length;nn++){
					var mm:MapAoPathMarker = _markers[nn] as MapAoPathMarker;
					rc2 =  mm.getBounds();
					if( rc1.intersects(rc2)){
						collison = true;
						break;
					}
				}
				if( collison ){
					//layer.removeFeature(m);
					m.clear();
					m = null;
					continue;
				} 				
				
				_markers.push(m); //不与相邻marker相交则显示				
			}
			//删除最后一个，无奈，显示与ao‘对象叠加到一起了
			/* //开放一下代码，导致拖动时会使估计线卡住，不知何原因
			if(_markers.length){
				var m1:MapAoPathMarker ;//= _markers[_markers.length-1] as MapAoPathMarker;
				
				m1 = _markers.pop() as MapAoPathMarker;
				m1.clear();
			}
			*/
			
			
		}
		
		private  function getDefaultStyle():Style {
			
			var rule:Rule = new Rule();
			rule.name = "Default rule";
			rule.symbolizers.push(new LineSymbolizer(new Stroke(0xff0000, 3,0.5)));
			//rule.symbolizers.push(new LineSymbolizer(new Stroke(0x40A6D9, 1)));
			
			var style:Style = new Style();
			style.name = "Default line style";
			style.rules.push(rule);
			return style;
		}
		
		
	}
}