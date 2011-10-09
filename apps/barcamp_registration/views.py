# Create your views here.

from django.shortcuts import render_to_response
from django.template.context import RequestContext
from menus.utils import simple_language_changer

from barcamp_registration.forms import BarcampRegistrationForm

@simple_language_changer
def registration(request):
    context = RequestContext(request)
    form = BarcampRegistrationForm()
    return render_to_response('barcamp_registration/registration.html',{'form':form},context_instance=context)