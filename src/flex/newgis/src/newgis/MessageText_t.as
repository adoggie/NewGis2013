package newgis{

	import tcelib.RpcConsts;
	import tcelib.RpcConnection;
	import tcelib.utils.HashMap;
	import flash.utils.ByteArray;
	import flash.utils.Endian;
	import tcelib.utils.HashMapEntry;
	
	
	public class MessageText_t{
	// -- STRUCT -- 
		public var type:int = 0;
		public var content:String = "";
		
		//构造函数
		public function MessageText_t(){
			
		}		
		
		public function marshall(d:ByteArray):void{
			d.writeInt(this.type);
			var bytes_11:ByteArray = new ByteArray();
			bytes_11.writeUTFBytes(this.content);
			d.writeInt(bytes_11.length);
			d.writeBytes(bytes_11);
		}		
		
		//反序列化 unmarshall()
		public function unmarshall(d:ByteArray):Boolean{
			try{
				var r:Boolean = false;
				this.type = d.readInt();
				{				
					var _d:uint = 0;
					_d = d.readUnsignedInt();
					this.content = d.readUTFBytes(_d);
				}				
			}catch(e:Error){
				return false;
			}
			return true;
		}		
		 // --  end function -- 
		
	}	

}