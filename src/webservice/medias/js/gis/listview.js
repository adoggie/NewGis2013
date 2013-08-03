
function new_ActiveObjectGrid(){
	var grid = new Ext.grid.PropertyGrid({
				title: 'AO-Info',
				autoHeight: true,
				width: 300,
				//renderTo: 'grid-ct',
				//headerAsText:false,
				header:false,
				region:'south',
				enableHdMenu: false,
				
				source: {
						"名称": "",
						"时间": '',
						"位置": '',
						"速度": '',
						"方向": '',
						"收星数": ''
				},
				buttons: [
							{
								text:'定位'
							},
							{text:'CenterOnMap'}
						]
			});
		grid.on("beforeedit",function(e) {
					e.cancel = true;
					return false;
					});
		//grid.source['名称'] = "abc";
	return grid;
}


var aoDetailGrid = null;

function ActiveObjectDetailGrid(updateInterval){	
	this.grid = new_ActiveObjectGrid();
	this.ao = null;  //当前选择的活动对象
	this.updateInterval = updateInterval; //定时更新时间间隔
	this.getActiveObject = function(){
		return this.ao; //{name,aoid}
	}
	this.setActiveObject =  function(ao){ // ao - {aoid,name}
		this.ao = ao;
		//this.grid.source['名称'] = aoDetailGrid.ao.name;
		//this.grid.update();
		this.grid.setSource({				
						"名称": ao.name,
						"时间": '',
						"位置": '',
						"速度": '',
						"方向": '',
						"收星数": ''
				
		});
	}
	//更新gps信息
	this.update =function(gpslist){
		if(this.ao == null){
			return ;
		}		
		for(var n=0;n<gpslist.length;n++){
			if(gpslist[n].aoid == this.ao.aoid){
				//设置信息
				var dt = new Date(parseInt(gpslist[n].time)*1000);
				
				this.grid.setSource({				
						"名称": aoDetailGrid.ao.name,
						"时间": dt.toLocaleString(),
						"位置": gpslist[n].lon+','+gpslist[n].lat,
						"速度": gpslist[n].speed,
						"方向": gpslist[n].angle,
						"收星数": gpslist[n].sateused
				
					});
				/*
				this.grid.source['名称'] = aoDetailGrid.ao.name;
				this.grid.source['时间'] = gpslist[n].time;					
				this.grid.source["位置"] = gpslist[n].lon+','+gpslist[n].lat;				
				this.grid.source["速度"] = gpslist[n].speed;
				this.grid.source["方向"] = gpslist[n].angle;
				this.grid.source["收星数"] = gpslist[n].sateused;
									*/
				//alert(this.grid.source["位置"]);
				break;		
			}
		}
	}
	//启动定时器
	this.task = {
    run: function(){
        //Ext.fly('clock').update(new Date().format('g:i:s A'));
				//Ext.MessageBox.alert("abc");
    },
    interval: 2000 //1 second	
	}
	Ext.TaskMgr.start(this.task);
}


function createActiveObjectDetailGrid(){
	aoDetailGrid = new ActiveObjectDetailGrid();
	return aoDetailGrid.grid;
}

 