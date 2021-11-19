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
import requests
# Create your views here.


# def get_all_indian_news(request):

#     url = "https://indian-news-live.p.rapidapi.com/news"

#     headers = {
#     'x-rapidapi-host': "indian-news-live.p.rapidapi.com",
#     'x-rapidapi-key': "fd72cb71a9msh1fa6a2791e31886p1c79aejsne23a14ea8bd6"
#     }

#     response = requests.get(url, headers= headers)

#     return HttpResponse(response)

def top_indian_news(request):
    API_KEY = "e6a2a3f2f2ad4258adca6d6e017584d2"
    COUNTRY = 'in'
    CATEGORY = 'sports'
    #USING NEWS API (https://newsapi.org/)

    url = f"https://newsapi.org/v2/top-headlines?category={CATEGORY}&country={COUNTRY}&apiKey={API_KEY}"

    response = requests.get(url)
    data = response.json()
    articles = data['articles']
    #print(data)

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
