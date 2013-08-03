package newgis{

	import tcelib.RpcConsts;
	import tcelib.RpcConnection;
	import tcelib.utils.HashMap;
	import flash.utils.ByteArray;
	import flash.utils.Endian;
	import tcelib.utils.HashMapEntry;
	
	
	public class Properties_thlp {
		//# -- THIS IS DICTIONARY! --
		public var ds :HashMap = null;
		
		public function Properties_thlp(ds:HashMap){
			this.ds = ds;
		}		
		
		public function marshall(d:ByteArray):void{
			var _size:uint = 0;
			_size = this.ds.size();
			d.writeUnsignedInt( this.ds.size() );
			var _items:Array;
			var _pair: HashMapEntry;
			_items = this.ds.getEntries();
			for(var _n:int=0; _n < _items.length ; _n++){
				_pair = _items[_n] as HashMapEntry;
				{				
					var k:String = _pair.key as String;
					var bytes_4:ByteArray = new ByteArray();
					bytes_4.writeUTFBytes(k);
					d.writeInt(bytes_4.length);
					d.writeBytes(bytes_4);
				}				
				{				
					var v:String = _pair.value as String;
					var bytes_5:ByteArray = new ByteArray();
					bytes_5.writeUTFBytes(v);
					d.writeInt(bytes_5.length);
					d.writeBytes(bytes_5);
				}				
			}			
		}		
		
		// unmarshall()
		public function unmarshall(d:ByteArray):Boolean{
			var r:Boolean = false;
			try{
				var _size:uint = 0;
				_size = d.readUnsignedInt();
				for(var _p:uint=0;_p < _size;_p++){
					var _k:String = "";
					{					
						var _d:uint = 0;
						_d = d.readUnsignedInt();
						_k = d.readUTFBytes(_d);
					}					
					var _v:String = "";
					{					
						var _d:uint = 0;
						_d = d.readUnsignedInt();
						_v = d.readUTFBytes(_d);
					}					
					this.ds[_k] = _v;
				}				
			
			}catch(e:Error){
				return false;
			}			
			return true;
		}		
	}	
	//-- end Dictonary Class definations --
	

}