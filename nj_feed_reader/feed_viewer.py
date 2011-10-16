from django.conf import settings
from django.core.files.storage import default_storage
from django.shortcuts import render_to_response
from django.template import RequestContext
from storage.image_utils import (collected_images, TWITTER_IMAGE_PATH,
                                 THUMBNAIL_PATH, collect_images_and_text)

TWITTER_IMAGE_URL = default_storage.url(TWITTER_IMAGE_PATH)
THUMBNAIL_IMAGE_URL = settings.MEDIA_URL + THUMBNAIL_PATH

def home(request):
    context = RequestContext(request)
    context['IMAGE_URL'] = TWITTER_IMAGE_URL
    context['THUMBNAIL_URL'] = THUMBNAIL_IMAGE_URL
    context['images'] = collected_images()
    context['tweets'] = collect_images_and_text()
    return render_to_response('home.html', context_instance=context)
