# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.forms import AuthenticationForm
from forms import CustomAuthForm

from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.apps import apps
import re
import requests 
import json
import mysqlx

from actstream import action

from collections import defaultdict

# Create your views here.
def index(request):
    
    MovieData = apps.get_model('landing', 'MovieData')
    Movies = apps.get_model('landing', 'Movies')
    movies = MovieData.objects.filter()
    
    size = len(movies)
    
    movie_genres_dict = defaultdict(int)
    
    for movie in movies:
        movie_genre_string = movie.genres
        movie_genres = movie_genre_string.split("|")
        
        for movie_genre in movie_genres:
            movie_genres_dict[movie_genre] += 1
           
        
    print movie_genres_dict
    page = request.GET.get('page', 1)
     
    paginator = Paginator(movies, 6)
    try:
        movies = paginator.page(page)
        
        for movie in movies:
            movie_data = Movies.objects.get(pk=movie.movieid)
            
            m = re.search("'path': u'(.+?)',", movie_data.images)
            if m:
                path = m.group(1)
                movie.path = path
            
        
        
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)
    
    
    form = CustomAuthForm()
    return render(request, 'movies/index.html', {'form2':form , 'movies':movies , 'size':size, 'gsize': dict(movie_genres_dict) })


def movie_single(request, movie_id):
    
    
    
    
    
    
    
    
    Movies = apps.get_model('landing', 'Movies')
    MovieData = apps.get_model('landing', 'MovieData')
    movie_data = Movies.objects.get(pk=movie_id)
    
    if request.user.is_authenticated:
        action.send(request.user, verb='movie_view', target=movie_data)
    
    movie_data2 = MovieData.objects.get(pk=movie_id)
    
    m = re.search("'path': u'(.+?)',", movie_data.images)
    if m:
        path = m.group(1)
        movie_data.path = path
    
    movie_data.title = movie_data2.title
    
    

    url = 'https://www.googleapis.com/youtube/v3/search'
    
    params = {'part':'snippet', 'maxResults':'1', 'q':movie_data.title + ' Trailer' , 'key':'AIzaSyCV1fQD2VC6HoNbuuSPkE0q_QZvDf117PY'}
    
    r = requests.get(url = url, params = params) 
    data = r.json() 
    
    movie_data.trailer = data['items'][0]['id']['videoId']
    
    movie_data.genres = movie_data2.genres
    
    movie_data.writers = movie_data.writers.replace("u'","")
    movie_data.writers = re.sub('[^A-Z,a-z0-9]+', ' ', movie_data.writers)
    
    movie_data.description = movie_data.description.replace("u\"","").replace("u'","")
    movie_data.description = re.sub('[^A-Z,\'a-z0-9]+', ' ', movie_data.description).strip()
    
    movie_data.stars = movie_data.stars.replace("u'","")
    movie_data.stars = re.sub('[^A-Z,a-z0-9]+', ' ', movie_data.stars)
    
    movie_data.director = movie_data.director.replace("u'","")
    movie_data.director = re.sub('[^A-Z,a-z0-9]+', ' ', movie_data.director)
    
    movie_data.runtime = movie_data.runtime.replace("u'","")
    movie_data.runtime = re.sub('[^A-Z,a-z0-9]+', ' ', movie_data.runtime).strip()
    
    
    form = CustomAuthForm()
    return render(request, 'movies/movie_s.html', {'form2':form , 'data': movie_data })

def movie_category(request, movie_category):
    
    
    
    MovieData = apps.get_model('landing', 'MovieData')
    Movies = apps.get_model('landing', 'Movies')
    movies_all = MovieData.objects.filter()
    
    movies = MovieData.objects.filter(genres__contains=movie_category)
    
    
    
    size = len(movies_all)
    
    movie_genres_dict = defaultdict(int)
    
    for movie in movies:
        movie_genre_string = movie.genres
        movie_genres = movie_genre_string.split("|")
        
        for movie_genre in movie_genres:
            movie_genres_dict[movie_genre] += 1
           
        
    print movie_genres_dict
    page = request.GET.get('page', 1)
     
    paginator = Paginator(movies, 6)
    try:
        movies = paginator.page(page)
        
        for movie in movies:
            
            try:
                movie_data = Movies.objects.get(pk=movie.movieid)
            except Movies.DoesNotExist:
                movie_data = None
            
            
            if movie_data != None:
            
                m = re.search("'path': u'(.+?)',", movie_data.images)
                if m:
                    path = m.group(1)
                    movie.path = path
            
        
        
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)
    
    
    form = CustomAuthForm()
    return render(request, 'movies/index.html', {'form2':form , 'movies':movies , 'size':size, 'gsize': dict(movie_genres_dict) })
    
    
def movie_search(request, movie_name):
    
    
    MovieData = apps.get_model('landing', 'MovieData')
    Movies = apps.get_model('landing', 'Movies')
    
    
    movies = MovieData.objects.filter(title__icontains=movie_name).order_by('movieid')
    
    
    
    
    
    
    size = len(movies)
    
    movie_genres_dict = defaultdict(int)
    
    for movie in movies:
        movie_genre_string = movie.genres
        movie_genres = movie_genre_string.split("|")
        
        for movie_genre in movie_genres:
            movie_genres_dict[movie_genre] += 1
    
    
    
    
    page = request.GET.get('page', 1)
     
    paginator = Paginator(movies, 6)
    try:
        movies = paginator.page(page)
        
        for movie in movies:
            movie_data = Movies.objects.get(pk=movie.movieid)
            
            m = re.search("'path': u'(.+?)',", movie_data.images)
            if m:
                path = m.group(1)
                movie.path = path
            
        
        
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)
     
    
    return render(request, 'movies/index.html', {'movies':movies, 'search':movie_name, 'movies':movies , 'size':size, 'gsize': dict(movie_genres_dict) })
    
    
def add_rating(request, rating, movie_id):
    
    session = mysqlx.get_session({
    'host': 'localhost',
    'port': 33060,
    'user': 'root',
    'password': 'abcd123'
})


    schema = session.get_schema('moviews')

    ratings = schema.get_table('user_ratings')
    
    uid = request.user.id
    
    
    row = ratings.insert('userId','movieId','rating').values(int(uid),int(movie_id),int(rating)).execute()
    
    return HttpResponse('200')