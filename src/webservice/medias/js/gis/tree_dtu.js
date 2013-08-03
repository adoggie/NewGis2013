
var treeActiveObject =null;
function TreeActiveObject(){
		
	this.rootnode = new Ext.tree.AsyncTreeNode({expanded: true,checked:false});


  this.handle= new Ext.tree.TreePanel({        
        //title: 'My Task List',
        height: 200,
        width: '100%',
        useArrows:true,
        autoScroll:true,
        animate:true,
        enableDD:true,
        containerScroll: true,
        rootVisible: false,
        frame: true,
				region:'center',
        root: this.rootnode,				
				
				/*loader: new Ext.tree.TreeLoader(
											{dataUrl:'getActiveObjects/',
												listeners:{
													load:function(p1,p2,p3){
														//alert(1000);
														//this.rootnode.expand(true);														
													}
												}
											
											}),				 */
        listeners: {
            'checkchange': function(node, checked){
                if(checked){
                    node.getUI().addClass('complete');
                }else{
                    node.getUI().removeClass('complete');
                }
            },
						click:function(n,e){
							if(n.attributes.children==undefined){
								//alert(n.attributes.id);
								aoDetailGrid.setActiveObject({name:n.attributes.text,aoid:n.attributes.id});
							}
						}
        }
        
				/*buttons: [{
            text: '刷新',
						handler:function(){																
								Ext.MessageBox.alert(treeActiveObject.getAllObjects());
							}
						}
						]*/
    });
	
		//加载树
	this.reloadTree = function(){
		Ext.Ajax.request({
            url: 'getActiveObjects/',
            success: function(request) {
                    var data = Ext.util.JSON.decode(request.responseText);
										treeActiveObject.rootnode.removeAll(false);
                    treeActiveObject.rootnode.appendChild(data);
                    treeActiveObject.rootnode.expandChildNodes(true);
										//添加ao对象到地图上作为marker
										
										for(var n=0;n<data.length;n++){
											var g  = data[n];
											
											for(var m=0;m<g.children.length;m++){
												var ao = g.children[m]
												g_aoMarkerMgr.createActiveObject(ao.id,ao.text);
												
											}
										}
										//
										g_aoMarkerMgr.show();
                    
            },
            failure: function() {
                    Ext.MessageBox.show({
                        title: '版块管理',
                        msg: '对不起,加载数据出现异常,请重试!',
                        buttons: Ext.MessageBox.OK,
                        icon: Ext.MessageBox.ERROR
                    });
            }
    });
	}
	
	this.reloadTree();
	
	//获取所有ao对象的aoid
	this.getAllObjects = function(){
		var aoids = new Array();		
		this.rootnode.eachChild(
			function(n){				
				for(var n2=0;n2< n.attributes.children.length;n2++){					
					aoids.push(n.attributes.children[n2].id);					
				};
			});
		return aoids;
	}
	
	
}

function newTreeActiveObject(){
	treeActiveObject = new TreeActiveObject();
	return treeActiveObject.handle;
}