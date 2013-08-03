package newgis{

	import tcelib.RpcConsts;
	import tcelib.RpcConnection;
	import tcelib.utils.HashMap;
	import flash.utils.ByteArray;
	import flash.utils.Endian;
	import tcelib.utils.HashMapEntry;
	
	
	public class GpsData_t{
	// -- STRUCT -- 
		public var lon:Number = 0.0;
		public var lat:Number = 0.0;
		public var speed:Number = 0.0;
		public var direction:Number = 0.0;
		public var time:int = 0;
		public var extra:GpsExtraData_t = new GpsExtraData_t();
		
		//构造函数
		public function GpsData_t(){
			
		}		
		
		public function marshall(d:ByteArray):void{
			d.writeFloat(this.lon);
			d.writeFloat(this.lat);
			d.writeFloat(this.speed);
			d.writeFloat(this.direction);
			d.writeInt(this.time);
			{			
				this.extra.marshall(d);
			}			
		}		
		
		//反序列化 unmarshall()
		public function unmarshall(d:ByteArray):Boolean{
			try{
				var r:Boolean = false;
				this.lon = d.readFloat();
				this.lat = d.readFloat();
				this.speed = d.readFloat();
				this.direction = d.readFloat();
				this.time = d.readInt();
				r = this.extra.unmarshall(d)
				if(!r){return false;}
			}catch(e:Error){
				return false;
			}
			return true;
		}		
		 // --  end function -- 
		
	}	

}