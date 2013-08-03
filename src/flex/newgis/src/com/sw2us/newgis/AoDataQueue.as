package com.sw2us.newgis
{
	import com.adobe.utils.DictionaryUtil;
	
	import flash.utils.Dictionary;
	
	import mx.utils.ArrayUtil;
	
	import newgis.GpsData_t;
	
	public class AoDataQueue
	{
		// cachesize - 模块设备队列数据缓冲长度
		public function AoDataQueue(cachesize:int=1024,policy:int =CachedPolicy_Size )
		{
			_cachesize = cachesize;
			_cachedtime = 3600*1; //默认1个小时
			_modules[ActiveObjectData.GPS]=new Array();
			_modules[ActiveObjectData.IMAGE]=new Array();
		}
		private var _cachesize:int;
		private var _cachedtime:int;	//缓冲时长 (sencond)
		private var _modules:Dictionary = new Dictionary(); 		//根据设备模块类型存储数据
		private var _cachedpolicy:int = CachedPolicy_Size; 	//存储策略 ，时间还是数据量
		
		
		public static const CachedPolicy_Size:int = 1;
		public static const CachedPolicy_Time:int = 2; //根据时间
		public static const CachedPolicy_Unlimited:int = 0 ;// 无限制 
		
		private var _lastpos:int =0;	//最近一次访问数据下标
		
		public function setCachedPolicy(policy:int):void{
			_cachedpolicy = policy;			
		}
		
		public function setCachedSize(size:int):void{
			_cachesize = size;
		}
		
		//缓冲数据时长
		public function setCachedTime(seconds:int):void{
			_cachedtime = seconds;
		}
		
		public function pushData(module:int,data:GpsData_t):void{
			//var x:ArrayUtil;
			var keys:Array = DictionaryUtil.getKeys(_modules);
			if( ArrayUtil.getItemIndex(module,keys) ==-1){
				_modules[module]=new Array();	//模块数据是个队列			
			}
			var ar:Array = _modules[module] as Array;
			if( _cachedpolicy == CachedPolicy_Size){
				if( ar.length >= _cachesize){ //删除头部
					ar.shift();
				}
			}else if( _cachedpolicy == CachedPolicy_Time){
				//无论何种module数据，都必须存在time字段, time - (unix timestamp)
				//last - first <= _cachedtime
				var now:Date = new Date();
				var newar:Array = new Array();
				for(var n:int=ar.length-1;n>=0;n--){//反向找到第一个时间过期的数据，且删除于此之前的数据					
					var d:Object = ar[n];
					//trace(d.time, now.time/1000,now.toString());
					if( now.time/1000 - d.time > _cachedtime){ // as 记录的是million seconds
						//newar.push(ar[n]);
						ar.splice(0,n+1);
						break;
					}
				}
				
			}
			ar.push(data);
		}
		
		//清除指定模块的数据，且保留 keepnum个数据(keepnum-最新鲜的数据)
		public function clearData(module:int,keepnum:int=1):void{
			var ar:Array = _modules[module] as Array;
			//ar =[];
			ar.splice(0);
		}
		
		//删除所有模块数据 
		public function clearAll():void{
			var keys:Array = DictionaryUtil.getKeys(_modules);
			for(var n:int=0;n<keys.length;n++){
				_modules[keys[n]] = new Array();
			}
		}
		
		//最接近tick时间且大于等于tick的模块数据 
		public function getModuleDataByTime(module:int,tick:int):Object{
			var keys:Array = DictionaryUtil.getKeys(_modules);
			if( ArrayUtil.getItemIndex(module,keys) ==-1){
				return null; //module数据类型不存在，便不存在数据
			}
			var dd:Array = _modules[module]  as Array; //模块数据列表
			if( dd.length ==0){
				return null;
			}
			var d:Object;
			var i:int=0;
			/*
			if( this._lastpos >= datalist.length){
				this._lastpos = 0;
			}
			d = datalist[_lastpos];
			
			if( tick >= d.time ){
				start = _lastpos;
			}*/
			for(;i < dd.length;i++){
				d = dd[i];
				//trace(d.time,tick);
				if( d.gpstime >= tick){ //must be  '>'
					//_lastpos = start;
					return d;
				}
			}			
			return null;
		}
		
		// pushDataList 
		// 推入模块数据列表  , 用于显示ao对象gps近一个小时的路径轨迹
		public function pushDataList(module:int,datalist:Array):void{
			var keys:Array = DictionaryUtil.getKeys(_modules);
			if( ArrayUtil.getItemIndex(module,keys) ==-1){
				_modules[module]=new Array();	//模块数据是个队列			
			}
			var ar:Array = _modules[module] as Array;
			for(var n:int=0;n<datalist.length;n++){
				ar.push( datalist[n] );
			}			
		}
		
		//获取最新的一个模块对象数据
		public function getData(module:int):Object{
			var obj:Object = null;
			var keys:Array = DictionaryUtil.getKeys(_modules);
			if( ArrayUtil.getItemIndex(module,keys) ==-1){
				return null;	
			}
			var ar:Array = _modules[module] as Array;
			if(ar.length ==0){
				return null;
			}
			obj = ar[ar.length-1]; //获取最后一个对象数据
			return obj;
		}
		
		public function getDataList(module:int):Array{
			var ar:Array;
			var keys:Array = DictionaryUtil.getKeys(_modules);
			if( ArrayUtil.getItemIndex(module,keys) ==-1){
				ar =new Array();	//模块数据是个队列			
			}else{			
			 	ar = _modules[module] as Array;
			}
			return ar;
		}
		
		
		
	}
}