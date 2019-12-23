# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

# Create your models here.
class Movie(models.Model):
    id = models.AutoField(primary_key='True')
    title = models.CharField(max_length=100, blank=False)
    movie_data = models.ForeignKey('landing.MovieData')
    
    
    def __unicode__(self):
        return self.title
    
class Genre(models.Model):
    movie = models.ForeignKey(Movie, related_name='genres')
    genre = models.CharField(max_length=100)
    
