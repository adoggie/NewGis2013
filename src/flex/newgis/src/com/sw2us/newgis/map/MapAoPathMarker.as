package com.sw2us.newgis.map
{
	/*
	 * PathMarker - 显示路径gps节点的方向指示，同时可以切换显示时间 
		两个pathMarker不允许叠加显示
	*/
	
	import com.sw2us.newgis.ActiveObject;
	import com.sw2us.newgis.assets.comps.PathMarker;
	
	import flash.display.Bitmap;
	import flash.display.BitmapData;
	import flash.display.DisplayObject;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.text.TextField;
	import flash.text.TextFormat;
	import flash.text.TextFormatAlign;
	
	import org.openscales.core.Map;
	import org.openscales.core.StringUtils;
	import org.openscales.core.feature.*;
	import org.openscales.core.layer.FeatureLayer;
	import org.openscales.core.layer.Layer;
	import org.openscales.core.request.DataRequest;
	import org.openscales.core.style.Style;
	import org.openscales.geometry.Point;
	import org.openscales.geometry.basetypes.Location;
	
	import spark.core.SpriteVisualElement;
	
	public class MapAoPathMarker extends PointFeature
	{		 
		private var _ispathshow:Boolean = false;
	//	private var _marker:CustomMarker = null; //图上运动对象图标 
		private var _text:String ;			//显示文本		
		private var _textVisible:Boolean = true; //是否显示文本提示内容
		private var _mao:MapAo;
		
		private var _clip:DisplayObject;
		private var _xOffset:Number=0;
		private var _yOffset:Number=0;
		private var _req:DataRequest=null;
		
		private var _path:MapAoPath;
		private var _showmode:int;
		private var _data:Object;
		
		private var _marker:DisplayObject;
		
		
		public static const SHOWMODE_TIME:int = 1;		//显示时间
		public static const SHOWMODE_ANGLE:int = 2;  //显示方向
		public static const SHOWMODE_DEFAULT:int =SHOWMODE_ANGLE;
		
		public function MapAoPathMarker(path:MapAoPath)
		{
			super(null,null,null);
			_path = path;	
			var layer:FeatureLayer = _path.layer as FeatureLayer;
			layer.addFeature(this);			
			
			this.visible = true;
			_showmode = SHOWMODE_DEFAULT;
			_showmode = SHOWMODE_TIME;
			_data = null;
			_marker = null;
		}
		
		public function setShowMode(mode:int):void{
			if( _showmode != mode){
				_showmode = mode;
				this.update();
			}			
		}
		
		public function getShowMode():int{
			return _showmode;
		}
		
		//设置gps数据 
		public function setData(gps:Object):void{
			_data = gps;
			update();
		}
		
		
		
		public function update():void{			
			/*
			if(this.visible == false){
				return;
			}*/
			this.geometry = new Point(_data.lon,_data.lat);
			
			if( _showmode ==  SHOWMODE_DEFAULT){
				var m:SpriteVisualElement = new SpriteVisualElement();
				m = new PathMarker();
				m.rotationX = m.width/2;
				m.rotationY = m.height/2;
				m.rotation = _data.angle; //旋转角度
				loadDisplayObject(m);					
			}else {
				var t:Date = new Date(_data.time*1000);
				var txt:TextField = new TextField();
				//txt.text = org.openscales.core.StringUtils.sprintf("%02d:%02d:%02d", t.hours,t.minutes,t.seconds);
				txt.text = org.openscales.core.StringUtils.sprintf("%02d:%02d", t.hours,t.minutes);
				//txt.width = 60;
				txt.height= 25;
				txt.border = true;
				txt.borderColor = 0xff0000;
				txt.autoSize ="center";
				txt.backgroundColor = 0xffff00;
				txt.background = true;
				txt.antiAliasType = flash.text.AntiAliasType.ADVANCED;
				txt.alpha = 0.7;
				var f:TextFormat = new TextFormat();
				f.align = TextFormatAlign.CENTER;
				f.bold = true;
				txt.setTextFormat(f);
				loadDisplayObject(txt);
			}						
		}
		
		public function clear():void{
			if(this._clip){
				this.removeChild(this._clip);				
			}
			this._clip = null;
			if(this.layer)
				this.draw();
			this.visible = false;
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
	//	private static  var addnum:int = 0;
		public function loadDisplayObject(clip:DisplayObject):void {
			if(this._clip)
				this.removeChild(this._clip);
			this._clip = clip;
			this.addChild(this._clip);
		//	trace("ticktime num",++addnum);
			
			//trace("clip size",this._clip.width,this._clip.height);
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
			x = dX - (this._clip.width/2) + _xOffset + point.x / resolution;
			y = dY - (this._clip.height/2) + _yOffset - point.y / resolution;
			_clip.x = x;
			_clip.y = y;
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
		
		
		
	}
}