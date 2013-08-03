package com.sw2us.newgis.event
{
	import com.sw2us.newgis.UserFeaturePoint;
	
	import flash.events.Event;
	
	public class UserFeatureEvent extends Event
	{
		public static var USERFEATURE_CLICK:String = "sw2us.gis.featureclick";
		public var _feature:UserFeaturePoint = null;
		public function UserFeatureEvent(type:String, ftr:UserFeaturePoint, bubbles:Boolean=false, cancelable:Boolean=false)
		{
			
			super(type, bubbles, cancelable);
			_feature = ftr;
		}
	}
}