package newgis{

	import tcelib.RpcConsts;
	import tcelib.RpcConnection;
	import tcelib.utils.HashMap;
	import flash.utils.ByteArray;
	import flash.utils.Endian;
	import tcelib.utils.HashMapEntry;
	
	
	public class MessageImage_t{
	// -- STRUCT -- 
		public var type:int = 0;
		public var width:int = 0;
		public var height:int = 0;
		public var data:Array = new Array();
		public var data64:String = "";
		
		//构造函数
		public function MessageImage_t(){
			
		}		
		
		public function marshall(d:ByteArray):void{
			d.writeInt(this.type);
			d.writeInt(this.width);
			d.writeInt(this.height);
			{			
				var container:ImageData_thlp = ImageData_thlp(this.data);
				container.marshall(d);
			}			
			var bytes_7:ByteArray = new ByteArray();
			bytes_7.writeUTFBytes(this.data64);
			d.writeInt(bytes_7.length);
			d.writeBytes(bytes_7);
		}		
		
		//反序列化 unmarshall()
		public function unmarshall(d:ByteArray):Boolean{
			try{
				var r:Boolean = false;
				this.type = d.readInt();
				this.width = d.readInt();
				this.height = d.readInt();
				{				
					var container:ImageData_thlp = new ImageData_thlp(this.data);
					r = container.unmarshall(d);
					if(!r){return false;}
				}				
				{				
					var _d:uint = 0;
					_d = d.readUnsignedInt();
					this.data64 = d.readUTFBytes(_d);
				}				
			}catch(e:Error){
				return false;
			}
			return true;
		}		
		 // --  end function -- 
		
	}	

}