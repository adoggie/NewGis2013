package com.sw2us.newgis
{
	/**
	 * UserFeatureLayer
	 * 用户feature的容器管理器,绑定指定地图的featurelayer
	 * 
	 */ 
	import com.sw2us.newgis.event.UserFeatureEvent;
	import com.sw2us.newgis.util.HashMap;
	
	import flash.display.DisplayObject;
	import flash.events.MouseEvent;
	import flash.geom.Rectangle;
	
	import org.openscales.core.Map;
	import org.openscales.core.feature.Feature;
	import org.openscales.core.layer.FeatureLayer;
	import org.openscales.geometry.basetypes.Bounds;
	import org.openscales.geometry.basetypes.Location;

	public class UserFeatureLayer
	{
		private var _layer:FeatureLayer = null;
		private var _points:HashMap = new HashMap();
		
		public function UserFeatureLayer(layer:FeatureLayer)
		{
			_layer = layer;
		}
		
		private function onFeatureClick(evt:UserFeatureEvent):void{
			dispatchEvent( evt); //直接丢到外层用户
		}
		
		private function createFeaturePoint(o:Object):Feature{
			var d:DisplayObject = AppResource.instance().getUserFeatureIconByType(o.type);
			var f:UserFeaturePoint = UserFeaturePoint.create(_layer,d,new Location(o.lon,o.lat),o);
			if( f ){
				f.addEventListener(UserFeatureEvent.USERFEATURE_CLICK,onFeatureClick);
			}
			return f;
		}
		
		public function addFeaturePoint(o:Object):Boolean{
			var ftr:Feature = createFeaturePoint(o);
			_points.put(o.id,ftr);
		}
		
		public function onFeaturesLoad(features:Array):void{
			var n:uint = 0;
			var map:Map = _layer.map;
			
			for(;n<features.length;n++){
				var o:Object = features[n] as Object;
				addFeaturePoint(o);
				//create feature on map
			}
		}
		
		public function onFeaturesDestroy(b:Bounds):void{
			var vals:Array = _points.getValues();
			var n:uint = 0;
			for(;n<vals.length;n++){
				var o:Object = vals[n] as Object;
				if ( b.containsLocation( new Location(o.lon,o.lat)) ){
					if( _points.containsKey(o.id) ){
						var ftr:Feature = _points[o.id];
						_points.remove(o.id);
						_layer.removeFeature(ftr);
						ftr.destroy();
						ftr = null;
					}
					//remove feature on map
				}
			}
		}
		
	}
}