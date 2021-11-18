import os
import requests



# def get_droplets():
#     url = 'https://api.digitalocean.com/v2/droplets'
#     r = requests.get(url, headers={'Authorization':'Bearer %s' % 'access_token'})
#     droplets = r.json()
#     droplet_list = []
#     for i in range(len(droplets['droplets'])):
#         droplet_list.append(droplets['droplets'][i])
#     return droplet_list

def get_all_indian_news():

    url = "https://indian-news-live.p.rapidapi.com/news"

    headers = {
    'x-rapidapi-host': "indian-news-live.p.rapidapi.com",
    'x-rapidapi-key': "fd72cb71a9msh1fa6a2791e31886p1c79aejsne23a14ea8bd6"
    }

    response = requests.get(url, headers={'X-RapidAPI-Host' : "indian-news-live.p.rapidapi.com" % "fd72cb71a9msh1fa6a2791e31886p1c79aejsne23a14ea8bd6"})

    return(response.text)


