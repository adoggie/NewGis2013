package com.sw2us.newgis.util
{
	import com.adobe.serialization.json.JSON;
	import com.adobe.utils.*;
	
	import flash.utils.ByteArray;
	
	public class DataSerial
	{
		public function DataSerial()
		{
		}
		
		public static function unjson(d:String):Object{
			var obj:Object;			
			obj = JSON.decode(d);
			return obj;
		}
		
		public static function unjsonzlib(s:String):Object{
			var bytes:ByteArray = new ByteArray();
			bytes.writeUTFBytes(s);
			bytes.uncompress();
			s = bytes.readUTFBytes(bytes.length);
			var obj:Object;			
			obj = JSON.decode(s);
			return obj;
		}
	}
}