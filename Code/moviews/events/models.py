# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from simple_history.models import HistoricalRecords

from django.db import models

# Create your models here.
class Event(models.Model):
    id = models.AutoField(primary_key='True')
    title = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    runtime = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()
    image_url = models.CharField(max_length=500)
    history = HistoricalRecords()
    
    
    def __unicode__(self):
        return self.title