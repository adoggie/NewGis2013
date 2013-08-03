/**
 *  MapAolayer - 活动对象层
 * 
 * 
 * 
 * 
 * */

package com.sw2us.newgis.map
{
	import com.mapabc.maps.api.MFlexMap;
	import com.mapabc.maps.api.core._ai1318;
	
	import org.openscales.core.Map;
	import org.openscales.core.feature.Feature;
	import org.openscales.core.layer.FeatureLayer;
	
	
	
	//public class MapAoLayer extends FeatureLayer
	public class MapAoLayer 
	{		
		private var _aoCenter:MapAo = null ; 	//图随ao移动 ，当前ao
		private var _aoFocus:MapAo = null;	//选择焦点ao
		
		private var _map:MapControl = null;
		
		private var _maos:Array = new Array();
		
		public function get map():MapControl{
			return _map;	
		}
		
		public function MapAoLayer(map:MapControl){
			//super("aoLayer");
			this._map = map;
		}
		
		/*
		public override function addFeature(feature:Feature,dispatchFeatureEvent:Boolean=true,reproject:Boolean=true):void{
			super.addFeature(feature,dispatchFeatureEvent,reproject);	
			
		}*/
		
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
		
		/*
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
		*/
		
		public function addMapAo(mao:MapAo):void{
			_maos.push(mao);
		}
		
		public function getMapAoById(aoid:int):MapAo{						
			var n:int;
			for(n=0;n<_maos.length;n++){
				if( _maos[n].getActiveObject().getId() == aoid){
					return _maos[n];
				}
			}	
			return null;
		}
		
		
		/*
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
				 
			}	
			return null;
		}
		
		*/
		
	}

	
}