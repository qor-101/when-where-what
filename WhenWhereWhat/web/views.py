from django.shortcuts import render
import requests
from .services import get_all_indian_news
from django.http import HttpResponse


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


