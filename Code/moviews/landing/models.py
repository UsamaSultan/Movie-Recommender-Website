# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin


class MovieData(models.Model):
    movieid = models.IntegerField(primary_key=True, db_column='movieId', blank=False)  # Field name made lowercase.
    title = models.CharField(max_length=100, blank=False, null=True)
    genres = models.CharField(max_length=1000, blank=False, null=True, default="New|", verbose_name=" Genres ( Add after ' New| ' with pipes)")
    
    def __unicode__(self):
        return self.title

    class Meta:
        managed = False
        db_table = 'movie_data'


class Movies(models.Model):
    movie_id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=2000, blank=False, null=True)
    writers = models.CharField(max_length=2000, blank=False, null=True)
    stars = models.CharField(max_length=2000, blank=False, null=True)
    director = models.CharField(max_length=2000, blank=False, null=True)
    runtime = models.CharField(max_length=2000, blank=False, null=True)
    images = models.CharField(max_length=2000, blank=False, null=True)
    
    def __unicode__(self):
        return str(self.movie_id)

    class Meta:
        managed = False
        db_table = 'movies'