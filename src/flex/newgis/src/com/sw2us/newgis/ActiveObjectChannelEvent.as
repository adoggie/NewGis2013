package com.sw2us.newgis
{
	import flash.events.Event;
	public class ActiveObjectChannelEvent extends Event
	{
		public function ActiveObjectChannelEvent(evt:String,channel:ActiveObjectChannel)
		{
			super(evt);						
			this.channel = channel;
			
		}	
		public var data:Object;
		public var channel:ActiveObjectChannel;		
		public static const CHANNEL_OPENED:String ="channelOpened";
		public static const CHANNEL_CLOSED:String ="channelClosed";
		public static const CHANNEL_DATA:String ="channelData";
		
	}
}