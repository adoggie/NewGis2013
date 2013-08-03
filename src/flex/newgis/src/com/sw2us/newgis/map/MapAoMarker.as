/**
 * MapaoMarker - Map ActiveObject Marker
 * 
 */ 


/* fxg 

import spark.core.SpriteVisualElement;
private var myStar:SpriteVisualElement;
private function drawStar():void {
// Create new instances of star.fxg as if it were a local component.
for (var i:int = 0; i<4; i++) {
myStar = new star();
myStar.x = 50 + (i*75);
myStar.y = 50;
myStar.height = 100 - (i*30);
myStar.width = 100 - (i*30);
myStar.alpha = 1 - (i*.2);
myStar.rotationX = 20 + (i*20);
addElement(myStar);
}
}

fxg 图形旋转都是顺时针旋转

*/
package com.sw2us.newgis.map
{
	import com.sw2us.newgis.ActiveObject;
	import com.sw2us.newgis.AppResource;
	
	import flash.display.Bitmap;
	import flash.display.BitmapData;
	import flash.display.DisplayObject;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.text.TextField;
	import flash.text.TextFormat;
	import flash.text.TextFormatAlign;
	
	import org.openscales.core.Map;
	import org.openscales.core.events.MapEvent;
	import org.openscales.core.feature.*;
	import org.openscales.core.layer.FeatureLayer;
	import org.openscales.core.layer.Layer;
	import org.openscales.core.request.DataRequest;
	import org.openscales.core.style.Style;
	import org.openscales.geometry.Point;
	import org.openscales.geometry.basetypes.Location;
	import org.openscales.geometry.basetypes.Pixel;
	
	
	public class MapAoMarker extends PointFeature 
	{
		//private var _layer:Layer= null;
		//private var _ao:ActiveObject = null;
		private var _ispathshow:Boolean = false;
		private var _marker:CustomMarker = null; //图上运动对象图标 
		private var _text:String="" ;			//显示文本
		//private var _visible:Boolean = true; //是否显示 说
		private var _textVisible:Boolean = true; //是否显示文本提示内容
		private var _mao:MapAo=null;
		
		private var _textAnno:TextField ;
		
		private var _clip:DisplayObject;
		private var _xOffset:Number;
		private var _yOffset:Number;
		private var _req:DataRequest=null;
		
		private var _symbol:Sprite = null;
		
		
		public function MapAoMarker(mao:MapAo,layer:MapAoLayer)
		{
			super(null,null,null);
			_mao = mao;			
			//this.visible = false;
			//ao.addMapObject(this);
			//var flayer:FeatureLayer = layer as FeatureLayer;
			layer.addFeature(this);
			
			//this.layer.map.addEventListener(MapEvent.MOVE_END,onMapMoveEnd);	
		}
	 	
		private function onMapMoveEnd(event:MapEvent):void{
			draw();
		}
		
		
		
		public function deleteThis():void{
			if(_clip){
				this.removeChild(_clip);				
			}
			if(_textAnno){
				this.removeChild(_textAnno);
			}
			var flayer:FeatureLayer = this.layer as FeatureLayer;
			flayer.removeFeature(this);
		} 
		
		
		public function setMarkerIcon(icon:MapAoMarkerIconArrow):void{
			loadDisplayObject(icon);
		}
		
		public function set textVisible(v:Boolean):void{
			_textVisible = v;
			_textAnno.visible = v;
		}
		
		public function get textVisible():Boolean{
			return _textAnno.visible;
		}
		
		public function getMap():Map{
			return this.layer.map;
		}
		
		public function getMapAo():MapAo{
			return _mao;
		}
		
		public function getText():String{
			return _text;
		}
		
		public function setText(text:String):void{
			_text = text;
			this.loadDisplayObject2(this._clip);
		}
		
		public function reCreateSymbol():Boolean{
			//_symbol = null;
			var symbol:Sprite = new Sprite();
			var disobj:DisplayObject;
			var gps:Object = _mao.getActiveObject().getGpsData();
			var angle:Number= 0;
			if( gps ){
				angle = gps.angle;
			}
			disobj =AppResource.instance().getAoBitmapByAngle(angle);
			symbol.addChild(disobj);
			
			var txt:TextField= new TextField();
			txt.text = _mao.getActiveObject().getInfo().name;
			txt.width = 60;txt.height= 25;
			//txt.border = true;
			//txt.borderColor = 0xff0000;
			txt.autoSize ="center";
			//txt.backgroundColor = 0xffff00;
			//txt.background = true;
			txt.antiAliasType = flash.text.AntiAliasType.ADVANCED;
			//txt.alpha = 0.5;
			var f:TextFormat = new TextFormat();
			f.align =TextFormatAlign.CENTER;
			txt.setTextFormat(f);
			symbol.addChild(txt);
			this.loadDisplayObject(symbol);
			return true;
		}
		
		///////////////////////////////////////
		public static function create(mao:MapAo,
														 layer:MapAoLayer,
														 dispObj:DisplayObject,
														 point:Location,
														 data:Object=null,
														 xOffset:Number=0,
														 yOffset:Number=0):MapAoMarker {
			var ret:MapAoMarker = new MapAoMarker(mao,layer);
			ret.geometry = new Point(point.x,point.y);
			ret.data = data;
			ret.xOffset = xOffset;
			ret.yOffset = yOffset;
			
			//ret.setMarkerIcon( new MapAoMarkerIconArrow());
			ret.loadDisplayObject(dispObj);
			//ret.textVisible = false;
			
			return ret;
		}
		
		public static function create2(
									  layer:MapAoLayer,
									  dispObj:DisplayObject,
									  point:Location,
									  data:Object=null,
									  xOffset:Number=0,
									  yOffset:Number=0):MapAoMarker {
			var ret:MapAoMarker = new MapAoMarker(null,layer);
			ret.geometry = new Point(point.x,point.y);
			ret.data = data;
			ret.xOffset = xOffset;
			ret.yOffset = yOffset;
			
			//ret.setMarkerIcon( new MapAoMarkerIconArrow());
			ret.loadDisplayObject2(dispObj);
			//ret.textVisible = false;
			
			return ret;
		}
		
		public function setAngle(a:Number):void{
			loadDisplayObject(AppResource.instance().getAoBitmapByAngle(a));
		}

		
		override public function clone():Feature {
			var ret:CustomMarker = new CustomMarker();
			ret.geometry = this.point.clone();
			ret.data = this.data;
			ret.xOffset = this._xOffset;
			ret.yOffset = this._yOffset;
			var bitmap:Bitmap = new Bitmap();
			bitmap.bitmapData = new BitmapData(this._clip.width, this._clip.height, false, 0x000000);
			bitmap.bitmapData.draw(this._clip, null, null, null, null);
			ret.loadDisplayObject(bitmap);
			return ret;
		}
		
		public function set xOffset(value:Number):void {
			this._xOffset = value;
			if(this.layer)
				this.draw();
		}
		
		public function get xOffset():Number {
			return this._xOffset;
		}
		
		public function set yOffset(value:Number):void {
			this._yOffset = value;
			if(this.layer)
				this.draw();
		}
		
		public function get yOffset():Number {
			return this._yOffset;
		}
		
		public function loadUrl(url:String):void {
			this._req = new DataRequest(url,onSuccess, onFailure);
			this._req.send();
		}
		
		
		
		public function loadDisplayObject2(clip:DisplayObject):void {
			if(this._clip)
				this.removeChild(this._clip);
			if(this._textAnno){
				this.removeChild(this._textAnno);
			}
			
			this._clip = clip;
			this.addChild(this._clip);
			
			//添加文本标注
			{
				_textAnno = new TextField();
				_textAnno.text = getText();
				_textAnno.width = 60;_textAnno.height= 25;
				_textAnno.border = true;
				_textAnno.borderColor = 0xff0000;
				_textAnno.autoSize ="center";
				_textAnno.backgroundColor = 0xff00ff;
				_textAnno.background = true;
				_textAnno.antiAliasType = flash.text.AntiAliasType.ADVANCED;
				_textAnno.alpha = 0.7;
				
				var f:TextFormat = new TextFormat();
				f.align =TextFormatAlign.CENTER;
				f.color = 0x0000ff;
				_textAnno.setTextFormat(f);
				this.addChild(_textAnno);
				//this.setChildIndex(_textAnno,100);
			}
			if(this.layer)
				this.draw();
		}
		
		public function loadDisplayObject(clip:DisplayObject):void {
			if(this._clip)
				this.removeChild(this._clip);
			if(this._textAnno){
				this.removeChild(this._textAnno);
			}
			
			this._clip = clip;
			this.addChild(this._clip);
			
			//添加文本标注
			{
				_textAnno = new TextField();
				_textAnno.text = _mao.getActiveObject().getInfo().name;
				_textAnno.width = 60;_textAnno.height= 25;
				_textAnno.border = true;
				_textAnno.borderColor = 0xff0000;
				_textAnno.autoSize ="center";
				
				_textAnno.backgroundColor = 0xffffff;
				_textAnno.background = true;
				_textAnno.antiAliasType = flash.text.AntiAliasType.ADVANCED;
				_textAnno.alpha = 0.8;
				var f:TextFormat = new TextFormat();
				f.align =TextFormatAlign.CENTER;
				_textAnno.setTextFormat(f);
				this.addChild(_textAnno);
				//this.setChildIndex(_textAnno,100);
			}
			if(this.layer)
				this.draw();
		}
		
		override public function draw():void {
			if(!this._clip)
				return;
			// we compute the location of the marker
			var x:Number;
			var y:Number;
			var resolution:Number = this.layer.map.resolution;
			var dX:int = -int(this.layer.map.layerContainer.x) + this.left;
			var dY:int = -int(this.layer.map.layerContainer.y) + this.top;
			
			var icon:MapAoMarkerIconArrow = this._clip as MapAoMarkerIconArrow;
			
			x = dX - (this._clip.width/2) + _xOffset + point.x / resolution;
			y = dY - (this._clip.height/2) + _yOffset - point.y / resolution;
			_clip.x = x;
			_clip.y = y;
		//	var px:Pixel = layer.map.getLayerPxFromLocation( this.lonlat);
		//	_clip.x = px.x;
		//	_clip.y = px.y;
			
			trace("clip size:",_clip.width,_clip.height);
			_textAnno.x = _clip.width/2 + _clip.x - _textAnno.width/2;
			_textAnno.y = _clip.height + _clip.y ;
		}
		
		public function setLocation(loc:Location):void{
			geometry = new Point(loc.lon,loc.lat);
			draw();	
		}
		
		private function onSuccess(e:Event):void {
			this.loadDisplayObject(Bitmap(this._req.loader.content));
			this._req.destroy();
			this._req = null;
		}
		
		private function onFailure(e:Event):void {
			this._req.destroy();
			this._req = null;
			//this.loadDisplayObject(new _defaultImage());
			this._xOffset = 0;
			this._yOffset = 0;
		}
		
		//设置绘制成焦点ao 
		public function set drawFocused(b:Boolean):void{
			
		}
		
	}
}