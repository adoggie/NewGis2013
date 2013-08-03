package com.sw2us.mapext
{
	import flash.display.Sprite;
	import flash.events.KeyboardEvent;
	import flash.events.MouseEvent;
	
	import org.openscales.core.Map;
	import org.openscales.core.events.ZoomBoxEvent;
	import org.openscales.core.handler.Handler;
	import org.openscales.core.handler.mouse.DragHandler;
	import org.openscales.geometry.basetypes.Bounds;
	import org.openscales.geometry.basetypes.Location;
	import org.openscales.geometry.basetypes.Pixel;
	
	public class ZoomBoxHandlerExt extends Handler
	{		
		private var _startCoordinates:Location = null;		
		private var _fillColor:uint = 0xFF0000
		private var _drawContainer:Sprite = new Sprite();     
		private var _ctrlpressed:Boolean = false;
		
		private static const STATUS_UNSET:int =0;
		private static const STATUS_SHIFTPRESSED:int = 0x01 ;
		private static const STATUS_CTRLPRESSED:int = 0x10;
		
		private var _opkeys:int = 0;
		
		public function ZoomBoxHandlerExt(map:Map=null, active:Boolean=false):void{
			super(map, active);
			map.addEventListener(KeyboardEvent.KEY_DOWN,onKeyEvent);
		}
		
		private function onKeyEvent(e:KeyboardEvent):void{
			if(	 e.ctrlKey ){
				_opkeys|=STATUS_CTRLPRESSED;
			}else{
				_opkeys&=~STATUS_CTRLPRESSED;
			}
			if(_opkeys){
				this.deactiveDrag();
			}
		}
		
		override protected function registerListeners():void{
			if (this.map) {
				this.map.addEventListener(MouseEvent.MOUSE_DOWN,startBox);
				this.map.addEventListener(MouseEvent.MOUSE_UP,endBox);     
				map.addEventListener(MouseEvent.MOUSE_MOVE,expandArea);
			}
		}
		
		override protected function unregisterListeners():void{
			if (this.map) {
				this.map.removeEventListener(MouseEvent.MOUSE_DOWN,startBox);
				this.map.removeEventListener(MouseEvent.MOUSE_UP,endBox);
				this.map.removeEventListener(MouseEvent.MOUSE_MOVE,expandArea);
				
			}
		}
		
		override public function set active(value:Boolean):void {
			super.active  = value;			
		}
		
		override public function set map(value:Map):void{
			super.map = value;
			if(map!=null){map.addChild(_drawContainer);}
		}
		
		private function startBox(e:MouseEvent) : void {
			if(_opkeys){ //  放大
				trace("startBox...");
				this.deactiveDrag(); //禁止拖动
				//this.map.addEventListener(MouseEvent.MOUSE_MOVE,expandArea);
				_drawContainer.graphics.beginFill(_fillColor,0.5);
				_drawContainer.graphics.drawRect(map.mouseX,map.mouseY,1,1);
				_drawContainer.graphics.endFill();
				this._startCoordinates = this.map.getLocationFromMapPx(new Pixel(map.mouseX, map.mouseY));
				_ctrlpressed = true;
			}
		}
		
		private function endBox(e:MouseEvent) : void {
			_ctrlpressed = false;
			//if(_opkeys == 0) return;
			if(this._startCoordinates == null){
				return;
			}
			//this.map.removeEventListener(MouseEvent.MOUSE_MOVE,expandArea);
			/*
			this.map.removeEventListener(MouseEvent.MOUSE_DOWN,startBox);
			this.map.removeEventListener(MouseEvent.MOUSE_UP,endBox);
			*/
			_drawContainer.graphics.clear();
			var endCoordinates:Location = this.map.getLocationFromMapPx(new Pixel(map.mouseX, map.mouseY));
			if(_startCoordinates != null) {
				if(_startCoordinates.equals(endCoordinates)){
					this.map.moveTo(endCoordinates);
				}else{
					this.map.zoomToExtent(new Bounds(Math.min(_startCoordinates.lon,endCoordinates.lon),
						Math.min(endCoordinates.lat,_startCoordinates.lat),
						Math.max(_startCoordinates.lon,endCoordinates.lon),
						Math.max(endCoordinates.lat,_startCoordinates.lat),
						endCoordinates.projection));
				}
			}
			this._startCoordinates = null;
			//this.active = false;
			//activeDrag();
			//this.map.dispatchEvent(new ZoomBoxEvent(ZoomBoxEvent.END));
			_opkeys = 0;
		}
		
		// onMouseMove
		private function expandArea(e:MouseEvent) : void {
			if(this._startCoordinates == null){
				return;
			}
			if(  _opkeys ){				
				var ll:Pixel = map.getMapPxFromLocation(_startCoordinates);
				_drawContainer.graphics.clear();
				_drawContainer.graphics.lineStyle(1,_fillColor);
				_drawContainer.graphics.beginFill(_fillColor,0.25);
				_drawContainer.graphics.drawRect(ll.x,ll.y,map.mouseX - ll.x,map.mouseY - ll.y);
				_drawContainer.graphics.endFill();
			}
		}
		
		/**
		 * Active paning
		 * User can pan the map
		 */
		public function activeDrag():void{
			var handler:Handler;
			for each(handler in this.map.handlers) {
				if (handler is DragHandler) {
					handler.active = true;
				}
			}
		}
		
		/**
		 * Deactive paning
		 * User can't pan map anymore
		 */
		public function deactiveDrag():void{
			var handler:Handler;
			for each(handler in this.map.handlers) {
				if (handler is DragHandler) {
					handler.active = false;
				}
			}
		}
		////////////////
	}
}


