# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.forms import AuthenticationForm
from forms import CustomAuthForm

from actstream import action

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Celebs
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import re




# Create your views here.
def index(request):
    
    
    
    celebs = Celebs.objects.get_queryset()
    
    page = request.GET.get('page', 1)
    

    paginator = Paginator(celebs, 9)
    try:
        celebs = paginator.page(page)
        
        
            
            
            
            
            
            
        
    except PageNotAnInteger:
        celebs = paginator.page(1)
    except EmptyPage:
        celebs = paginator.page(paginator.num_pages)
    
    form = CustomAuthForm()
    return render(request, 'celebs/index.html', {'form2':form, 'celebs':celebs})

def celeb_letter(request, letter):
    
    
    search_query = " " + letter.upper()
    celebs = Celebs.objects.filter(name__startswith=search_query)
    
    
    page = request.GET.get('page', 1)
    

    paginator = Paginator(celebs, 9)
    try:
        celebs = paginator.page(page)
        
        for celeb in celebs:
            celeb.name = celeb.name.replace('\\n','')
            
            
            
            celeb.name = re.sub('[^A-Za-z0-9]+', ' ', celeb.name)
            
            
            
            celeb.description = celeb.description.replace('"','')
            
            
            celeb.description = celeb.description.replace(', ,','')
            
            celeb.description = celeb.description.replace('[','')
            celeb.description = celeb.description.replace(']','')
            
            celeb.description = celeb.description.replace('\\n','')
            
            
           
            
            
            
            
            
        
    except PageNotAnInteger:
        celebs = paginator.page(1)
    except EmptyPage:
        celebs = paginator.page(paginator.num_pages)
    
    
    
    form = CustomAuthForm()
    return render(request, 'celebs/index.html', {'form2':form, 'celebs':celebs})


def celeb_search(request, celeb_name):
    
    
    celebs = Celebs.objects.filter(name__icontains=celeb_name).order_by('id')
    
    page = request.GET.get('page', 1)
    

    paginator = Paginator(celebs, 9)
    try:
        celebs = paginator.page(page)
        
        
            
            
            
            
            
            
        
    except PageNotAnInteger:
        celebs = paginator.page(1)
    except EmptyPage:
        celebs = paginator.page(paginator.num_pages)
    
    form = CustomAuthForm()
    return render(request, 'celebs/index.html', {'form2':form, 'celebs':celebs})
    
    
    
def view_celeb(request, cid):
    
    
    celeb = Celebs.objects.get(pk=cid)
    action.send(request.user, verb='celeb_view', target=celeb)
    
    return True
 
    