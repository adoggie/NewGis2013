package com.sw2us.newgis
{
	public class AppUser
	{
		public function AppUser()
		{
		}
		
		public var id:uint = 0;
		public var user:String ;
		public var passwd:String;
		public var name:String;
		public var d:Object = null; //用户信息
		public var behavior:Object = new Object(); //用户操作行为，记录当前状态
		public var params:Object = null;
		public var token:String = "";
	}
}