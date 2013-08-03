package newgis{

	import tcelib.RpcConsts;
	import tcelib.RpcConnection;
	import tcelib.utils.HashMap;
	import flash.utils.ByteArray;
	import flash.utils.Endian;
	import tcelib.utils.HashMapEntry;
	
	
	public class GpsExtraData_t{
	// -- STRUCT -- 
		public var miles:int = 0;
		public var power:int = 0;
		public var acc:int = 0;
		public var av:int = 0;
		
		//构造函数
		public function GpsExtraData_t(){
			
		}		
		
		public function marshall(d:ByteArray):void{
			d.writeInt(this.miles);
			d.writeInt(this.power);
			d.writeInt(this.acc);
			d.writeInt(this.av);
		}		
		
		//反序列化 unmarshall()
		public function unmarshall(d:ByteArray):Boolean{
			try{
				var r:Boolean = false;
				this.miles = d.readInt();
				this.power = d.readInt();
				this.acc = d.readInt();
				this.av = d.readInt();
			}catch(e:Error){
				return false;
			}
			return true;
		}		
		 // --  end function -- 
		
	}	

}