package newgis{

	import tcelib.RpcConsts;
	import tcelib.RpcConnection;
	import tcelib.utils.HashMap;
	import flash.utils.ByteArray;
	import flash.utils.Endian;
	import tcelib.utils.HashMapEntry;
	
	
	public class ImageDataList_thlp{
		//# -- SEQUENCE --
		
		public var ds:Array = null;
		public function ImageDataList_thlp(ds:Array){
			this.ds = ds
		}		
		
		public function marshall(d:ByteArray):void{
			d.writeInt(this.ds.length);
			for(var n:uint=0; n< this.ds.length;n++){
				{				
					var _c:ImageData_thlp = new ImageData_thlp(this.ds[n]);
					_c.marshall(d);
				}				
			}			
		}		
		
		public function unmarshall(d:ByteArray):Boolean{
			var r:Boolean = false;
			try{
				var _size:uint = 0;
				_size = d.readUnsignedInt();
				for(var _p:uint=0;_p < _size;_p++){
					{					
						var _o:Array = new Array();
						var container:ImageData_thlp = new ImageData_thlp(_o);
						r = container.unmarshall(d);
						if(!r) return false;
						this.ds.push(_o);
					}					
				}				
			}catch(e:Error){
				return false;
			}			
			return true;
		}		
		
	}	
	

}