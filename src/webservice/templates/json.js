///<reference path="js/vswd-ext_2.0.2.js" />  
Ext.onReady(function(){
  Ext.get('ok').on('click', function(e){
				Ext.Ajax.request({
					 url: '/json/',
					 success: function (resp,opts) {
						Ext.MessageBox.alert('',Ext.decode(resp.responseText).name); //返回hospital.name
					 },					 
					 failure: function (resp,opts) {
						alert(resp.toString());
					 },
					 //headers: {},
					 params: { foo:Ext.util.JSON.encode({students:[12,233,45],hospital:{name:'中国',addr:'shanghai road'} })}
				});
			

			}
	);
	
}

);
