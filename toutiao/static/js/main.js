function capitalizeEachWord(str) {
    return str.replace(/\w\S*/g, function(txt) {
        return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();
    });
}

$(document).ready(function() {
    $words = $(".words");
	  $title = $(".title");

	$('.generate').click(function(e) {
		e.preventDefault;
		  $title.hide();
      $words.hide();

	});

    $( 'a#process_input' ).bind('click', function() {
				$.getJSON('/generate', {
				    inputword: $('input[name="inputword"]').val(),

				}, function(data) {
            var output="";
            var loop_count = 0;

            for (var key in data){
                output += '<div id="outline-container-orgheadline"' + loop_count.toString() + 'search class="outline-3">'
                output += '<h3 id="orgheadline' + loop_count.toString() + 'search">' + key + '</h3>'
                output += '<div class="table-responsive">'
                output += '<table class="table table-striped">'
                output += '<tbody>'
                for (var i in data[key]){
                    output += '<tr><td><a href="' + data[key][i].url + '">' + data[key][i].title + '</a></td></tr>'
                }
                output += '</tbody>'
                output += '</table>'
                output += '</div>'
                loop_count += 1;
            }
            $words.html(output);
            $words.show();
            window.location="#orgheadline3level";
				});

				return false;
		});

});
