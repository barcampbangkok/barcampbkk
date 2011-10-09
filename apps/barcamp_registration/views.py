# Create your views here.

from django.shortcuts import render_to_response
from django.template.context import RequestContext

def registration(request):
    context = RequestContext(request)
    return render_to_response('barcamp_registration/registration.html',context=context)