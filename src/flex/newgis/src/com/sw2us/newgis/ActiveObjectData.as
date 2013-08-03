package com.sw2us.newgis
{
	public class ActiveObjectData
	{
		public function ActiveObjectData()
		{
			
		}
		//public var aoid:int;
		public var ao:ActiveObject;
		
		public var type:int = 0;
		public var data:Object = null;
		
		public static const GPS:int = 1<<0;
		public static const AUDIO:int = 1<<1;
		public static const VIDEO:int = 1<<2;
		public static const IMAGE:int = 1<<3;
		public static const TEXT:int = 1<<4;
		public static const IODATA:int = 1<<5;
		public static const ALARM:int = 1<<6;
		
	}
}