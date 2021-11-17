from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, request
from django.template import loader
from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from datetime import date
import sqlite3

# Create your views here.

@csrf_exempt
def index(request):
    return render(request,"homepage.html")

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
