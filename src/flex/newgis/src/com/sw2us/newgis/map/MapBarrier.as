package com.sw2us.newgis.map
{
	import flash.display.Sprite;
	import flash.geom.Point;
	import flash.geom.Rectangle;
	import flash.text.TextField;
	import flash.text.TextFormat;
	import flash.text.TextFormatAlign;
	
	import org.openscales.core.StringUtils;
	import org.openscales.core.basetypes.maps.HashMap;
	import org.openscales.core.events.MapEvent;
	import org.openscales.core.feature.*;
	import org.openscales.core.layer.FeatureLayer;
	import org.openscales.core.layer.Layer;
	import org.openscales.core.style.*;
	import org.openscales.core.style.fill.Fill;
	import org.openscales.core.style.fill.SolidFill;
	import org.openscales.core.style.stroke.*;
	import org.openscales.core.style.symbolizer.*;
	import org.openscales.geometry.*;
	import org.openscales.geometry.basetypes.Bounds;
	import org.openscales.geometry.basetypes.Location;
	import org.openscales.geometry.basetypes.Pixel;
	
	public class MapBarrier extends PolygonFeature
	{
		private var _layer:FeatureLayer;
		private var _bnd:Bounds = null;
		
		public function MapBarrier(layer:FeatureLayer)
		{
			super( new Polygon( new Vector.<Geometry>()),null,this.getDefaultStyle());
			layer.addFeature(this);
			_layer = layer;	
		}
		
		//设置焦点选择中
		public function setFocus(f:Boolean):void{
			if(f){
				var rule:Rule = new Rule();			
				var stroke:Stroke = new Stroke(0xff0000, 1,0.5);
				var fill:Fill = new SolidFill(0xff0000,0.5);			
				var style:Style = new Style();
				
				rule.symbolizers.push(new PolygonSymbolizer(fill,stroke));			
				style.name = "Barrier Styles";
				style.rules.push(rule);
				this.style = style;
			}else{
				this.style = this.getDefaultStyle();
			}
			draw();			
		}
		
		public   function getGeoRect():Bounds{
			return _bnd;
		}
		
		public function setRect(rc:Bounds):void{
			var ring:LinearRing ;
			var pts:Vector.<Number> = new Vector.<Number>();
			_bnd = rc;
			
			//var hullf:Feature = new PolygonFeature(new Polygon(hullLinearRing),null,style);

			
			pts.push(
					rc.left,rc.top,
					rc.left,rc.bottom,
					rc.right,rc.bottom,
					rc.right,rc.top,
					rc.left,rc.top);
			
			ring = new LinearRing(pts);
			var rings:Vector.<Geometry> = new Vector.<Geometry>();
			rings.push(ring);
			
			
			this.geometry = new Polygon(rings);
			setFocus(false);
			
			this.draw();
		}
		
		private  function getDefaultStyle():Style {	
			//return Style.getDefaultSurfaceStyle();
			
			var rule:Rule = new Rule();			
			var stroke:Stroke = new Stroke(0xff0000, 1,0.5);
			var fill:Fill = new SolidFill(0xffff00,0.5);			
			var style:Style = new Style(); // Style.getDefaultSurfaceStyle();
			
			rule.symbolizers.push(new PolygonSymbolizer(fill,stroke));			
			style.name = "Barrier Styles";
			style.rules.push(rule);
			return style;
		}
	}
}