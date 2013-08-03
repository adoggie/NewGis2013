var gMap;



function init_map(){
	OpenLayers.DOTS_PER_INCH = 96;
	var options = {					
					scales:[2000 ,3500 ,5000, 7500 ,10000  ,20000  ,50000 , 100000  ,200000  ,400000 ,
					700000, 1000000, 2000000, 5000000 ,10000000 ,20000000 ,40000000],
					 maxResolution: "auto",
					maxExtent: new OpenLayers.Bounds(70, 10, 130, 60), //µٍ¼Дʾµŗ·¶Χ
                    projection: "EPSG:4326",
					units:'degrees',
					controls:[]
                };
	var map = new OpenLayers.Map('map',options);
    var layer = new OpenLayers.Layer.WMS(
				"china",
				"http://122.227.135.172:8080/wms",
				//"http://192.168.14.66:8080/wms",
				{						
					layers:'china',					 
					srs: 'EPSG:4326',                                        
					styles: '',                      
					tiled: 'true'		//θ¸򀩻º³㞉					
				});
    map.addLayer(layer);

    var mapPanel = new GeoExt.MapPanel({
        title: "China Map",
        //renderTo: "mappanel",
        //stateId: "mappanel",
        //height: 400,
        //width: 600,
		region: 'center',
        map: map
		//zoom:4
		});
		
	map.addControl(new OpenLayers.Control.PanZoomBar());
	map.addControl(new OpenLayers.Control.Navigation());				//֧³׊󲫍϶¯£¬shift¿󑟍
    //map.addControl(new OpenLayers.Control.Scale($('scale')));			//̵·űƍ
    //map.addControl(new OpenLayers.Control.MousePosition({element: $('location'),suffix:'¶Ƨ}));  //Дʾ˳±뎻׃
	map.addControl(new OpenLayers.Control.Scale());			//̵·űƍ
    map.addControl(new OpenLayers.Control.MousePosition({suffix:'',prefix:'位置:',numDigits:4}));  //Дʾ˳±뎻׃
	//map.addControl(new OpenLayers.Control.NavToolbar());
	map.addControl(new OpenLayers.Control.ScaleLine());
	//map.addControl(new OpenLayers.Control.Measure());
	//map.setCenter(new OpenLayers.LonLat(121.4188, 31.1282), 4);
	//map.addControl(new OpenLayers.Control.NavigationHistory());
	 //map.addControl(new OpenLayers.Control.Button({trigger:function(){alert(100);} }));

	gMap = map;
	gMap.ui = mapPanel;
	return mapPanel;
}