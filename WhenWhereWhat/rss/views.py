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

def toi(request):
    
    articles = []
    dx = fp.parse('https://timesofindia.indiatimes.com/rssfeedstopstories.cms')
    n = min(len(dx.entries),28)
    for i in range(n):
        a={
            'title':dx.entries[i].title,
            'url':dx.entries[i].link,
            'publishedAt':dx.entries[i].published,
            'description':dx.entries[i].summary,
        }
        articles.append(a)
    context = {
        'zero' : articles[0],
        'news' : articles[1:],
    }
    return render(request , 'toi.html' , context)

def indiatoday(request):
    
    dx = fp.parse('https://www.indiatoday.in/rss/1206584')
    articles = []
    n = min(len(dx.entries),28)
    for i in range(n):
        m = dx.entries[i].summary.find("src")
        x = dx.entries[i].summary[m:].split(" ")
        l = x[0].split('"')
        a={
            'title':dx.entries[i].title,
            'url':dx.entries[i].link,
            'published':dx.entries[i].published,
            'imgurl':l[1],
        }
        articles.append(a)
    
    context = {
        'zero' : articles[0],
        'news' : articles[1:],
    }
    
    return render(request , 'indiatoday.html' , context)

def news18(request):
    
    dx = fp.parse('https://www.news18.com/rss/india.xml')
    articles = []
    n = min(len(dx.entries),28)
    for i in range(n):
        a={
            'title':dx.entries[i].title,
            'url':dx.entries[i].link,
            'publishedAt':dx.entries[i].published,
            'urlToImage':dx.entries[i].media_content[0]['url'],
            'description':dx.entries[i].description[:100],
        }
        articles.append(a)
    
    context = {
        'zero' : articles[0],
        'news' : articles[1:],
    }
    
    return render(request , 'index.html' , context)

def unasia(request):
    
    dx = fp.parse('https://news.un.org/feed/subscribe/en/news/region/asia-pacific/feed/rss.xml')
    articles = []
    n = min(len(dx.entries),28)
    for i in range(n):
        a={
            'title':dx.entries[i].title,
            'url':dx.entries[i].link,
            'publishedAt':dx.entries[i].published,
            'urlToImage':dx.entries[i].links[1].href,
            'description':dx.entries[i].summary,
        }
        articles.append(a)
    
    context = {
        'zero' : articles[0],
        'news' : articles[1:],
    }
    
    return render(request , 'index.html' , context)
