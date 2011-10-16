function test_integration_twitter_feed() {
    // Arrange
    var feed = [];
    // Act
    twitter_search();
    // Assert
    var tweets;
    setTimeout(function() {
        tweets = $('#output div div');
        var msg = "Should be able to fetch tweets"
        jqUnit.ok(tweets.length > 0, msg)
    }, (3 * 1000)); // wait 3 seconds to let tweets be fetched
}

