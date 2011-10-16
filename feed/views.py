from django.core.serializers.json import DjangoJSONEncoder
from django.forms import model_to_dict
from django.http import HttpResponse
from feed.models import Tweet
from json import dumps

def new_tweets(request):
    tweets = Tweet.objects.all().extra(order_by = ['-created_at'])
    json_str = dumps({'max_id_str': '117972896940437504',
                      'next_page': '/api/new_tweets/after/117972896940437504',
                      'results': [ model_to_dict(tweet) for tweet in tweets ]
                     }, cls = DjangoJSONEncoder)
    return HttpResponse(json_str)

