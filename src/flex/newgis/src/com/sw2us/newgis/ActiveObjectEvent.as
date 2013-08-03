package com.sw2us.newgis
{
	import flash.events.Event;

	public class ActiveObjectEvent extends Event
	{
		public function ActiveObjectEvent(ev:String)
		{
			super(ev);
			event = ev;	
		}
		public var event:String;
		public var data:ActiveObjectData;
		
		public static const AO_DATA:String = "aoData";
	}
}