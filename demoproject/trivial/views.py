from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

from django.contrib.auth.decorators import login_required



def homepage(request):
    return render_to_response("homepage.html",
            context_instance = RequestContext(request))

@login_required
def secure(request):
    return render_to_response("secure.html",
            context_instance = RequestContext(request))


