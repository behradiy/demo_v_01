from django.urls import path
from .views import mainpage , importcommodity

urlpatterns=[
    path('',mainpage,name='Commmain'),
    path('import/',importcommodity,name='importComm'),

]