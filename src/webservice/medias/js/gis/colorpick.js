
function new_colorpick1(){

	var cp = new Ext.ColorPalette({value:'993300',
						listeners:{
							select:function (o,color){								
								//var  j= { name:'scott',b:100};
								//alert(j.name);
								try{
									//alert(Ext.util.JSON.encode(j));
									//alert(Ext.util.Format.date(10000025));									
								}catch(e){
									alert(e);
								}
							}
						}
					});
	return cp;
}