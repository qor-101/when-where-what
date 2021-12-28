from django.urls import path
from .views import *

urlpatterns = [
    path('toi/', toi, name='toi'),
    path('indiatoday/', indiatoday, name='indiatoday'),
    path('news18/',news18,name='news18'),
    path('unasia/',unasia,name='unasia')
]
