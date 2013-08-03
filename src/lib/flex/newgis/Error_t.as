package newgis{

	import tcelib.RpcConsts;
	import tcelib.RpcConnection;
	import tcelib.utils.HashMap;
	import flash.utils.ByteArray;
	import flash.utils.Endian;
	import tcelib.utils.HashMapEntry;
	
	
	public class Error_t{
	// -- STRUCT -- 
		public var succ:Boolean = false;
		public var code:int = 0;
		public var msg:String = "";
		
		//构造函数
		public function Error_t(){
			
		}		
		
		public function marshall(d:ByteArray):void{
			if(this.succ == true){
				d.writeByte(1);
			}else{
				d.writeByte(0);
			}			
			d.writeInt(this.code);
			var bytes_16:ByteArray = new ByteArray();
			bytes_16.writeUTFBytes(this.msg);
			d.writeInt(bytes_16.length);
			d.writeBytes(bytes_16);
		}		
		
		//反序列化 unmarshall()
		public function unmarshall(d:ByteArray):Boolean{
			try{
				var r:Boolean = false;
				{				
					var _d:uint = 0;
					_d = d.readUnsignedByte();
					if(_d == 0){
						this.succ = false;
					}else{
						this.succ = true;
					}					
				}				
				this.code = d.readInt();
				{				
					var _d:uint = 0;
					_d = d.readUnsignedInt();
					this.msg = d.readUTFBytes(_d);
				}				
			}catch(e:Error){
				return false;
			}
			return true;
		}		
		 // --  end function -- 
		
	}	

}