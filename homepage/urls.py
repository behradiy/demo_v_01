from django.urls import path
from .views import *

urlpatterns = [
    path('' , mainview , name='mainview'),
]
