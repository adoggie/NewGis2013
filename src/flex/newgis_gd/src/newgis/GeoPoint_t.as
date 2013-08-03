package newgis{

	import tcelib.RpcConsts;
	import tcelib.RpcConnection;
	import tcelib.utils.HashMap;
	import flash.utils.ByteArray;
	import flash.utils.Endian;
	import tcelib.utils.HashMapEntry;
	
	
	public class GeoPoint_t{
	// -- STRUCT -- 
		public var lon:Number = 0.0;
		public var lat:Number = 0.0;
		
		//构造函数
		public function GeoPoint_t(){
			
		}		
		
		public function marshall(d:ByteArray):void{
			d.writeFloat(this.lon);
			d.writeFloat(this.lat);
		}		
		
		//反序列化 unmarshall()
		public function unmarshall(d:ByteArray):Boolean{
			try{
				var r:Boolean = false;
				this.lon = d.readFloat();
				this.lat = d.readFloat();
			}catch(e:Error){
				return false;
			}
			return true;
		}		
		 // --  end function -- 
		
	}	

}