package newgis{

	import tcelib.RpcConsts;
	import tcelib.RpcConnection;
	import tcelib.utils.HashMap;
	import flash.utils.ByteArray;
	import flash.utils.Endian;
	import tcelib.utils.HashMapEntry;
	
	
	public class AlarmInfo_t{
	// -- STRUCT -- 
		public var type:String = "";
		public var params:String = "";
		
		//构造函数
		public function AlarmInfo_t(){
			
		}		
		
		public function marshall(d:ByteArray):void{
			var bytes_9:ByteArray = new ByteArray();
			bytes_9.writeUTFBytes(this.type);
			d.writeInt(bytes_9.length);
			d.writeBytes(bytes_9);
			var bytes_10:ByteArray = new ByteArray();
			bytes_10.writeUTFBytes(this.params);
			d.writeInt(bytes_10.length);
			d.writeBytes(bytes_10);
		}		
		
		//反序列化 unmarshall()
		public function unmarshall(d:ByteArray):Boolean{
			try{
				var r:Boolean = false;
				{				
					var _d:uint = 0;
					_d = d.readUnsignedInt();
					this.type = d.readUTFBytes(_d);
				}				
				{				
					var _d:uint = 0;
					_d = d.readUnsignedInt();
					this.params = d.readUTFBytes(_d);
				}				
			}catch(e:Error){
				return false;
			}
			return true;
		}		
		 // --  end function -- 
		
	}	

}