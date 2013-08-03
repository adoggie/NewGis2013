package com.sw2us.newgis.maptools
{
	import flash.display.Sprite;
	
	import mx.events.ResizeEvent;
	
	import org.openscales.core.Map;
	
	import spark.primitives.Line;
	
	public class MapCenterCross extends Sprite
	{
		var vline:Line;
		var hline:Line;
		public function MapCenterCross(map:Map,width:int=40,height:int=40)
		{
			map.addEventListener(ResizeEvent.RESIZE,onMapResize(event) );
			this.width = width;
			this.height = height;
			vline = new Line();
			vline.xFrom = 0;
			vline.xTo = width;
			hline = new Line();
			hline.xFrom = width/2;
			//hline.
		}
		public function onMapResize(event:ResizeEvent):void{
				
		}
	}
}