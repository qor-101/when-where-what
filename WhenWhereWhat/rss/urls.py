from django.urls import path
from .views import *

urlpatterns = [
    path('toi/', toi, name='toi'),
    path('indiatoday/', indiatoday, name='indiatoday'),
    path('etimes/', etimes, name='etimes'),
]