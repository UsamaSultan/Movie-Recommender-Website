# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    # add additional fields in here
    
    username = models.CharField(max_length=100, unique='true')
    email = models.EmailField(unique='true')
    first_name = models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
   

    def __str__(self):
        return self.email