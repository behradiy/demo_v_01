"""demo_v_01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
<<<<<<< HEAD
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('loginapp/', include('django.contrib.auth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'), # new
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
=======

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('',include('homepage.urls')),
>>>>>>> b4c7abd111ab6aa238e95b29616c34ab6412c488
]


urlpatterns += [
    path('users/', include('django.contrib.auth.urls')),
    ]
