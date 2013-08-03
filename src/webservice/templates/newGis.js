///<reference path="js/vswd-ext_2.0.2.js" />  


/**
* 去除多余空格函数
* trim:去除两边空格 lTrim:去除左空格 rTrim: 去除右空格
* 用法：
*     var str = "  hello ";
*     str = str.trim();
*/
String.prototype.trim = function()
{
    return this.replace(/(^[\\s]*)|([\\s]*$)/g, "");
}
String.prototype.lTrim = function()
{
    return this.replace(/(^[\\s]*)/g, "");
}
String.prototype.rTrim = function()
{
    return this.replace(/([\\s]*$)/g, "");
}

////////////////////////////////////////////////////////
// classes
function DeviceObject(id,iconUrl,text){
	this.id = id;
	this.iconUrl = iconUrl;
	
	this.visible = true;
	this.ll = new OpenLayers.LonLat(0,0);
	this.icon = new OpenLayers.Icon(this.iconUrl);
	this.marker = new OpenLayers.Marker(this.ll,this.icon);
	this.layer = null;
	
	
	this.getPos = function(){
		return this.ll;
	}
	
	this.setText = function(text){
		this.text = text;
		var markHtml ="<div> <img src=\""+ this.iconUrl + "\"/>"+ this.text+"</div>";
		this.marker.icon.imageDiv.innerHTML  = markHtml;
	}
	this.show = function(){
		this.marker.display(true);
	}
	this.hide =function(){
		this.marker.display(true);
	}
	this.showText =function(b){		
		if( b){
			var markHtml ="<div> <img src=\""+ this.iconUrl + "\"/>"+ this.text+"</div>";
			this.marker.icon.imageDiv.innerHTML  = markHtml;
		}else{			
			this.marker.icon.imageDiv.innerHTML  = '';
			this.marker.setUrl(this.iconUrl);
		}
	}
	this.setPos = function(lon,lat){
		this.marker.lonlat = new OpenLayers.LonLat(lon,lat); 
		this.layer.layer.redraw();
	}
	
	this.setText(text);
}

function DeviceLayer(id,map){
	this.id='';
	this.visible = true;
	this.devices = new Array();
	this.layer = new OpenLayers.Layer.Markers( id );
	this.map = map;
	this.map.addLayer(this.layer);
	
	this.getDevice = function(id){
		var d = null;
		for(n=0;n<this.devices.length;n++){
			if( id == this.devices[n].id){
				d = this.devices[n];
				break;
			}
		}
		return d;
	}
	this.addDevice =function(d){
		d.layer = this;
		this.devices.push(d);
		this.layer.addMarker(d.marker);
	}
	this.removeDevice = function(id){
		for(n=0;n<this.devices.length;n++){
			if( id == this.devices[n].id){
				this.layer.removeMarker(this.devices[n].marker);
				this.devices.splice(n,1);
				break;
			}
		}
	}
	this.show =function(){
		this.layer.setVisibility(true);
	}
	this.hide =function(){
		this.layer.setVisibility(false);
	}
	this.showText = function(b){
		for(n=0;n<this.devices.length;n++){
			this.devices[n].showText(b);
		}
		this.layer.redraw();
	}
	
}


//////////////////////////////////////////////////////
//function 

//////////////////////////////////////////////////////
   function change(val){
        if(val > 0){
            return '<span style="color:green;">' + val + '</span>';
        }else if(val < 0){
            return '<span style="color:red;">' + val + '</span>';
        }
        return val;
    }

    /**
     * Custom function used for column renderer
     * @param {Object} val
     */
    function pctChange(val){
        if(val > 0){
            return '<span style="color:green;">' + val + '%</span>';
        }else if(val < 0){
            return '<span style="color:red;">' + val + '%</span>';
        }
        return val;
    }

		var g_devlist;
		
		var geoHotPosition_Tree;
		
		function swInitUI(){
			 geoHotPosition_Tree = new Ext.tree.TreePanel(
				{
					rootVisible: false,											
					root: new Ext.tree.AsyncTreeNode({expanded: true,checked:false,text:'设备组',}),
					loader: new Ext.tree.TreeLoader({dataUrl:'/getGeoHotPositions/'}),
					listeners: {
						click: function(n) { 
						}				
					}
				}); 
		}
		
		var PositionObject = Ext.data.Record.create([
														'id','devname','group','hwid','lon','lat','speed',
														'direct','satnum',														
  														/*{name: 'lon', type: 'float'},
  														{name: 'lat', type: 'float'},
  														{name: 'speed', type: 'float'},
  														{name: 'direct', type: 'float'},
  														{name: 'satnum', type: 'float'},														
  														//{name: 'gpstime', type: 'date', dateFormat: 'n/j h:ia'},*/
															'gpstime',
  														'nearpos'	
												]);
		
		
		//////////////////////////////////////////////////////////////////////////
		// initMap()
			var map, layer;
			var layerChina;
			var layerCities;
			var g_devicelayer;
			
			function initMap(){
			  OpenLayers.DOTS_PER_INCH = 96;
				
			
				var vlayer = new OpenLayers.Layer.Vector( "Editable" );
				var options = {					
          controls: [ ],
					scales:[2000 ,3500 ,5000, 7500 ,10000  ,20000  ,50000 , 100000  ,200000  ,400000 ,
					700000, 1000000, 2000000, 5000000 ,10000000 ,20000000 ,40000000],
          
					maxResolution: "auto", // 地理宽度/视窗宽度(单位:度)
					maxExtent: new OpenLayers.Bounds(70, 10, 130, 60), //地图显示的最大范围
          projection: "EPSG:4326",
//        units: 'm'
					units:'degrees',
					eventListeners: {
                        
            "zoomend": function(evt){ 
								
						}                        
          }
				};
        map = new OpenLayers.Map('chinamap', options);// , options);
				
				layerChina = new OpenLayers.Layer.WMS( "FirstMap",
											"http://wallizard.vicp.net:8000/wms",		
										{						
                        layers:'china',					 
                        srs: 'EPSG:4326',                                        
                        styles: '',                      
                        tiled: 'true'		//网格块缓冲 						
                    } 								
					);
				
				
				map.addLayer(layerChina);
		
				//缩放工具栏
				map.addControl(new OpenLayers.Control.PanZoomBar({ }));              
				//map.addControl(new OpenLayers.Control.PanZoomBar({ //position: new OpenLayers.Pixel(2, -10)}));              
				map.addControl(new OpenLayers.Control.Navigation());				//支持鼠标拖动，shift框选
				//map.addControl(new OpenLayers.Control.Scale($('scale')));			//缩放比
				//map.addControl(new OpenLayers.Control.MousePosition({element: $('location'),suffix:'度'}));  //显示鼠标位置
				
				//alert(lon.toString()+ ':'+lat.toSource());							 
				map.setCenter(new OpenLayers.LonLat(120.0, 31), 8);
				//map.zoomToMaxExtent();
				
		 }
		// end initMap()
