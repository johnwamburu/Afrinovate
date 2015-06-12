from django.template import RequestContext
from django.shortcuts import render, render_to_response

def index(request):
    batch = {}
    return render_to_response('web/index.html', batch, context_instance=RequestContext(request))
