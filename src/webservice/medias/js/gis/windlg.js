
function new_window1(){
	var w = new Ext.Window({ 
			title:'test window',
			width:400,
			height:300,			
			modal:true  //模态窗口属性，但没法再api中找到
		});
	w.show();

	
}