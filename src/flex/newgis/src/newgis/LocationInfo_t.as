package newgis{

	import tcelib.RpcConsts;
	import tcelib.RpcConnection;
	import tcelib.utils.HashMap;
	import flash.utils.ByteArray;
	import flash.utils.Endian;
	import tcelib.utils.HashMapEntry;
	
	
	public class LocationInfo_t{
	// -- STRUCT -- 
		public var gps:GpsData_t = new GpsData_t();
		public var desc:String = "";
		
		//构造函数
		public function LocationInfo_t(){
			
		}		
		
		public function marshall(d:ByteArray):void{
			{			
				this.gps.marshall(d);
			}			
			var bytes_8:ByteArray = new ByteArray();
			bytes_8.writeUTFBytes(this.desc);
			d.writeInt(bytes_8.length);
			d.writeBytes(bytes_8);
		}		
		
		//反序列化 unmarshall()
		public function unmarshall(d:ByteArray):Boolean{
			try{
				var r:Boolean = false;
				r = this.gps.unmarshall(d)
				if(!r){return false;}
				{				
					var _d:uint = 0;
					_d = d.readUnsignedInt();
					this.desc = d.readUTFBytes(_d);
				}				
			}catch(e:Error){
				return false;
			}
			return true;
		}		
		 // --  end function -- 
		
	}	

}