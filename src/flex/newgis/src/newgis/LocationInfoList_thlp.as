package newgis{

	import tcelib.RpcConsts;
	import tcelib.RpcConnection;
	import tcelib.utils.HashMap;
	import flash.utils.ByteArray;
	import flash.utils.Endian;
	import tcelib.utils.HashMapEntry;
	
	
	public class LocationInfoList_thlp{
		//# -- SEQUENCE --
		
		public var ds:Array = null;
		public function LocationInfoList_thlp(ds:Array){
			this.ds = ds
		}		
		
		public function marshall(d:ByteArray):void{
			d.writeInt(this.ds.length);
			for(var n:uint=0; n< this.ds.length;n++){
				this.ds[n].marshall(d);
			}			
		}		
		
		public function unmarshall(d:ByteArray):Boolean{
			var r:Boolean = false;
			try{
				var _size:uint = 0;
				_size = d.readUnsignedInt();
				for(var _p:uint=0;_p < _size;_p++){
					{					
						var _o:LocationInfo_t = new LocationInfo_t();
						r= _o.unmarshall(d);
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