from .services import get_all_indian_news
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, request
from django.template import loader
from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from datetime import date
import sqlite3
from django.shortcuts import render
import requests
from .services import get_all_indian_news
from django.http import HttpResponse, response
from django.conf import settings
from urllib.parse import urlparse


# Create your views here.






#API_KEY = "e6a2a3f2f2ad4258adca6d6e017584d2"

def top_news(request):
    category = ""
    country = "in"

    if(request.GET.get('category')):
        category = request.GET.get('category')

    if(request.GET.get('country')):    
        country = request.GET.get('country')

    
    if(category == "" and country == ""):
        print("Error here 1")
        url = f"https://newsapi.org/v2/top-headlines?category=general&country=in&apiKey={settings.API_KEY_SUNDAR}"

    
    elif(country == ""):
        url = f"https://newsapi.org/v2/top-headlines?category={category}&apiKey={settings.API_KEY_SUNDAR}"
        print("ERROR 2")


    elif(category == ""):    
        url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={settings.API_KEY_SUNDAR}"


    else:
        url = f"https://newsapi.org/v2/top-headlines?category={category}&country={country}&apiKey={settings.API_KEY_SUNDAR}"


    response = requests.get(url)
    data = response.json()
    articles = data['articles']
    #print(data)

    context = {
        'news' : articles,

    }

    return render(request , 'index.html' , context)



def search_news(request):
    SEARCH_WORDS = "the+rock"
    url = f"https://newsapi.org/v2/everything?q={SEARCH_WORDS}&apiKey={settings.API_KEY}"

    response = requests.get(url)
    data = response.json()
    articles = data['articles']

    context = {
        'news' : articles
    }
    return render(request , 'index.html' , context)

@csrf_exempt
def login_user(request):
    cand_usn = request.POST['usn']
    cand_pwd = request.POST['pwd']
    user = authenticate(request, username = cand_usn, password = cand_pwd)
    if user is not None:
        login(request, user)
        return redirect('/profile')
    else: 
        # create alert as login failed
        return redirect('/')

@csrf_exempt
def signup_user(request):
    new_usn = request.POST['usn']
    new_pwd = request.POST['pwd']
    new_email = request.POST['mail']
    new_fname = request.POST['fname']
    new_lname = request.POST['lname']
    
    usn_list = get_user()
    if(new_usn in usn_list):
        #create alert usn npt available
        return redirect("/")
    else:
        user = User.objects.create_user(new_usn, email=new_email, password=new_pwd)
        user.first_name = new_fname
        user.last_name = new_lname
        user.save()
        
        if user is not None:
            login(request,user)
            return redirect('/profile')
        else:
            return redirect('/') 
