from django.shortcuts import render, redirect
from .models import *
from django.http import HttpRequest, HttpResponse
from django.template import loader
from .forms import importCommodity,SortImport,importCategory


def mainpage(request):

    if (request.method=='GET'):
        cms = Commoditie.objects.order_by('Views')[:30]
        context = {'commodity': cms, 'SortImport':SortImport}
        return render(request, 'commodity/CommodityMain.html', context)

    elif(request.method=='POST'):
        if 'Import' in request.POST:
            cms = Commoditie.objects.order_by(request.POST['Import'])[0:30]

            context= {'commodity':cms,'SortImport':SortImport}
            return render(request, 'commodity/CommodityMain.html', context)

def MainImport(request):
    if (request.method=='GET'):
        return render(request,'commodity/MainImport.html',context=None)




def importcommodity (request):
    if (request.method == 'POST'):
        C=Category.objects.get(Name=request.POST['Category'])
        M = User.objects.get(id=request.POST['Marketer'])
        COM=Commoditie.objects.create(Name=request.POST['Name'],
                                  Price=request.POST['Price'],
                                  Category=C,
                                  Marketer=M,
                                  AmountinStore=request.POST['Amountinstore'],
                                  About=request.POST['About']
                                    )
        #image=request.POST['Image']
        COM.save();
        return HttpResponse("ok siktir")


    elif (request.method=='GET'):
        Context = {'form': importCommodity()}
        return render(request,'commodity/ImportCommodity.html',Context)

def importcategory(request):
    context = {'catformcont':importCategory()}
    return render(request,"commodity/ImportCat.html",context)


# Create your views here.
