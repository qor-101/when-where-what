from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='homepage'),
    path('login',views.login_user,name='login_user'),
    path('signup',views.signup_user,name='signup_user'),
]
