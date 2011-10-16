/* require {{MEDIA_URL}}js/jquery-1.4.4.min.js */    

var feed = [];
twitter_search();

function twitter_search() {
    var url = "/media/search.json" 
    $.Updater(url, {}, twitter_search_call_back);
}

function twitter_search_call_back(data) {
    add_to_feed(data.results, twitter_to_feed_item);
    feed.sort(compare_by_created_at);
    update_output(feed);
}

function add_to_feed(results, to_feed_item_fn) {
    $.each( results, function (index, result) {
        var feed_item = to_feed_item_fn(result); 
        feed.push(feed_item);
    });
}

function twitter_to_feed_item(search_result) {
    var feed_item = { "text": search_result.text,
                      "created_at": string_to_date(search_result.created_at),
                      "from_user": search_result.from_user,
                      "profile_image": search_result.profile_image_url 
                    };
    return feed_item;
}

function feed_to_html(feed_items) {
    var list = $("<div/>");
    $.each( feed_items, function( index, item ) {
        var profile = $("<img/>").attr("src", item.profile_image);
        var str = item.from_user + " : " + item.text;
        var msg = $("<p/>").text(str);
        var created_at = $("<p/>").text(item.created_at.toString());
        var element = $("<div/>");

        // set class for each element
        profile.attr("class", "profile"); 
        msg.attr("class", "msg");
        created_at.attr("class", "created_at");

        profile.appendTo(element);
        msg.appendTo(element);
        created_at.appendTo(element);
        element.appendTo(list);
    });
    return list;
}

function update_output(feed_items) {
    var list_in_html = feed_to_html(feed_items);
    empty_array(feed_items)
    $("#output").html(list_in_html);
}

