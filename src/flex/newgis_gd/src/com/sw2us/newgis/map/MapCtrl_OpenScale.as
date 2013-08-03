package com.sw2us.newgis.map
{
	import org.openscales.core.Map;
	import org.openscales.geometry.basetypes.Location;
	
	public class MapCtrl_OpenScale extends MapControl
	{
		private var _map:Map;
		
		public function MapCtrl_OpenScale(map_:Map =null)
		{
			super();
			map = map_;
		}
		
		public override function moveTo(lon:Number,lat:Number,zoom:int=-1):void{
			_map.moveTo( new Location(lon,lat));			
		}
		
		public override function zoomIn():void{
			_map.zoom+=1;
			
		}
		
		public override function zoomOut():void{
			if(_map.zoom == 0){
				return;
			}
			_map.zoom-=1;
		}
		
		public override function zoomTo(z:int):void{
			_map.zoom = z;
		}
		
		public override function get map():Object{
			return _map;
		}
		
		public function set map(map_:Map):void{
			_map = map_;	
		}
		
	}
}