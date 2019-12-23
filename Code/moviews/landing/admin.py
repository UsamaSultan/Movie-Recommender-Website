# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import MovieData
from models import Movies


class MovieDataAdmin(admin.ModelAdmin):
    
    search_fields = ('title',)
    
class MoviesAdmin(admin.ModelAdmin):
    
    search_fields = ('movie_id',)


# Register your models here.

admin.site.register(MovieData, MovieDataAdmin)
admin.site.register(Movies, MoviesAdmin)