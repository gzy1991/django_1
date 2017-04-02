from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.views.static import serve


import datetime

def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request,'hello.html',context)

def current_datetime(request):
    now=datetime.datetime.now()
    html="<html><body>It is now %s</body></html>" % now
    return HttpResponse(html)



