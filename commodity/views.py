from django.shortcuts import render
from .models import *
from django.http import HttpRequest,HttpResponse
from django.template import loader
from .forms import importCommodity
def mainpage(request):
    cms = Commoditie.objects.all()
    context = {'commodity': cms, }
    t = loader.get_template('commodity/CommodityMain.html')
    t.render(context)
    return HttpResponse(t)

def importcommodity (request):
    if (request.method == 'POST'):
        C=Category.objects.get(Name=request.POST['Category'])
        M = User.objects.get(id=request.POST['Marketer'])
        COM=Commoditie.objects.create(Name=request.POST['Name'],
                                  Price=request.POST['Price'],
                                  Category=C,
                                  Marketer=M,
                                  AmountinStore=request.POST['Amountinstore'],
                                  About=request.POST['About'])
        COM.save();


    elif (request.method=='GET'):
        Context = {'form': importCommodity()}
        return render(request,'commodity/ImportCommodity.html',Context)




# Create your views here.
