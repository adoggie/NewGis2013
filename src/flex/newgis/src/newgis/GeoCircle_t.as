package newgis{

	import tcelib.RpcConsts;
	import tcelib.RpcConnection;
	import tcelib.utils.HashMap;
	import flash.utils.ByteArray;
	import flash.utils.Endian;
	import tcelib.utils.HashMapEntry;
	
	
	public class GeoCircle_t{
	// -- STRUCT -- 
		public var center:GeoPoint_t = new GeoPoint_t();
		public var radius:Number = 0.0;
		
		//构造函数
		public function GeoCircle_t(){
			
		}		
		
		public function marshall(d:ByteArray):void{
			{			
				this.center.marshall(d);
			}			
			d.writeFloat(this.radius);
		}		
		
		//反序列化 unmarshall()
		public function unmarshall(d:ByteArray):Boolean{
			try{
				var r:Boolean = false;
				r = this.center.unmarshall(d)
				if(!r){return false;}
				this.radius = d.readFloat();
			}catch(e:Error){
				return false;
			}
			return true;
		}		
		 // --  end function -- 
		
	}	

}