package newgis{

	import tcelib.RpcConsts;
	import tcelib.RpcConnection;
	import tcelib.utils.HashMap;
	import flash.utils.ByteArray;
	import flash.utils.Endian;
	import tcelib.utils.HashMapEntry;
	
	
	public class GeoSize_t{
	// -- STRUCT -- 
		public var cx:Number = 0.0;
		public var cy:Number = 0.0;
		
		//构造函数
		public function GeoSize_t(){
			
		}		
		
		public function marshall(d:ByteArray):void{
			d.writeFloat(this.cx);
			d.writeFloat(this.cy);
		}		
		
		//反序列化 unmarshall()
		public function unmarshall(d:ByteArray):Boolean{
			try{
				var r:Boolean = false;
				this.cx = d.readFloat();
				this.cy = d.readFloat();
			}catch(e:Error){
				return false;
			}
			return true;
		}		
		 // --  end function -- 
		
	}	

}