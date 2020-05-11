from django.db import models
from django.contrib.auth.models import User
class Commoditie (models.Model):
    Category = models.ForeignKey('Category',on_delete=models.CASCADE)
    Name = models.CharField(max_length=50)
    Marketer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    Price = models.BigIntegerField()
    SelesNumber = models.IntegerField()
    Popularity=models.IntegerField()
    Views=models.IntegerField()
    AmountinStore = models.IntegerField()
    About = models.CharField(max_length=5000)
    image = models.ImageField()

class Category (models.Model):
    
    Name=models.CharField(max_length=50)
    selesNumber=models.IntegerField()
    Popularity = models.IntegerField()
    views = models.IntegerField()
    Image = models.ImageField()







# Create your models here.
