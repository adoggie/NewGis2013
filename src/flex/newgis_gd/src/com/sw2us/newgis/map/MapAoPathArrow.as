package com.sw2us.newgis.map
{
	/*
	 * MapAoPathArrow - 行驶轨迹方向箭头 
	*/
	
	import com.mapabc.maps.api.MFlexMap;
	import com.mapabc.maps.api.basetypes.MLngLat;
	import com.sw2us.newgis.ActiveObject;
	import com.sw2us.newgis.assets.comps.PathMarker;
	
	import flash.display.Bitmap;
	import flash.display.BitmapData;
	import flash.display.DisplayObject;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.geom.Point;
	import flash.geom.Rectangle;
	import flash.text.TextField;
	import flash.text.TextFormat;
	import flash.text.TextFormatAlign;
	
	import mx.core.UIComponent;
	
	import org.openscales.core.Map;
	import org.openscales.core.StringUtils;
	import org.openscales.core.feature.*;
	import org.openscales.core.layer.FeatureLayer;
	import org.openscales.core.layer.Layer;
	import org.openscales.core.request.DataRequest;
	import org.openscales.core.style.Style;
	import org.openscales.geometry.Point;
	import org.openscales.geometry.basetypes.Location;
	import org.openscales.geometry.basetypes.Pixel;
	
	import spark.core.SpriteVisualElement;
	
	//public class MapAoPathArrow extends PointFeature  
	public class MapAoPathArrow extends Sprite
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
		private var _startpt:Location;
		private var _endpt:Location;
		
		private var _marker:DisplayObject;
		//箭头的大小  
		public var Radius:int=6;  
		public var FromPoint:flash.geom.Point;  
		public var ToPoint:flash.geom.Point;
		public var LineColor:uint=0xff0000;  
		
		
		
		
		public function MapAoPathArrow(path:MapAoPath,pt1:Location,pt2:Location){
		//public function MapAoPathArrow(layer:FeatureLayer,pt1:Location,pt2:Location){
			//super(null,null,null);
			//super();
			_path = path;
			_startpt = pt1;
			_endpt = pt2;
			
			//FromPoint = path.layer.getMapPxFromLocation(pt1);
			//ToPoint = path.layer.getMapPxFromLocation(pt2);
			var map:MFlexMap;
			map = _path.mao.layer.map.getMap() as MFlexMap;
			//var pt:Point;
			FromPoint = map.fromLatLngToContainerPixel(new MLngLat(pt1.lon,pt1.lat));
			ToPoint = map.fromLatLngToContainerPixel(new MLngLat(pt2.lon,pt2.lat));
			 
			
			_data = null;
			
			update();
			
			map.addChild( this);
			
			
			//var layer:FeatureLayer = path.layer as FeatureLayer;
			//layer.addFeature(this);
			//layer.addChildAt(this,0);
			//super.visible = true;
		}
		
	  
		//设置gps数据 
		public function setData(gps:Object):void{
			_data = gps;
			
		}
		
		//获得线的角度
		private function getAngle():Number
		{  
			var  tmpx:int=ToPoint.x-FromPoint.x ;  
			var tmpy:int=FromPoint.y -ToPoint.y ;  
			var angle:Number= Math.atan2(tmpy,tmpx)*(180/Math.PI);  
			return angle;  
		}  
		
		public function clear():void{
			var map:MFlexMap;
			map = _path.mao.layer.map.getMap() as MFlexMap;
			map.removeChild(this);
		}
		 
		public function getBounds_():Rectangle{
			var r:Rectangle;
			//r = new Rectangle(this.x,this.y,this.width,this.height);
			
			var map:MFlexMap;
			map = _path.mao.layer.map.getMap() as MFlexMap;
			r = super.getBounds(map);
			return r;
		}
		
		public function update():void{
			
			var x:Number;
			var y:Number;
			//var resolution:Number = this.layer.map.resolution;
			
			//this.geometry = new Point(_endpt.lon,_endpt.lat);
			/*
			x = this.left;
			y = this.top;
			var dX:int = -int(this.layer.map.layerContainer.x) + this.left;
			var dY:int = -int(this.layer.map.layerContainer.y) + this.top;
			
			x = dX +  _endpt.lon / resolution;
			y = dY + _endpt.lat / resolution;
			//this.graphics.drawRect(x, y, 5, 5);
			*/
			/*
			var map:MFlexMap;
			map = _path.mao.layer.map.getMap() as MFlexMap;
			//var pt:Point;
			FromPoint = map.fromLatLngToContainerPixel(new MLngLat(pt1.lon,pt1.lat));
			ToPoint = map.fromLatLngToContainerPixel(new MLngLat(pt12.lon,pt2.lat));
			*/
			
			this.graphics.clear();  
			this.graphics.lineStyle(1,LineColor,1);  
			
			
			if(1)  
			{  
				var angle:Number =getAngle();  
				/*
				if( angle>180&& angle <360){
					x+=1;
				}else{
					x-=1;
				}
				if( angle >90 && angle<270){
					x+=1;
				}else{
					x-=1
				}*/
				
				var centerX:int=ToPoint.x-Radius * Math.cos(angle *(Math.PI/180)) ;  
				var centerY:int=ToPoint.y+Radius * Math.sin(angle *(Math.PI/180)) ;  
				var topX:int=ToPoint.x ;  
				var topY:int=ToPoint.y  ;  
				
				/*
				var centerX:int=x-Radius * Math.cos(angle *(Math.PI/180)) ;  
				var centerY:int=+Radius * Math.sin(angle *(Math.PI/180)) ;  
				var topX:int=x ;  
				var topY:int=y  ;
				*/
				
				var leftX:int=centerX + Radius * Math.cos((angle +120) *(Math.PI/180))  ;  
				var leftY:int=centerY - Radius * Math.sin((angle +120) *(Math.PI/180))  ;  
				
				var rightX:int=centerX + Radius * Math.cos((angle +240) *(Math.PI/180))  ;  
				var rightY:int=centerY - Radius * Math.sin((angle +240) *(Math.PI/180))  ;  
				
				this.graphics.beginFill(LineColor,1);  
				
				this.graphics.lineStyle(1,LineColor,1);  
				
				this.graphics.moveTo(topX,topY);  
				this.graphics.lineTo(leftX,leftY);  
				
				this.graphics.lineTo(centerX,centerY);  
				
				this.graphics.lineTo(rightX,rightY);  
				this.graphics.lineTo(topX,topY);  
				
				this.graphics.endFill();  
			}  
		}
		
		/*
		override public function draw():void {
			//super.draw();
			this.update();
		}
		*/
		
		
		
	
		
		
	}
}