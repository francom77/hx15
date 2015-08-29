
$.ajax({
    url: "http://localhost:8000/getData",
    jsonp: "callback",
    dataType: "jsonp",
    success: function(response){

        _.each(response, function(item){
            var $template = $("#item-template");
            var template = $template.html();
            var item_html = Mustache.render(template, item);
            $(".items-list").append($(item_html));
        });
    }
});
