package com.sw2us.newgis.map
{
	import com.mapabc.maps.api.MFlexMap;
	import com.mapabc.maps.api.basetypes.MLngLat;
	
	import flash.geom.Point;
	
	public class MapCtrl_AutoNavi extends MapControl
	{
		
		private var _map:MFlexMap;
		
		public function MapCtrl_AutoNavi(map_:MFlexMap=null)
		{
			super();
			map = map_;
		}
		
		public override function moveTo(lon:Number,lat:Number,zoom:int=-1):void{
			_map.setCenter( new MLngLat(lon,lat));
			zoomTo(zoom);
			
		}
		
		public override function getCenter():Point{
			return new Point(_map.getCenter().lngX,_map.getCenter().latY);
		}
		
		public override function getZoom():int{
			return _map.getZoomLevel(); 
		}
		
		public override function zoomIn():void{
			_map.zoomIn();
		}
		
		public override function zoomOut():void{
			_map.zoomOut();
		}
		
		public override function zoomTo(z:int):void{
			if ( z <=-1){
				return;
			}
			_map.zoom = z;
		}
		
		public override  function getMap():Object{
			return _map;
			//return null;
		}
		
		public function set map(map_:MFlexMap):void{
			_map = map_;	
		}
		
	}
}