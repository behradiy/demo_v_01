from django.shortcuts import render
from .models import *
from django.http import HttpRequest,HttpResponse
from django.template import loader
def mainpage(request):
    cms = Commoditie.objects.all()
    context = {'commodity': cms, }
    t = loader.get_template('commodity/CommodityMain.html')
    t.render(context)
    return HttpResponse(t)




# Create your views here.
