package newgis{

	import tcelib.RpcConsts;
	import tcelib.RpcConnection;
	import tcelib.utils.HashMap;
	import flash.utils.ByteArray;
	import flash.utils.Endian;
	import tcelib.utils.HashMapEntry;
	
	
	public class AuthToken_t{
	// -- STRUCT -- 
		public var user_id:String = "";
		public var user_name:String = "";
		public var user_realname:String = "";
		public var login_time:int = 0;
		public var login_type:int = 0;
		public var expire_time:int = 0;
		public var rights:String = "";
		public var user_type:int = 0;
		
		//构造函数
		public function AuthToken_t(){
			
		}		
		
		public function marshall(d:ByteArray):void{
			var bytes_12:ByteArray = new ByteArray();
			bytes_12.writeUTFBytes(this.user_id);
			d.writeInt(bytes_12.length);
			d.writeBytes(bytes_12);
			var bytes_13:ByteArray = new ByteArray();
			bytes_13.writeUTFBytes(this.user_name);
			d.writeInt(bytes_13.length);
			d.writeBytes(bytes_13);
			var bytes_14:ByteArray = new ByteArray();
			bytes_14.writeUTFBytes(this.user_realname);
			d.writeInt(bytes_14.length);
			d.writeBytes(bytes_14);
			d.writeInt(this.login_time);
			d.writeInt(this.login_type);
			d.writeInt(this.expire_time);
			var bytes_15:ByteArray = new ByteArray();
			bytes_15.writeUTFBytes(this.rights);
			d.writeInt(bytes_15.length);
			d.writeBytes(bytes_15);
			d.writeInt(this.user_type);
		}		
		
		//反序列化 unmarshall()
		public function unmarshall(d:ByteArray):Boolean{
			try{
				var r:Boolean = false;
				{				
					var _d:uint = 0;
					_d = d.readUnsignedInt();
					this.user_id = d.readUTFBytes(_d);
				}				
				{				
					var _d:uint = 0;
					_d = d.readUnsignedInt();
					this.user_name = d.readUTFBytes(_d);
				}				
				{				
					var _d:uint = 0;
					_d = d.readUnsignedInt();
					this.user_realname = d.readUTFBytes(_d);
				}				
				this.login_time = d.readInt();
				this.login_type = d.readInt();
				this.expire_time = d.readInt();
				{				
					var _d:uint = 0;
					_d = d.readUnsignedInt();
					this.rights = d.readUTFBytes(_d);
				}				
				this.user_type = d.readInt();
			}catch(e:Error){
				return false;
			}
			return true;
		}		
		 // --  end function -- 
		
	}	

}