package com.sw2us.newgis
{
	[Event(name="channelOpened",type="ActiveObjectChannelEvent")]
	[Event(name="channelClosed",type="ActiveObjectChannelEvent")]
	[Event(name="channelData",type="ActiveObjectChannelEvent")]
	
	
	import com.adobe.utils.*;
//	import com.adobe.serialization.json.JSON;
	
	import flash.events.*;
	import flash.net.Socket;
	import flash.utils.ByteArray;
	import flash.utils.Endian;
	import flash.utils.Timer;
	
	
	
	
	public class ActiveObjectChannel extends EventDispatcher
	{
		
		private var _host:String=null;
		private var _port:int=0;
		private var _sock:Socket;
		
		private var _timer:Timer;
		private var _aoids:Array=null;
		private var _aoset:AoCollector;
		
		public function ActiveObjectChannel(aoset:AoCollector,host:String="",port:int=0,delay:int=5*1000)
		{
			_sock = new Socket();
			_sock.addEventListener(Event.CLOSE,onclosed);
			_sock.addEventListener(Event.CONNECT,onconnected);
			_sock.addEventListener(IOErrorEvent.IO_ERROR,onerror);
			_sock.addEventListener(SecurityErrorEvent.SECURITY_ERROR,onerror);
			_sock.addEventListener(ProgressEvent.SOCKET_DATA,ondata);
			_timer = new Timer(delay);
			_timer.addEventListener(TimerEvent.TIMER,ontimer);
			
			_sock.endian = Endian.BIG_ENDIAN;
			_buf.endian = Endian.BIG_ENDIAN;
			
			_aoset = aoset;
		}
		
		
		private function ontimer(e:TimerEvent):void{
			if( _sock.connected){
				return ;
			}
			if(_port ==0){
				return;
			}
			_sock.connect(_host,_port);
		}
		
		private var _packsize:uint = 0;
		private var _buf:ByteArray = new ByteArray();
		//解析ao数据，船钓aoDataCollector
		private function ondata(e:ProgressEvent):void{
			//var b:ByteArray ;
			while(_sock.bytesAvailable >= _packsize){
				if( _packsize == 0){
					if( _sock.bytesAvailable < 4){
						break;  // too short not enough for headsize
					}
					_packsize = _sock.readUnsignedInt();					
				}
				if(_sock.bytesAvailable < _packsize){
					break; // less than one packet size					
				}
				var s:String ; //= b.readUTFBytes(_packsize);
				//2012.3.26 5:03  数据传输改为压缩
				var bytes:ByteArray = new ByteArray();
				//	s = _sock.readUTFBytes(_packsize);
				_sock.readBytes(bytes);
				bytes.uncompress();
				s = bytes.readUTFBytes(bytes.length);				
				_packsize = 0;
				decodeMsg(s);
				//b.uncompress();  //先不采用压缩的方式，直接json过来	
			}				
		}
		
		private function decodeMsg(msg:String):void{
//			var obj:Object;			
//			obj = com.adobe.serialization.json.JSON.decode(msg);
//			
//			//AoCollector.instance().pushData(obj);
//			_aoset.pushData(obj);
		}
		
		private function onerror(e:Event):void{
			trace(e.toString());
		}
		
		private function onclosed(e:Event):void{
			dispatchEvent( new ActiveObjectChannelEvent(
				ActiveObjectChannelEvent.CHANNEL_CLOSED,this));
		}
		
		//socket connected dgw succ！
		//连接上dgw之后重新发送aoids列表
		private function onconnected(e:Event):void{
			//发送链接头标志
			/*
			_sock.writeUTFBytes("SW2US");
			var aoids:Array;
			aoids = ArrayUtil.copyArray(_aoids);
			this.openActiveObjects(aoids);
			*/
			this.dispatchEvent( new ActiveObjectChannelEvent(ActiveObjectChannelEvent.CHANNEL_OPENED,this));
			//_sock.flush();
			trace("socket with dgw has connected!");
		}		
		//发送消息到dgw
		public function sendMessage(obj:Object):Boolean{
//			var s:String=null;
//			s = JSON.encode(obj);
//			try{
//				var bytes:ByteArray = new ByteArray();
//				bytes.writeUTFBytes(s);
//				bytes.compress();
//				//数据进行压缩
//				_sock.writeUnsignedInt(bytes.length); //需要携带长度 				
//				_sock.writeBytes(bytes);
//				_sock.flush();
//				trace("sendMessage:",s);
//			}catch(e:Error){
//				trace("sendMessage exception occurred!");
//			}
			return true;
		}
		
		private function reset():void{
			
		}
				
		//打开dgw的通信通道
		public function open(host:String="",port:int=0):Boolean{
			if(host!=""){
				_host = host;
				_port = port;
			}
			_timer.start();
			return true;
		}
		
		public function close():void{
			
			_timer.stop();
		}
		
		public function openActiveObjects(aoids:Array):Boolean{
			var s:String;
//			if(_aoids ==null){
//				_aoids = aoids;
//			}else{ //添加
//				for(var n:int=0;n<aoids.length;n++){
//					if(!ArrayUtil.arrayContainsValue(_aoids,aoids[n])){
//						_aoids.push(aoids[n]);
//					}
//				}
//			}
//			if(aoids.length == 0){
//				return true ;
//			}
//			if(_sock.connected ==false){
//				return false;
//			}
//			var obj:Object = new Object();
//			obj.msg= "OpenActiveObject";
//			obj.aoids= aoids;
//			this.sendMessage(obj);
//			
//			s = JSON.encode(obj);
//			_sock.writeUnsignedInt(s.length);
//			_sock.writeUTFBytes(s);
//			_sock.flush();
			return true;
		}
		
		public function closeActiveObjects(aoids:Array):void{
			var s:String;
//			if(_aoids ==null){
//				return;
//			}else{
//				for(var n:int=0;n<aoids.length;n++){
//					ArrayUtil.removeValueFromArray(_aoids,aoids[n]);
//				}
//			}
//			if(_sock.connected ==false){
//				return;
//			}
//			var obj:Object = new Object();
//			obj.mid= "CloseActiveObject";
//			obj.aoids= aoids;
//			s = JSON.encode(obj);
//			_sock.writeUnsignedInt(s.length);
//			_sock.writeUTFBytes(s);
//			_sock.flush();
		}
		
		
	}
}