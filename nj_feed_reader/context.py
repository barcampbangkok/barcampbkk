from django.conf import settings
def twitter_tags(request):
    """
    Adds NJ_feed_reader context variables to the context.

    """
    return {'TWITTER_TAGS': settings.TWITTER_TAGS}