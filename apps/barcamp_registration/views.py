# Create your views here.

from django.shortcuts import render_to_response
from django.template.context import RequestContext

from barcamp_registration.forms import BarcampRegistrationForm

def registration(request):
    context = RequestContext(request)
    form = BarcampRegistrationForm()
    return render_to_response('barcamp_registration/registration.html',{'form':form},context_instance=context)