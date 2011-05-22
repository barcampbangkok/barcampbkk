function test_twitter_search() {
    test_twitter_to_feed_item_parse_result_properly()
}

function test_twitter_to_feed_item_parse_result_properly() {
    var result = {"profile_image_url":"http://a0.twimg.com/profile_images/1364330878/x2_60d863e_normal.jpg",
                  "created_at":"Sun, 22 May 2011 12:00:32 +0000",
                  "from_user":"BaitOng_Seo",
                  "text":"sample_text",
                 }
    var feed_item = twitter_to_feed_item(result)
    msg = "twitter_to_feed_item parse text properly"
    jqUnit.ok(feed_item.text == result.text, msg)
    msg = "twitter_to_feed_item parse from_user properly"
    jqUnit.ok(feed_item.from_user == result.from_user, msg)
    msg = "twitter_to_feed_item parse profile_image properly"
    jqUnit.ok(feed_item.profile_image == result.profile_image_url, msg)
}

function test_twitter_to_feed_item_calls_string_to_date() {
    var mock = new jqMock.Mock(window, "string_to_date")
    var call_count = 1
    var date_str = "Sun, 22 May 2011 12:00:32 +0000"
    var result = {"profile_image_url":"http://a0.twimg.com/profile_images/1364330878/x2_60d863e_normal.jpg",
                  "created_at":date_str,
                  "from_user":"BaitOng_Seo",
                  "text":"sample_text",
                 }
    mock.modify().args(date_str).multiplicity(call_count)
    twitter_to_feed_item(result)
    mock.verifyAll()
    mock.restore()
}

function test_twitter_search_calls_twitter_api() {
    var mock = new jqMock.Mock($, "getJSON")
    var hashtag = "test_tag"
    var user = "test_user"
    var call_count = 1
    url = "http://search.twitter.com/search.json?q=FROM:%user+OR+%23%hashtag&callback=?"
    url = url.replace("%user", user)
    url = url.replace("%hashtag", hashtag)
    mock.modify().args(url, twitter_search_call_back).multiplicity(call_count)
    twitter_search(user, hashtag)
    mock.verifyAll()
    mock.restore()
}

function test_twitter_search_call_back_adds_results_to_feed() {
    var mock = new jqMock.Mock(window, "add_to_feed")
    var call_count = 1
    results = []
    data = {'results': results}
    mock.modify().args(results, twitter_to_feed_item).multiplicity(call_count)
    twitter_search_call_back(data)
    mock.verifyAll()
    mock.restore()
}

function test_twitter_search_call_back_sorts_by_created_at() {
    var mock = new jqMock.Mock(window.feed, "sort")
    var call_count = 1
    var comparator = window.compare_by_created_at
    results = []
    data = {'results': results}
    mock.modify().args(comparator).multiplicity(call_count)
    twitter_search_call_back(data)
    mock.verifyAll()
    mock.restore()
}

function test_twitter_search_call_back_calls_update_output() {
    var mock = new jqMock.Mock(window, "update_output")
    var call_count = 1
    results = []
    data = {'results': results}
    mock.modify().args().multiplicity(call_count)
    twitter_search_call_back(data)
    mock.verifyAll()
    mock.restore()
}

function test_add_to_feed_add_item_to_feed() {
    var mock = new jqMock.Mock(window.feed, "push")
    var results = ['a', 'b', 'c']
    var call_count = results.length 
    var parser = function(){}
    mock.modify().args(jqMock.is.anything).multiplicity(call_count)
    add_to_feed(results, parser)
    mock.verifyAll()
    mock.restore()
}

function test_add_to_feed_calls_parser_for_every_item() {
    var mock = new jqMock.Mock(window, "twitter_to_feed_item")
    var results = ['a', 'b', 'c']
    mock.modify().args('a').multiplicity(1)
    mock.modify().args('b').multiplicity(1)
    mock.modify().args('c').multiplicity(1)
    add_to_feed(results, twitter_to_feed_item)
    mock.verifyAll()
    mock.restore()
}
