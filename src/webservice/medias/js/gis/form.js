
function test_form1(){
	var tf1 = new Ext.form.TimeField({
		minValue: '9:00 AM',
		maxValue: '6:00 PM',
		increment: 60
	});
	//return tf1;
	var f2 = new Ext.form.DateField(
			{data:new Date(),
				blankText:'choice date..',
				allowBlank:false,
				editable:false
			}
			);
	return f2;
}