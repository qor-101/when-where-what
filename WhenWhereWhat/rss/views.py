from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, request, response
from django.template import loader
from django.contrib import messages
from django.conf import settings
from urllib.parse import urlparse

from datetime import date
import sqlite3

# Create your views here.

