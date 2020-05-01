from django.contrib.auth import views
from django.urls import path
from .views import *
from . import views
app_name = 'login_page'

urlpatterns = [
#    path('login/', views.loginView.as_view(), name='login'),
]
