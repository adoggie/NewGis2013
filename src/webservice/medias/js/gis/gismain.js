
var gDataMgr;
//数据采集器
function DataManager(){
	/*
	this.store = new Ext.data.JsonStore({ 
			url:"/getGpsData",
			root: 'result',
			fields: ['aoid','time','satenum','sateused','lon','lat','speed','angle']
			});*/
	this.store = null;
	this.gpsData = new Array();
	this.gpscount = 0;
	
	this.getAoProfile = function(aoid){
		var html ="";
		//alert("sdfkj");
		for(var n=0;n<this.gpsData.length ;n++){
			if( aoid == this.gpsData[n].aoid){
				
				var dt = new Date(parseInt(this.gpsData[n].time)*1000);
				html+="时间:" + dt.toLocaleString() +"<br>";
				html+="位置:" + this.gpsData[n].lon+','+this.gpsData[n].lat +"<br>";
				html+="速度:" +  this.gpsData[n].speed +"<br>";
				html+="方向:" + this.gpsData[n].angle +"<br>";
				html+="收星数:" +  this.gpsData[n].sateused + "<br>";
				break;
			}
		}
		return html;
	};
	
	this.loadsucc=function(resp){		
		var r = Ext.util.JSON.decode(resp.responseText);
		
		//		
		if(true){ //返回的是差异数据，所以必须比对更新记录
			for(var n=0;n<r.result.length;n++){
				var find = false;
				//alert(gDataMgr.gpsData.length);
				for(var m=0;m<gDataMgr.gpsData.length;m++){
					
					if(gDataMgr.gpsData[m].aoid == r.result[n].aoid){
						gDataMgr.gpsData[m] = r.result[n];
						find = true;
						break;
					}
				}
				if(!find){
					gDataMgr.gpsData.push(r.result[n]);
				}
			}
			//gps 数据范围显示标记Ao
			//if(gDataMgr.gpscount++ <2){
			for(var n=0;n<r.result.length;n++){
				var lon = parseFloat(r.result[n].lon);
				var lat = parseFloat(r.result[n].lat);
				g_aoMarkerMgr.aoMoveTo(r.result[n].aoid,lon,lat);
			}
			//}
			 
			//----------------
		}
		//////
		//alert(gDataMgr.gpsData.length);
		aoDetailGrid.update(gDataMgr.gpsData); //
		
		//alert(aoDetailGrid.getActiveObject().name);
		//=======================================
		//show activeobject on map
		
	}

	this.loadfail=function(resp){
		//alert('GpsLoading(): ajax failed!');
	}

	this.task = {
    run: function(){
					//[[aoid,lasttime],]					
					var aos = new Array();					
					if(this.gpsData == null){
						var ids = treeActiveObject.getAllObjects();
						for(var n=0;n<ids.length;n++){
							aos.push([ids[n],0]);  // first request
						}
					}else{
						for(var n=0;n<this.gpsData.length;n++){
							aoid = this.gpsData[n].aoid;
							time = this.gpsData[n].time;
							aos.push([aoid,time]);
						}
					}
					//发送请求Ajax
					var req = Ext.util.JSON.encode(aos)
					Ext.Ajax.request({
								url: '/getGpsData',
								success: gDataMgr.loadsucc,
								failure: gDataMgr.loadfail,
								params: { params: req }
					});
    },
    interval: 4000 //1 second	
	}

	this.startGrab=function(){
		Ext.TaskMgr.start(this.task);
	}
	this.stopGrab = function(){
	}
}



Ext.onReady(function(){
	gDataMgr = new DataManager();
	init_map();
	init_MapMarkers(gMap);
	
	new Ext.Viewport({
		layout: 'border',
		items: [{
				region: 'north',
				//html: '<h1 class="x-panel-header">Page Title</h1>',
				title:'',
				autoHeight: true,
				border: false,
				margins: '0 0 0 0',
				//height:100,
				html:"<h1>[ swGis@2010 ] sw2us.com  msn:socketref@hotmail.com </h1>" //"<img src=\"/medias/images/logo.png\" width=\"70\" height=\"65\">"
				//tbar:test_new_tbar1()
			}, 
			{
				region: 'west',
				collapsible: true,
				title: 'Navigation',
				width: 300,
				split:true,
				layout:'border',
			// the west region might typically utilize a TreePanel or a Panel with Accordion layout
				items:[
					newTreeActiveObject(),
					createActiveObjectDetailGrid(5)
					//test_form1()
				]
			}, {
				region: 'south',
				//title: 'Title for Panel',
				//collapsible: true,
				html: "<img src=\"/medias/images/logo.png\" width=\"80\" height=\"60\" >",
				split: true,
				//height: 100,
				//minHeight: 10,
				autoHeight: true,
				border: false,
				margins: '0 0 0 0'
			},
			gMap.ui
			/*
			{
			id:'maptab',
			region: 'center',
			xtype: 'tabpanel', // TabPanel itself has no title
			//activeTab:0,
			items: [											
				{
					title: 'Default Tab',
					html: 'The first tab\'s content. Others may be added dynamically'
				}
				
			]
		}*/
		]
	});
	//alert( typeof(Ext.get('maptab')));
	//alert( Ext.get('maptab').constructor.toString() );
	//alert(  Ext.get('maptab') instanceof Ext.TabPanel );	
	gMap.setCenter(new OpenLayers.LonLat(121.4188, 31.1282), 4);
	gDataMgr.startGrab(); //启动定时获取gps数据
	
	
});