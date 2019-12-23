# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Movies(models.Model):
    movie_id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=2000, blank=True, null=True)
    writers = models.CharField(max_length=2000, blank=True, null=True)
    stars = models.CharField(max_length=2000, blank=True, null=True)
    director = models.CharField(max_length=2000, blank=True, null=True)
    runtime = models.CharField(max_length=2000, blank=True, null=True)
    images = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movies'
