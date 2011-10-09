# Create your views here.
import logging
logger = logging.getLogger(__name__)

from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.db import IntegrityError
from django.core.urlresolvers import reverse

from menus.utils import simple_language_changer

from barcamp_registration.models import BarcampRegistration
from barcamp_registration.forms import BarcampRegistrationForm

@simple_language_changer
def registration(request):
    context = RequestContext(request)
    status_code = 200
    if request.method == "POST":
        form = BarcampRegistrationForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return HttpResponseRedirect(reverse('whos_coming'))
            except IntegrityError:
                status_code = 400
                logger.exception(request.POST)
        else:
            status_code = 400
            logger.info('form is invalid for: %s' % (request.POST))
    else:
        form = BarcampRegistrationForm()
    response_content = render_to_response('barcamp_registration/registration.html',
                                        {'form':form},
                                        context_instance=context)
    if status_code == 400:
        return HttpResponseBadRequest(response_content)
    else:
        return response_content

@simple_language_changer
def whos_coming(request):
    context = RequestContext(request)
    return render_to_response('barcamp_registration/whos_coming.html',
                                {'whos_coming':BarcampRegistration.objects.all().order_by('-id')},
                                context_instance=context)