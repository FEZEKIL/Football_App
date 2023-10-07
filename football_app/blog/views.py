from django.shortcuts import render
from django.http import HttpResponse
import requests 
from datetime import datetime

# Create your views here.

def index(request):
    today = datetime.today().strftime('%Y-%m-%d')
    url = "https://apiv3.apifootball.com/?action=get_events&from=2023-04-05&to=2023-04-05&league_id=152&APIkey=9b622f7d1cba87ae4e6dcc24827bd27db9f031d4c51c527c24f76a1545722894"
    #url = "https://apiv3.apifootball.com/?action=get_events&from="+today+"&to"+today+"&league_id=152&APIkey=9b622f7d1cba87ae4e6dcc24827bd27db9f031d4c51c527c24f76a1545722894"
    response = requests.get(url)
    jsonResponse = response.json()
    return render(request, 'blog/index.html', {'jsonResponse':jsonResponse})

def specific(request):
    return HttpResponse('This is the specific url')


    