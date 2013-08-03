package newgis{

	import tcelib.RpcConsts;
	import tcelib.RpcConnection;
	import tcelib.utils.HashMap;
	import flash.utils.ByteArray;
	import flash.utils.Endian;
	import tcelib.utils.HashMapEntry;
	
	
	public class TimeRange_t{
	// -- STRUCT -- 
		public var start:int = 0;
		public var end:int = 0;
		
		//构造函数
		public function TimeRange_t(){
			
		}		
		
		public function marshall(d:ByteArray):void{
			d.writeInt(this.start);
			d.writeInt(this.end);
		}		
		
		//反序列化 unmarshall()
		public function unmarshall(d:ByteArray):Boolean{
			try{
				var r:Boolean = false;
				this.start = d.readInt();
				this.end = d.readInt();
			}catch(e:Error){
				return false;
			}
			return true;
		}		
		 // --  end function -- 
		
	}	

}