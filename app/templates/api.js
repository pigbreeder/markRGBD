functinon mark_save(data){
	$.ajax({
	    type: 'POST',
	    url: '/simple/mark/save',
	    data: data, 
	    dataType: 'json', 
	    success: function(data) { 

	    },
	    error: function(xhr, type) {

	    }
	});
}

functinon mark_list(data){
	$.ajax({
	    type: 'POST',
	    url: '/simple/mark/save',
	    data: data, 
	    dataType: 'json', 
	    success: function(data) { 

	    },
	    error: function(xhr, type) {

	    }
	});
}
