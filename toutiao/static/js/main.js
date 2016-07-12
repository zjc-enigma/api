function capitalizeEachWord(str) {
    return str.replace(/\w\S*/g, function(txt) {
        return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();
    });
}

$(document).ready(function() {
    $words = $(".words");
	  $title = $(".title");
    $searchtag = $(".searchtags");

	$('.generate').click(function(e) {
		e.preventDefault;
		  $title.hide();
      $words.hide();
      $searchtag.hide();

	});

    $( 'a#process_input' ).bind('click', function() {
				$.getJSON('/demos/ad_crawl/generate', {
				    inputword: $('input[name="inputword"]').val(),

				}, function(data) {
            var output="";
            var loop_count = 0;
            var search_tag_content = "";

            for (var key in data){
                search_tag_content += '<li><a href="#orgheadline' + loop_count.toString() + 'search">' + key + '</a></li>';
                output += '<div id="outline-container-orgheadline"' + loop_count.toString() + 'search class="outline-3">';
                output += '<h3 id="orgheadline' + loop_count.toString() + 'search">' + key + '</h3>';
                output += '<div class="table-responsive">';
                output += '<table class="table table-striped">';
                output += '<tbody>';
                for (var i in data[key]){
                    output += '<tr><td><a href="' + data[key][i].url + '">' + data[key][i].title + '</a></td></tr>';
                }
                output += '</tbody>';
                output += '</table>';
                output += '</div>';
                loop_count += 1;
            }
            $searchtag.html(search_tag_content);
            $searchtag.show();
            $words.html(output);
            $words.show();
            window.location="#orgheadline3level";
				});

				return false;
		});

});
