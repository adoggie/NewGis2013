
/*
Shortcut  xtype          Class                  Description
'->'      'tbfill'       Ext.Toolbar.Fill       begin using the right-justified button container
'-'       'tbseparator'  Ext.Toolbar.Separator  add a vertical separator bar between toolbar items
' '       'tbspacer'     Ext.Toolbar.Spacer     add horiztonal space between elements
          'tbtext'  只是文本
*/

function test_tbar_combox(){
	var combo = new Ext.form.ComboBox({
		store: new Ext.data.ArrayStore({
			autoDestroy: true,
			fields: ['initials', 'fullname'],
			data : [
				['FF', 'Fred Flintstone'],
				['BR', 'Barney Rubble']
			]
		}),
		displayField: 'fullname',
		typeAhead: true,
		mode: 'local',  //数据是本地的
		forceSelection: true,
		triggerAction: 'all',
		emptyText: 'Select a name...',
		selectOnFocus: true,
		width: 135,
		getListParent: function() {
			return this.el.up('.x-menu');
		},
		iconCls: 'no-icon' //use iconCls if placing within menu to shift to right side of menu
	});
	return combo;
}

function test_circle_button(){
	var btn = new Ext.CycleButton({
		showText: true,
		//prependText: 'View as ',
		items: [{
			text:'text only',
			iconCls:'view-text',
			checked:true
		},{
			text:'HTML',
			iconCls:'view-html'
		}],
		changeHandler:function(btn, item){
			Ext.Msg.alert('Change View', item.text);
		}
	});
	return btn;
}

function test_new_tbar1(){
	return new Ext.Toolbar({
					items:[ //默认是button
						{xtype: 'tbtext', text: 'Item 1'},
						{	text:'botton1',
							
							handler: function(e){
								Ext.Msg.alert(e.getTarget());
							}
						},
						test_tbar_combox(),
						{text:'button_x',
							menu:test_tbar_menu(),
						},
						test_circle_button(),
						'->',
						{xtype: 'tbspacer', width: 50},
						{text:'button2'},'|',{text:'button3'}
					]
				});
}