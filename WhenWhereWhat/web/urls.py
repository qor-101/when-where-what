from django.urls import path
#from .services import get_all_indian_news
from .views import *


urlpatterns = [
    #path('allindiannews/' , get_all_indian_news , name= "All Indian News" ),
    #path('', getIndianNews.as_view(template_name='index.html')),
    #path("" , get_all_indian_news),
    path("" , top_indian_news)
]
