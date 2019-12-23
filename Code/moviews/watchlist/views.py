# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from actstream.models import any_stream
from events.models import Event
from landing.models import MovieData
from celebs.models import Celebs



# Create your views here.

def index(request):
    
    if request.user.is_authenticated:
        movie_view = {}
        celeb_view = {}
        event_view = {}
        
        stream = any_stream(request.user)
        
        
        
        for str1 in stream:
            if str1.verb == "movie_view":
                title = MovieData.objects.get(pk=str1.target_object_id).title
                movie_view[title] = str1.timestamp
                
                
            elif str1.verb == "event_view":
                
                title = Event.objects.get(pk=str1.target_object_id).title
                event_view[title] = str1.timestamp
                
                
            elif str1.verb == "celeb_view":
                
                title = Celebs.objects.get(pk=str1.target_object_id).name
                celeb_view[title] = str1.timestamp
                
        
        return render(request, 'watchlist/index.html', {'movie_view':movie_view, 'event_view':event_view, 'celeb_view':celeb_view})
    else:
		return render(request, 'watchlist/index.html')
		