

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.template import loader
from events.models import Event
from forms import CustomAuthForm
from collections import defaultdict
from models import MovieData
from models import Movies
import json
import re
import requests
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.shortcuts import render

import sys
sys.path.append('E:\moviews_recommendations')

from group_rating import group_rating_matrix
from prediction import Predictor

# Create your views here.
def index(request):
    
    
    url = 'https://newsapi.org/v2/everything'
    
    params = {'q':'Movie' , 'apiKey':'1007b5cbd3c14bedbc1d0308289852e8'}
    
    r = requests.get(url = url, params = params) 
    data = r.json() 
    
    articles = data['articles']
    
    
    rating_filter = {}
    
    movies=[]
    
    movie_data_dd=defaultdict(dict)
    
    movie_data_ddd = []
    
    if request.user.is_authenticated():
        
        
        user_id = request.user.id
        
        grm = group_rating_matrix()
        ratings = grm.group_ratings(user_id)
        
        pr = Predictor()
        predictions = pr.predictTop(user_id)
        
        
        
        rating_filter = []
        
        
        for key , value in ratings.iteritems():
            if value > 3.0:
                rating_filter.append(key)
        
        
            
            
        for x in predictions:
            movie = MovieData.objects.get(movieid=x)
            if Movies.objects.filter(pk=x).exists():
                movie_data_d = Movies.objects.get(pk=x)
                
                
                m = re.search("'path': u'(.+?)',", movie_data_d.images)
                if m:
                    path = m.group(1)
                    movie_data_dd[x]['path'] = path
                
                
                
            
            
            
            movies.append(movie)
            
            
            
       
    page = request.GET.get('page', 1)
     
    paginator = Paginator(movies, 6)
    try:
        movies = paginator.page(page)
        
        
        for movie in movies:
            if movie.movieid in movie_data_dd.keys():
                movie.data = movie_data_dd[movie.movieid]
                
        
        
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)
        
    
    
    
    
    
    events = Event.objects.all()
    form2 = CustomAuthForm()
    return render(request, 'landing/index.html', {'form2':form2, 'events':events, 'ratings':rating_filter, 'movies':movies, 'movie_data': movie_data_ddd, 'articles':articles})


def search(request, s_name):
    
    
    pass