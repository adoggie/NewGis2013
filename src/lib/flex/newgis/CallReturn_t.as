package newgis{

	import tcelib.RpcConsts;
	import tcelib.RpcConnection;
	import tcelib.utils.HashMap;
	import flash.utils.ByteArray;
	import flash.utils.Endian;
	import tcelib.utils.HashMapEntry;
	
	
	public class CallReturn_t{
	// -- STRUCT -- 
		public var error:Error_t = new Error_t();
		public var value:String = "";
		
		//构造函数
		public function CallReturn_t(){
			
		}		
		
		public function marshall(d:ByteArray):void{
			{			
				this.error.marshall(d);
			}			
			var bytes_17:ByteArray = new ByteArray();
			bytes_17.writeUTFBytes(this.value);
			d.writeInt(bytes_17.length);
			d.writeBytes(bytes_17);
		}		
		
		//反序列化 unmarshall()
		public function unmarshall(d:ByteArray):Boolean{
			try{
				var r:Boolean = false;
				r = this.error.unmarshall(d)
				if(!r){return false;}
				{				
					var _d:uint = 0;
					_d = d.readUnsignedInt();
					this.value = d.readUTFBytes(_d);
				}				
			}catch(e:Error){
				return false;
			}
			return true;
		}		
		 // --  end function -- 
		
	}	

}