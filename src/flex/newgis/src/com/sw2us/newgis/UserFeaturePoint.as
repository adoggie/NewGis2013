package com.sw2us.newgis
{	
	import com.sw2us.newgis.event.UserFeatureEvent;
	
	import flash.display.Bitmap;
	import flash.display.BitmapData;
	import flash.display.DisplayObject;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.MouseEvent;
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
	

	public class UserFeaturePoint extends PointFeature {
			//private var _layer:Layer= null;
			//private var _ao:ActiveObject = null;
			private var _ispathshow:Boolean = false;
			private var _marker:CustomMarker = null; //图上运动对象图标 
			private var _text:String ;			//显示文本
			//private var _visible:Boolean = true; //是否显示 说
			private var _textVisible:Boolean = true; //是否显示文本提示内容
			private var _mao:MapAo;
			
			private var _textAnno:TextField ;
			
			private var _clip:DisplayObject;
			private var _xOffset:Number;
			private var _yOffset:Number;
			private var _req:DataRequest=null;
			
			private var _symbol:Sprite = null;
			
			
			public function UserFeaturePoint()
			{
				super(null,null,null);				
				
				//this.layer.map.addEventListener(MapEvent.MOVE_END,onMapMoveEnd);	
				addEventListener(MouseEvent.CLICK,onFeatureIconClick);
			}

			private function onFeatureIconClick(evt:MouseEvent):void{
				this.dispatchEvent(new UserFeatureEvent(UserFeatureEvent.USERFEATURE_CLICK,this));
			}
			
			public override function destroy():void{
				if(_clip){
					this.removeChild(_clip);								
					_clip = null;
				}
				
				if(_textAnno){
					this.removeChild(_textAnno);
					_textAnno = null;
				}
				super.destroy();
			} 
			
			public function set textVisible(v:Boolean):void{
				_textVisible = v;
				_textAnno.visible = v;
			}
			
			public function get textVisible():Boolean{
				return _textAnno.visible;
			}
			
			public function getText():String{
				return _text;
			}
			
			public function setText(text:String):void{
				_text = text;
				if(this._textAnno){
					this.removeChild(this._textAnno);
				}				
	
				{
					_textAnno = new TextField();
					_textAnno.text = text;
					//_textAnno.width = 60;
					_textAnno.height= 25;
					_textAnno.border = true;
					_textAnno.borderColor = 0xff0000;
					_textAnno.autoSize ="center";
					//txt.backgroundColor = 0xffff00;
					//txt.background = true;
					_textAnno.antiAliasType = flash.text.AntiAliasType.ADVANCED;
					//txt.alpha = 0.5;
					var f:TextFormat = new TextFormat();
					f.align =TextFormatAlign.CENTER;
					_textAnno.setTextFormat(f);
					this.addChild(_textAnno);				
				}
				if(this.layer)
					this.draw();
			}

			public function setIcon(clip:DisplayObject):void{
				if(this._clip)
					this.removeChild(this._clip);
				this._clip = clip;
				this.addChild(this._clip);
				if(this.layer)
					this.draw();
			}
			
			public function getIcon():DisplayObject{
				return _clip;
			}
			
			///////////////////////////////////////
			public static function create(
										  layer:FeatureLayer,
										  dispObj:DisplayObject,
										  point:Location,
										  data:Object=null,
										  xOffset:Number=0,
										  yOffset:Number=0):UserFeaturePoint {
				var ftr:UserFeaturePoint = new UserFeaturePoint(layer);
				ftr.geometry = new Point(point.x,point.y);
				ftr.data = data;
				ftr.xOffset = xOffset;
				ftr.yOffset = yOffset;
				ftr.setIcon(dispObj);
				ftr.setText(data.name); // feature name with server delivered
				layer.addFeature(ftr);			
				
				return ftr;
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
			
		
			//icon在上且x，y方向居中，text紧靠icon下方，文本居中
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
				//trace("clip size:",_clip.width,_clip.height);
				_textAnno.x = _clip.width/2 + _clip.x - _textAnno.width/2;
				_textAnno.y = _clip.height + _clip.y ;
			}
		}
	}