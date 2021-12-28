from django.urls import path
#from .services import get_all_indian_news
from .views import *

urlpatterns = [
    #path('allindiannews/' , get_all_indian_news , name= "All Indian News" ),
    #path('', getIndianNews.as_view(template_name='index.html')),
    #path("" , get_all_indian_news),
    path("" , top_news , name = "index"),
    path("search/" , search_news , name = "search"),
    path('login/' , login , name = 'login'),
    path('loggedin/' , logged_in_news , name = "logged_in" ),
    path('logout/' , logout_view , name = 'logout')
    # path('login',login_user),
    # path('signup',signup_user),
]
