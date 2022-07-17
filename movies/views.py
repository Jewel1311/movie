from django.shortcuts import render,redirect
from .settings import API_KEY
import json
import requests
from django.contrib import messages


def search_movie(request):
    if request.method == "POST":
        name = request.POST['movie']
        if name is "":
            messages.warning(request, f"Please Provide a name")
        else:
            return redirect('movie_view', name=name)
    return render(request, 'movies/index.html')

def movie_view(request, name):
    details = requests.get(f"https://imdb-api.com/API/SearchMovie/{API_KEY}/{name}").json()
    count = len(details['results'])
    if count != 0:
        context = {
            'results': details['results'],
            'name': name
        } 
        return render(request, 'movies/list.html',context)
    messages.warning(request,f'No movies found')
    return render(request, 'movies/list.html')
 

def detail_view(request, id):
    return redirect(f"https://www.imdb.com/title/{id}/")