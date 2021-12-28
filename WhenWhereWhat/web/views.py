from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, request
from django.template import loader
from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from datetime import date
from django.contrib.auth.hashers import make_password
import secrets
from django.contrib.auth import logout
import sqlite3
import requests
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, response
from django.conf import settings
from urllib.parse import urlparse
from django.contrib.auth.forms import UserCreationForm

from web.forms import UserRegisterForm
# from .models import User
from .models import Profile
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
import random
from django.contrib.auth.decorators import login_required



# Create your views here.

#API_KEY = "e6a2a3f2f2ad4258adca6d6e017584d2"
#When we go to models, it should reroute to register url!

def login(request):
    if request.method == 'POST':
        username = request.POST.get('UN')

        password = request.POST.get('PW')
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request , "Successfully logged into {0}".format(request.POST.get('UN')))
        return redirect('logged_in')


@login_required
def logged_in_news(request):
    category = random.choice(request.user.profile.preference.split(","))
    #category = 'sports'
    print("Category is " , category)
    country = request.user.profile.country
    print(country)
    
    url = f"https://newsapi.org/v2/top-headlines?category={category}&country={country}&apiKey={settings.API_KEY_VARUN}"
    

    response = requests.get(url)
    data = response.json()
    articles = data['articles']
    #print(data)

    context = {
        'zero' : articles[0],
        'news' : articles[1:],
        # 'form' : form,
    }

    return render(request , 'index.html' , context)


        

def top_news(request):

    if request.method == 'POST':
        #form = UserRegisterForm(request.POST)
        # print(request.POST.get('pwd' , False))

        print(request.POST)
        print(request.POST.getlist('preference'))

        user = User.objects.create(username = request.POST.get('usn') , email = request.POST.get('mail') , password = make_password(request.POST.get('pwd')))
        print(user)
        # print(request.user.id)
        Profile.objects.create(user = user,preference = ",".join(request.POST.getlist('preference')) , country = request.POST.get('country'))
        
        messages.success(request , "Account created for {0}. Please login!".format(request.POST.get('usn')))


    category = ""
    country = "in"

    if(request.GET.get('category')):
        category = request.GET.get('category')

    if(request.GET.get('country')):    
        country = request.GET.get('country')

    
    if(category == "" and country == ""):
        url = f"https://newsapi.org/v2/top-headlines?category=general&country=in&apiKey={settings.API_KEY_SUNDAR}"

    
    elif(country == ""):
        url = f"https://newsapi.org/v2/top-headlines?category={category}&apiKey={settings.API_KEY_SUNDAR}"


    elif(category == ""):    
        url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={settings.API_KEY_SUNDAR}"


    else:
        url = f"https://newsapi.org/v2/top-headlines?category={category}&country={country}&apiKey={settings.API_KEY_SUNDAR}"

    
    # if(request.GET.get('search-btn')):
    #     search_news(request)

    response = requests.get(url)
    data = response.json()
    articles = data['articles']
    #print(data)

    context = {
        'zero' : articles[0],
        'news' : articles[1:],
        # 'form' : form,
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

@login_required
def logout_view(request):
    logout(request)
    messages.success(request , "Successfully logged out!")

    return redirect('index')

# def register(request):

#     return render(request , 'index.html' , context)


# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request , "Account created for {0}. Please login!".format(username))
#             return redirect('login')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'users/register.html' , {'form': form})    





















# def get_user():
#     mydb = sqlite3.connect("db.sqlite3")
#     mycursor = mydb.cursor()  
#     res = mycursor.execute('SELECT username FROM auth_user')
#     lis=[]
#     for i in res:
#         lis.append(i[0])
#     mydb.close()
#     return lis

# @csrf_exempt
# def login_user(request):
#     cand_usn = request.POST['UN']
#     cand_pwd = request.POST['PW']
#     user = authenticate(request, username = cand_usn, password = cand_pwd)
#     if user is not None:
#         login(request, user)
#         return redirect('/profile')
#     else: 
#         # create alert as login failed
#         return redirect('/')

# @csrf_exempt
# def signup_user(request):
    
#     new_fname = request.POST['fname']
#     new_email = request.POST['mail']
#     new_usn = request.POST['usn']
#     new_pwd = request.POST['pwd']
#     pref = []
#     cat1 = request.POST.get('cat1',False)
#     cat2 = request.POST.get('cat2',False)
#     cat3 = request.POST.get('cat3',False)
#     cat4 = request.POST.get('cat4',False)
#     cat5 = request.POST.get('cat5',False)
#     if cat1:
#         pref.append(cat1)
#     if cat2:
#         pref.append(cat2)
#     if cat3:
#         pref.append(cat3)
#     if cat4:
#         pref.append(cat4)
#     if cat5:
#         pref.append(cat5)
    
#     usn_list = get_user()
#     if(new_usn in usn_list):
#         #create alert usn not available
#         return redirect("/")
#     else:
#         user = User.objects.create_user(new_usn, email=new_email, password=new_pwd)
#         user.first_name = new_fname
#         user.save()
#         # saving preferences in preference table
#         prefs = ",".join(pref)
#         mydb = sqlite3.connect("db.sqlite3")
#         mycursor = mydb.cursor()  
#         mydb.execute("INSERT INTO preference VALUES(?,?)",(new_usn,prefs))
#         mydb.commit()
#         mydb.close()
        
#         if user is not None:
#             login(request,user)
#             return redirect('/profile')
#         else:
#             return redirect('/') 
