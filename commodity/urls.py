from django.urls import path, re_path
from .views import importcommodity,importcategory,mainpage,MainImport


urlpatterns=[
    path('',mainpage,name='Commmain'),
    re_path(r'^import/$',MainImport,name='importComm'),
    path('import/comm/',importcommodity,name='importComm'),
    path('import/Cat/',importcategory,name='importCat'),

]