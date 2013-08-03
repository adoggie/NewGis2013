/**
 *  MapAolayer - 活动对象层
 * 
 * 
 * 
 * 
 * */

package com.sw2us.newgis.map
{
	import org.openscales.core.Map;
	import org.openscales.core.feature.Feature;
	import org.openscales.core.layer.FeatureLayer;
	
	public class MapAoLayer extends FeatureLayer
	{		
		private var _aoCenter:MapAo = null ; 	//图随ao移动 ，当前ao
		private var _aoFocus:MapAo = null;	//选择焦点ao
		
		public function MapAoLayer(map:Map){
			super("aoLayer");
			this.map = map;
		}
		
		public override function addFeature(feature:Feature,dispatchFeatureEvent:Boolean=true,reproject:Boolean=true):void{
			super.addFeature(feature,dispatchFeatureEvent,reproject);	
			
		}
		
		public function setCurrentCenterAo(ao:MapAo):void{			
			_aoCenter = ao;			
		}
		
		public function getCurrentCenterAo():MapAo{
			return _aoCenter;
		}
		
		//当前聚焦ao对象
		public function setFocusAo(ao:MapAo):void{
			_aoFocus = ao;
		}
		
		public function getFocusAo():MapAo{
			return _aoFocus;
		}
		
		public function clearFocusAo():void{							
				var features:Vector.<Feature> = this.features;
				var n:int;
				for(n=0;n<features.length;n++){
					var m:MapAoMarker = features[n] as MapAoMarker;
					if(m){
						m.drawFocused = false;
					}
				}				
				setFocusAo(null);				
		}
		
		//根据ao编号查询地图feature
		public function getMapAoById(aoid:int):MapAo{						
			var features:Vector.<Feature> = this.features;
			var n:int;
			for(n=0;n<features.length;n++){
				var m:MapAoMarker = features[n] as MapAoMarker;
				if(m==null){
					continue;
				}
				if( m.getMapAo().getActiveObject().getId() == aoid){
					return m.getMapAo();
				}
				/*
				if(m.get){
					return m.getMapAo();
				}*/
			}	
			return null;
		}
		
		
		
	}

	
}