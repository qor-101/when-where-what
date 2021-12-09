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
        'zero' : articles[0],
        'news' : articles[1:],
    }

    return render(request , 'index.html' , context)



def search_news(request):
    if request.method == 'GET':
        SEARCH_WORDS = request.GET.get('search-btn')
    print(SEARCH_WORDS)
    url = f"https://newsapi.org/v2/everything?q={SEARCH_WORDS}&apiKey={settings.API_KEY_VARUN}"

    response = requests.get(url)
    data = response.json()
    articles = data['articles']

    context = {
        'zero' : articles[0],
        'news' : articles[1:],
    }
    return render(request , 'index.html' , context)

def get_user():
    mydb = sqlite3.connect("db.sqlite3")
    mycursor = mydb.cursor()  
    res = mycursor.execute('SELECT username FROM auth_user')
    lis=[]
    for i in res:
        lis.append(i[0])
    mydb.close()
    return lis

@csrf_exempt
def login_user(request):
    cand_usn = request.POST['UN']
    cand_pwd = request.POST['PW']
    user = authenticate(request, username = cand_usn, password = cand_pwd)
    if user is not None:
        login(request, user)
        return redirect('/profile')
    else: 
        # create alert as login failed
        return redirect('/')

@csrf_exempt
def signup_user(request):
    
    new_fname = request.POST['fname']
    new_email = request.POST['mail']
    new_usn = request.POST['usn']
    new_pwd = request.POST['pwd']
    pref = []
    cat1 = request.POST.get('cat1',False)
    cat2 = request.POST.get('cat2',False)
    cat3 = request.POST.get('cat3',False)
    cat4 = request.POST.get('cat4',False)
    cat5 = request.POST.get('cat5',False)
    if cat1:
        pref.append(cat1)
    if cat2:
        pref.append(cat2)
    if cat3:
        pref.append(cat3)
    if cat4:
        pref.append(cat4)
    if cat5:
        pref.append(cat5)
    
    usn_list = get_user()
    if(new_usn in usn_list):
        #create alert usn not available
        return redirect("/")
    else:
        user = User.objects.create_user(new_usn, email=new_email, password=new_pwd)
        user.first_name = new_fname
        user.save()
        # saving preferences in preference table
        prefs = ",".join(pref)
        mydb = sqlite3.connect("db.sqlite3")
        mycursor = mydb.cursor()  
        mydb.execute("INSERT INTO preference VALUES(?,?)",(new_usn,prefs))
        mydb.commit()
        mydb.close()
        
        if user is not None:
            login(request,user)
            return redirect('/profile')
        else:
            return redirect('/') 
