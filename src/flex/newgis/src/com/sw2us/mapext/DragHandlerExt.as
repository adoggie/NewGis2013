/**
 *  2011.8.17 scott  
 *   1. 新的draghandler，支持 zoomIn(ctrl),zoomOut(alt)
 * 
 * 
 * 	   使用方法: 
 *        去除fxmap中的<DragHandler/>
 *        var draghandler:DragHandlerExt = new DragHandlerExt(fxmap.map,true);
 * 
 * 
 * */

package com.sw2us.mapext
{
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.MouseEvent;
	
	import org.openscales.core.Map;
	import org.openscales.core.Trace;
	import org.openscales.core.events.MapEvent;
	import org.openscales.core.handler.Handler;
	import org.openscales.geometry.basetypes.Bounds;
	import org.openscales.geometry.basetypes.Location;
	import org.openscales.geometry.basetypes.Pixel;

	
	public class DragHandlerExt extends Handler
	{
	 
		private var _startCoordinates:Location = null;		
		private var _fillColor:uint = 0xFF0000;
		private var _drawContainer:Sprite = new Sprite();     
		////////////////////////////////////////////////////////////
		
		private var _startCenter:Location = null;
		private var _start:Pixel = null;
		private var _offset:Pixel = null;
		
		private var _firstDrag:Boolean = true;
		
		private var _dragging:Boolean = false;
		
		/**
		 *Callbacks function
		 */
		private var _onStart:Function=null;
		private var _oncomplete:Function=null;
	 
		public function DragHandlerExt(map:Map=null,active:Boolean=true)
		{
			super(map,active);
			if( map !=null){
				map.addChild(_drawContainer);
			}
		}
		
		override protected function registerListeners():void{
			if (this.map) {
				this.map.addEventListener(MouseEvent.MOUSE_DOWN, this.onMouseDown);
				this.map.addEventListener(MouseEvent.MOUSE_UP, this.onMouseUp);
				//map.addEventListener(MouseEvent.MOUSE_MOVE,expandArea);
			}
		}
		
		override protected function unregisterListeners():void{
			if (this.map) {
				this.map.removeEventListener(MouseEvent.MOUSE_DOWN, this.onMouseDown);
				this.map.removeEventListener(MouseEvent.MOUSE_UP, this.onMouseUp);
			}
		}
	 
		protected function onMouseDown(event:MouseEvent):void
		{
			if(event.ctrlKey || event.altKey){
				this.map.addEventListener(MouseEvent.MOUSE_MOVE,this.expandArea);
				this.startBox(event);
				return;
			}	 
			
			if (_firstDrag) {
				this.map.stage.addEventListener(MouseEvent.MOUSE_UP,this.onMouseUp);
				_firstDrag = false;
			}
			
			this.map.stage.addEventListener(MouseEvent.MOUSE_MOVE,this.onMouseMove);
			
			this._start = new Pixel(this.map.mouseX,this.map.mouseY);
			this._offset = new Pixel(this.map.mouseX - this.map.layerContainer.x,this.map.mouseY - this.map.layerContainer.y);
			this._startCenter = this.map.center;
			this.map.buttonMode=true;
			this._dragging=true;
			this.map.dispatchEvent(new MapEvent(MapEvent.DRAG_START, this.map));
			if(this.onstart!=null)
				this.onstart(event as MouseEvent);
		}
		
		protected function onMouseMove(event:MouseEvent):void  {
			this.map.layerContainer.x = this.map.layerContainer.parent.mouseX - this._offset.x;
			this.map.layerContainer.y = this.map.layerContainer.parent.mouseY - this._offset.y;
			if(this.map.bitmapTransition) {
				this.map.bitmapTransition.x = this.map.bitmapTransition.parent.mouseX - this._offset.x;
				this.map.bitmapTransition.y = this.map.bitmapTransition.parent.mouseY - this._offset.y;
			}
			
			// Force update regardless of the framerate for smooth drag
			event.updateAfterEvent();
		}
		
	 
		protected function onMouseUp(event:MouseEvent):void {
			if(this._startCoordinates!=null){
				this.map.removeEventListener(MouseEvent.MOUSE_MOVE,this.onMouseMove);
				this.endBox(event);
				return;
			}
			
			if((!this.map) || (!this.map.stage))
				return;
			
			this.map.stage.removeEventListener(MouseEvent.MOUSE_MOVE,this.onMouseMove);
			
			this.map.buttonMode=false;
			this.done(new Pixel(this.map.mouseX, this.map.mouseY));
			// A MapEvent.MOVE_END is emitted by the "set center" called in this.done
			this._dragging=false;
			if (this.oncomplete!=null)
				this.oncomplete(event as MouseEvent);
		}
		
		// Getters & setters as3
		/**
		 * To know if the map is dragging
		 */
		public function get dragging():Boolean
		{
			return this._dragging;
		}
		public function set dragging(dragging:Boolean):void
		{
			this._dragging=dragging;
		}
		/**
		 * Start's callback this function is call when the drag starts
		 */
		public function set onstart(onstart:Function):void
		{
			this._onStart=onstart;
		}
		public function get onstart():Function
		{
			return this._onStart;
		}
		/**
		 * Stop's callback this function is call when the drag ends
		 */
		public function set oncomplete(oncomplete:Function):void
		{
			this._oncomplete=oncomplete;
		}
		public function get oncomplete():Function
		{
			return this._oncomplete;
		}
		
		/**
		 * This function is used to recenter map after dragging
		 */
		private function done(xy:Pixel):void {
			if (this.dragging) {
				this.panMap(xy);
				this._dragging = false;
			}
		}
		private function panMap(xy:Pixel):void {
			this._dragging = true;
			var oldCenter:Location = this.map.center;
			var deltaX:Number = this._start.x - xy.x;
			var deltaY:Number = this._start.y - xy.y;
			var newPosition:Location = new Location(this._startCenter.lon + deltaX * this.map.resolution,
				this._startCenter.lat - deltaY * this.map.resolution,
				this._startCenter.projection);
			// If the new position equals the old center, stop here
			if (newPosition.equals(oldCenter)) {
				Trace.log("DragHandler.panMap INFO: new center = old center, nothing to do");
				return;
			}
			// Try to set the new position as the center of the map
			this.map.center = newPosition;
			// If the new position is invalid (see Map.setCenter for the
			// conditions), the center of the map is always the old one but the
			// bitmap that represents the map is centered to the new position.
			// We have to reset the bitmap position to the right center.
			if (this.map.center.equals(oldCenter)) {
				Trace.log("DragHandler.panMap INFO: invalid new center submitted, the bitmap of the map is reset");
				this.map.moveTo(this.map.center);
			}
		}
		
		
		private function startBox(e:MouseEvent) : void {
			if(1){ //  放大
				trace("startBox...");
				//this.deactiveDrag(); //禁止拖动
				//this.map.addEventListener(MouseEvent.MOUSE_MOVE,expandArea);
				_drawContainer.graphics.beginFill(_fillColor,0.5);
				_drawContainer.graphics.drawRect(map.mouseX,map.mouseY,1,1);
				_drawContainer.graphics.endFill();
				this._startCoordinates = this.map.getLocationFromMapPx(new Pixel(map.mouseX, map.mouseY));
				//_ctrlpressed = true;
			}
		}
		
		private function endBox(e:MouseEvent) : void {
			//_ctrlpressed = false;
			//if(_opkeys == 0) return;
			//if(this._startCoordinates == null){
			//	return;
			//}
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
					var bound:Bounds = new Bounds(Math.min(_startCoordinates.lon,endCoordinates.lon),
						Math.min(endCoordinates.lat,_startCoordinates.lat),
						Math.max(_startCoordinates.lon,endCoordinates.lon),
						Math.max(endCoordinates.lat,_startCoordinates.lat),
						endCoordinates.projection);
					if( e.ctrlKey){ //zoomin
						this.map.zoomToExtent(bound);
					}else if(e.altKey ){ // zoomout
						var r:Number = this.map.extent.width / bound.width; //比例
						r*= map.resolution; // 增加显示精度(缩小)
						var zoom:Number;
						zoom = map.getZoomForResolution(r);
						var loc:Location = new Location(   _startCoordinates.lon + (endCoordinates.lon - _startCoordinates.lon)/2.0,
																		_startCoordinates.lat +(endCoordinates.lat - _startCoordinates.lat)/2.0 );
						map.moveTo( loc,zoom);
					}
					
				}
			}
			this._startCoordinates = null;
			//this.active = false;
			//activeDrag();
			//this.map.dispatchEvent(new ZoomBoxEvent(ZoomBoxEvent.END));
			//_opkeys = 0;
		}
		
		// onMouseMove
		private function expandArea(e:MouseEvent) : void {
			if(this._startCoordinates == null){
				return;
			}
			if(  1 ){				
				var ll:Pixel = map.getMapPxFromLocation(_startCoordinates);
				_drawContainer.graphics.clear();
				_drawContainer.graphics.lineStyle(1,_fillColor);
				_drawContainer.graphics.beginFill(_fillColor,0.25);
				_drawContainer.graphics.drawRect(ll.x,ll.y,map.mouseX - ll.x,map.mouseY - ll.y);
				_drawContainer.graphics.endFill();
				trace(ll.x,ll.y,map.mouseX - ll.x,map.mouseY - ll.y);
			}
		}
		////
		
	}
}