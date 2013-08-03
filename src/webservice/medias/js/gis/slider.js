
function new_slider1(){
	var slider1= new Ext.Slider({
		 width: '100,%',
		 minValue: 0,
		 maxValue: 100,
		 plugins: new Ext.slider.Tip({
			 getText: function(thumb){
				 return String.format('{0}% complete', thumb.value);
			 }
		 })
	 });
	return slider1;
 };
 
 function new_slider2(){
	 return new Ext.slider.SingleSlider({
		//renderTo: Ext.getBody(),
		width: 200,
		value: 50,
		increment: 10,
		minValue: 0,
		maxValue: 100
	});

}

//
function new_slider3(){
	return new Ext.Slider({
		//renderTo: Ext.getBody(),
		width: 200,
		values: [25, 50, 75], //multi-thumb
		minValue: 0,
		maxValue: 100,

		//this defaults to true, setting to false allows the thumbs to pass each other
		constrainThumbs: false
	});
}
