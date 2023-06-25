from django.http import HttpResponse
from django.shortcuts import render

data = {'movies':[
    {"id": 1, 'title': "hrllo", 'year':"1899"},
    {"id": 2, 'title': "yello", 'year':"1999"},
    {"id": 3, 'title': "reddo", 'year':"1809"},
]}

def movies(request):
    return render(request, 'movies/movies.html', data)

def home(request):
    return HttpResponse("Home Page")