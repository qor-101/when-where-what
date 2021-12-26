from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, request, response
from django.template import loader
from django.contrib import messages
from django.conf import settings
from urllib.parse import urlparse

from datetime import date
import sqlite3
import feedparser as fp

# Create your views here.

def returns_a_list_of_news_articles_given_a_rss_link(rss_link_str):
    
    dx = fp.parse(rss_link_str)
    list_of_articles = []
    n = min(len(dx.entries),30)
    for i in range(n):
        a={
            'title':dx.entries[i].title,
            'url':dx.entries[i].link,
            'published':dx.entries[i].published,
        }
        list_of_articles.append(a)
    return list_of_articles

def toi(request):
    articles = returns_a_list_of_news_articles_given_a_rss_link('https://timesofindia.indiatimes.com/rssfeedstopstories.cms')
    context = {
        'zero' : articles[0],
        'news' : articles[1:],
    }
    return render(request , 'index.html' , context)

def indiatoday(request):
    articles = returns_a_list_of_news_articles_given_a_rss_link('https://www.indiatoday.in/rss/1206584')
    context = {
        'zero' : articles[0],
        'news' : articles[1:],
    }
    return render(request , 'index.html' , context)

def etimes(request):
    articles = returns_a_list_of_news_articles_given_a_rss_link('https://economictimes.indiatimes.com/rssfeedstopstories.cms')
    context = {
        'zero' : articles[0],
        'news' : articles[1:],
    }
    return render(request , 'index.html' , context)