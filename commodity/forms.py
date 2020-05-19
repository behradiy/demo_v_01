from django import forms
from .models import Category
from django.contrib.auth.models import User
class importCommodity(forms.Form):
    cats= Category.objects.all()
    catsstr= ""
    for c in cats:
        catsstr+=(c.Name+" ")

    Marketers=User.objects.all()
    Marketerstr= ""
    for us in Marketers:
        Marketerstr+=(str(us.id)+" ")

    Category = forms.CharField(max_length=50,help_text=catsstr)
    Name = forms.CharField(max_length=50)
    Marketer = forms.IntegerField(help_text=Marketerstr)
    Price= forms.IntegerField()
    About = forms.CharField(max_length=2000)
    Amountinstore=forms.IntegerField()
    Image=forms.ImageField()

class SortImport(forms.Form):
    choices=(('Price', 'Price'),('Popularity', 'Popularit'),('Vies', 'Views'))
    Import=forms.ChoiceField(choices=choices,label='import sort')

class importCategory(forms.Form):
    Name = forms.CharField(max_length=50)




