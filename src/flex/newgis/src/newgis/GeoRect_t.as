package newgis{

	import tcelib.RpcConsts;
	import tcelib.RpcConnection;
	import tcelib.utils.HashMap;
	import flash.utils.ByteArray;
	import flash.utils.Endian;
	import tcelib.utils.HashMapEntry;
	
	
	public class GeoRect_t{
	// -- STRUCT -- 
		public var x:Number = 0.0;
		public var y:Number = 0.0;
		public var width:Number = 0.0;
		public var height:Number = 0.0;
		
		//构造函数
		public function GeoRect_t(){
			
		}		
		
		public function marshall(d:ByteArray):void{
			d.writeFloat(this.x);
			d.writeFloat(this.y);
			d.writeFloat(this.width);
			d.writeFloat(this.height);
		}		
		
		//反序列化 unmarshall()
		public function unmarshall(d:ByteArray):Boolean{
			try{
				var r:Boolean = false;
				this.x = d.readFloat();
				this.y = d.readFloat();
				this.width = d.readFloat();
				this.height = d.readFloat();
			}catch(e:Error){
				return false;
			}
			return true;
		}		
		 // --  end function -- 
		
	}	

}