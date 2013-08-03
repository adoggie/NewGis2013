

/*
 javascript 领悟:
 如果function()视为一个class，里面用this.定义了成员变量
 也定义了成员函数this.func(),在这个对象的外部调用这个class实例的func()方法，则
 在这个方法内可以通过this.来引用这个类的成员变量。
 但问题出来了：如果将这个class.func()作为一个函数赋予其他类作为回调或事件处理函数的
 话，那在这个函数里面的this是指的调用者对象，而并不是原先的class，这大概就是所谓的
 javascript的闭包机制。

var animal = new Animal();
function Animal(){
	this.name='abc';
	this.move = function(xy){}  //在这个move函数内如果是闭包传递到Dog类去了，那this就指向Dog了，所以不能访问Animal的变量了
	this.create = function(){
		dog = new Dog(name,this.move); //这里this.move是个错误,Dog的第二个参数是个
							function,这个function必须是全局的或者指定某个对象的函数，
		dog = new  Dog(name,animal.move);//这样是正确的，也就是闭包了，Dog类将复制这个functi到Dog内部
										所以闭包更消耗内存
	}
}
 
*/
var g_aoMarkerMgr = null; //标记管理 

 
function aoMarkerMgr(map){
	this.map = map;
	this.aos = new Array();
	this.popupDetail = null;
	this.markers = new OpenLayers.Layer.Markers( "aoMarkers" );
	map.addLayer(this.markers);
	
  var size = new OpenLayers.Size(24,24);
  var offset = new OpenLayers.Pixel(-(size.w/2), -size.h);
  this.icon_ao= new OpenLayers.Icon('/medias/images/4-katoo-car-02.png',size,offset);
	this.icon_aofocus= new OpenLayers.Icon('/medies/images/4-katoo-car-02.png',size,offset);
	
	/*popup窗口显示ao对象细节*/
	
	
	this.onClosePopup = function(){
		if(g_aoMarkerMgr.popupDetail){
			try{
				//g_aoMarkerMgr.popupDetail.toggle();
				g_aoMarkerMgr.map.removePopup(g_aoMarkerMgr.popupDetail);
				g_aoMarkerMgr.popupDetail.destroy();
			}catch(e){
				alert(e.toString());
			}
			g_aoMarkerMgr.popupDetail = null;
			//alert(g_aoMarkerMgr.popupDetail);
		}
	};
	this.onMouseLeft = function(e){
		g_aoMarkerMgr.onClosePopup(e);
		//OpenLayers.Event.stop(e);
	};
	
	this.onMouseMove = function(e){
		//alert(g_aoMarkerMgr.popupDetail);
		if(g_aoMarkerMgr.popupDetail){
			return ;
		}
		var html ="<div style='background-color:red; width:150;height:100'>aoid</div>";
		//alert(e.object.ao.aoid);
		//alert( gDataMgr.getAoProfile(e.object.ao.aoid));
		html = e.object.ao.name + "<br>";
		html += gDataMgr.getAoProfile(e.object.ao.aoid);
		g_aoMarkerMgr.popupDetail = new OpenLayers.Popup("aopop",
                   e.object.lonlat.clone(),
									 //new OpenLayers.LonLat(5,40),
                   new OpenLayers.Size(260,160),
                   html);//,
                   //true,g_aoMarkerMgr.onClosePopup);
		//alert(g_aoMarkerMgr.popupDetail);
		
		//g_aoMarkerMgr.popupDetail.closeOnMove = true;
		g_aoMarkerMgr.popupDetail.setBackgroundColor("blue");
		g_aoMarkerMgr.popupDetail.setOpacity(0.7);
		e.object.map.addPopup(g_aoMarkerMgr.popupDetail);
		//OpenLayers.Event.stop(e);
	};
	this.createActiveObject = function(aoid,name){
		try{
			var marker = new OpenLayers.Marker(new OpenLayers.LonLat(0,0),this.icon_ao);		
			marker.ao = {'aoid':aoid,'name':name};
			this.aos.push(marker);
			marker.events.register('mouseover',marker,this.onMouseMove);
			marker.events.register('mouseout',marker,this.onMouseLeft);
		}catch(e){
			//alert(e.toString());
		}
	};
	
	/* 2010.12.14 IE6下 注释使用//将导致不可控的异常
	//移动ao对象
	
	BROWSER_EVENTS: [
        "mouseover", "mouseout",
        "mousedown", "mouseup", "mousemove", 
        "click", "dblclick", "rightclick", "dblrightclick",
        "resize", "focus", "blur"
    ],
    
		*/	
	this.aoMoveTo = function(aoid,lon,lat){
	
		try{
			for(var n=0;n<this.markers.markers.length;n++){
				var mkr = this.markers.markers[n];
				if(mkr.ao.aoid == aoid){					
					mkr.lonlat = new OpenLayers.LonLat(lon,lat);					
					this.markers.drawMarker(mkr);
					break;
				}
			}
		}catch(e){
			alert(e.toString());
		}
														
	};
		 
		 
	this.clear = function(){
		this.markers.clearMarkers();
		this.aos = new Array()
	};
	
	this.hide = function(){
		for(var n=0;n<this.markers.markers.length;n++){
			this.aos.push(this.markers.markers[n]);
		}
		this.markers.clearMarkers();
		
	};
	
	this.show = function(){
		for (var n=0;n<this.aos.length;n++){
			this.markers.addMarker(this.aos[n]);
		}
		this.aos = new Array();		
	};
												
}

function init_MapMarkers(map){
	try{		
		g_aoMarkerMgr = new aoMarkerMgr(map);
	}catch(e){
		alert(e);
	}
	
}

