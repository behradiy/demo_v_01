from django.shortcuts import render
from django.views.generic import TempaleView

# Create your views here.
class HomePageView(TemplateView):
    tempalte_name="home.html"
    
