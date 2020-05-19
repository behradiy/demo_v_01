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
    SelesNumber = models.IntegerField(default=0)
    Popularity=models.IntegerField(default=0)
    Views=models.IntegerField(default=0)
    AmountinStore = models.IntegerField()
    About = models.CharField(max_length=5000)
    image = models.ImageField(null=True)

class Category (models.Model):

    Name=models.CharField(max_length=50)
    selesNumber=models.IntegerField(default=0)
    Popularity = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    Image = models.ImageField(null=True)
    def __str__(self):
        return self.Name









# Create your models here.
