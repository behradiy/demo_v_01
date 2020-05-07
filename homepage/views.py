from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def mainview(request):
    template = loader.get_template('homepage/main.html')
    return HttpResponse(template.render(context=None, request=request))