//////////////////////////////////////////////////////////////////////////
//选择设备，地图定位显示并居中 
function selectDevice(id){
	g_devlist.getStore().each(function(rec){										
	for(n=0;n<datalist.length;n++){
		data = datalist[n];
		//Ext.Msg.alert(typeof(rec.get('id')),typeof(data.id));											
		if(rec.get('id') == id ){												
			//Ext.Msg.alert(rec.get('lon'));			
			var d = g_devicelayer.getDevice(id);
			if( d){
				//d.setPos(rec.get('lon'),rec.get('lat'));
				map.moveTo(new OpenLayers.LonLat(rec.get('lon'),rec.get('lat')));
			}
			break;
		}											
	}
	
});	
}

		//////////////////////////////////////////////////////////////////////////
		//Main Entry()
		//////////////////////////////////////////////////////////////////////////
		//
		var viewport ;
		
		function mainEntry(){}
    Ext.onReady(function(){
       
        Ext.state.Manager.setProvider(new Ext.state.CookieProvider());        
        OpenLayers.DOTS_PER_INCH = 96;
				
			
				var vlayer = new OpenLayers.Layer.Vector( "Editable" );
				var options = {					
          controls: [ ],
					scales:[2000 ,3500 ,5000, 7500 ,10000  ,20000  ,50000 , 100000  ,200000  ,400000 ,
					700000, 1000000, 2000000, 5000000 ,10000000 ,20000000 ,40000000],
          
					maxResolution: "auto", // 地理宽度/视窗宽度(单位:度)
					maxExtent: new OpenLayers.Bounds(70, 10, 150, 50), //地图显示的最大范围
          projection: "EPSG:4326",
					units:'degrees',
					eventListeners: {
                        
            "zoomend": function(evt){ 
								
						}                        
          }
				};
        var map = new OpenLayers.Map('chinamap', options);// , options);
				
				layerChina = new OpenLayers.Layer.WMS( "FirstMap",
											"http://wallizard.vicp.net:8000/wms",		
										{						
                        layers:'china',					 
                        srs: 'EPSG:4326',                                        
                        styles: '',                      
                        tiled: 'true'		//网格块缓冲 						
                    } 								
					);
				
				
				map.addLayer(layerChina);
		
				//缩放工具栏
				map.addControl(new OpenLayers.Control.PanZoomBar({ }));              
				//map.addControl(new OpenLayers.Control.PanZoomBar({ //position: new OpenLayers.Pixel(2, -10)}));              
				map.addControl(new OpenLayers.Control.Navigation());				//支持鼠标拖动，shift框选
				//map.addControl(new OpenLayers.Control.Scale($('scale')));			//缩放比
				map.addControl(new OpenLayers.Control.Scale());
        map.addControl(new OpenLayers.Control.MousePosition());
        //map.addControl(new OpenLayers.Control.MousePosition({element: $('location'),suffix:'度'}));  //显示鼠标位置
				
		
        
        new Ext.Viewport({
            layout: 'border',
            items:[
                {
                    xtype:'panel',
                    region:'north',
                    height:60
                },
                {
                    layout:'border',
                    region:'center',
                    items: [
                        {
                            xtype:'panel',
                            region:'west',
                            //split: true,
                            layout:'border',
                            width: 300,
                            //title: 'Navigation'
                            split: true,
                            collapsible: true,
                           // activeTab:0,
                            items:[{                
                                    region: 'center',
                                    collapsible: true,
                                    title: 'Navigation',
                                    xtype: 'treepanel',
                                    autoScroll: true,
                                    split: true,
                                    loader: new Ext.tree.TreeLoader({dataUrl:'/getPosObjects/'}),
                                    root: new Ext.tree.AsyncTreeNode(),
                                    rootVisible: false,
                                    listeners: {
                                        click: function(n) {
                                            Ext.Msg.alert('Navigation Tree Click', 'You clicked: "' + n.attributes.text + '"');
                                        }
                                    }
                                },{
                                    region:'south',
                                    title:'detail',
                                    xtype:'panel',
                                    height:400,
                                    split: true,
                                    collapsible: true,
                                }
                            ] 
                        },
                        new GeoExt.MapPanel({
                            map: map,
                            region: 'center',
                            zoom:2,
                            center:new OpenLayers.LonLat(121.3,31.0)
                        })
                    ]
                }]
        });
        

			
    });
