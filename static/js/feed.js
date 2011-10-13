/* require /static/pinax/js/jquery-1.3.2.min.js */

var feed = [];
var twitter_username = 'juacompe';
var max_timeline = 5;
var hashtag = 'thestar7';
twitter_search(twitter_username, hashtag);

function twitter_search(user, tag) {
    var url = "http://search.twitter.com/search.json?q=FROM:%user+OR+%23%hashtag&callback=?" 
    url = url.replace("%user", user)
    url = url.replace("%hashtag", tag)
    $.getJSON( url, twitter_search_call_back );
}

function twitter_search_call_back(data) {
    add_to_feed(data.results, twitter_to_feed_item);
    feed.sort(compare_by_created_at);
    update_output();
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

function feed_to_html() {
    var list = $("<div/>");
    $.each( feed, function( index, item ) {
        var profile = $("<img/>").attr("src", item.profile_image);
        var str = item.from_user + " : " + item.text;
        var msg = $("<p/>").text(str);
        var created_at = $("<p/>").text(item.created_at.toString());
        var element = $("<div/>")
        profile.appendTo(element);
        msg.appendTo(element);
        created_at.appendTo(element);
        element.appendTo(list);
    });
    return list;
}

function update_output() {
    var list = feed_to_html();
    $("#output").html(list);
}
