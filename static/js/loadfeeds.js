$(document).ready(function() {
        $.getJSON('http://pipes.yahoo.com/pipes/pipe.run?_id=65b02c87ed56d130499b0450060c9627&_render=json&_callback=?',
                function(json){
                        $.each(json.value.items, function(i, item) {
                                var ti = '<a class="news-title" href="' + item.link + '">' + item.title + '</a>';
                                var des = '<p class="news-description">' + item.description + '</p>';
                                var so = '<span class="news-source">' + item.source + ' &mdash; </span>';
                                var date = '<span class="news-date">' + item.pubDate + '</span>';
                                var content = ti + '<br />' + so + date + des;
                                $('#content').append('<div>' + content +  '</div>');
                                if (i>0 && (i+1 % 2==0)) {
                                    $('#content').append('<div class="clear"></div>');
                                    
                                };
                                
                        });
        });   
});
