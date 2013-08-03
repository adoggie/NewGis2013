

function test_tbar_menu(){
	var menu = new Ext.menu.Menu({
		id: 'mainMenu',
		items: [
			test_tbar_combox() // A Field in a Menu
		]
	});
	return menu;
}
