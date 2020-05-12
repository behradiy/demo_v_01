from django import forms

class importCommodity(forms.Form):
    Category = forms.CharField(max_length=50)
    Name = forms.CharField(max_length=50)
    Marrketer = forms.IntegerField()
    Price= forms.IntegerField()
    About = forms.CharField(max_length=2000)
    Image = forms.ImageField()
    Amountinstore=forms.IntegerField()


