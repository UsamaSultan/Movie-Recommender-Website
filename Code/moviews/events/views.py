# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from actstream import action
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from events.models import Event
from forms import CustomAuthForm
from django.db.models import Count


# Create your views here.
def index(request):
    event_list = Event.objects.get_queryset().order_by('id')
    categories = Event.objects.values("category").annotate(Count('category')).distinct().order_by('category')
    page = request.GET.get('page', 1)
    form = CustomAuthForm()

    paginator = Paginator(event_list, 6)
    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        events = paginator.page(1)
    except EmptyPage:
        events = paginator.page(paginator.num_pages)

       
    return render(request, 'events/index.html', { 'form2':form,'events': events, 'categories':categories })


def event_detail(request, event_id):
    
    
    
    event = Event.objects.get(pk=event_id)
    
    if request.user.is_authenticated:
        action.send(request.user, verb='event_view', target=event)
    
    form = CustomAuthForm()
    return render(request, 'events/event.html', { 'form2':form,  'event': event })


def event_category(request, event_category):
    
    event_list = Event.objects.filter(category=event_category).order_by('id')
    categories = Event.objects.values("category").annotate(Count('category')).distinct().order_by('category')
    
    page = request.GET.get('page', 1)
     
    paginator = Paginator(event_list, 6)
    try:
        events = paginator.page(page)
        
    except PageNotAnInteger:
        events = paginator.page(1)
    except EmptyPage:
        events = paginator.page(paginator.num_pages)
     
    
    return render(request, 'events/index.html', { 'events': events, 'categories':categories })


def event_search(request, event_name):
    
    event_list = Event.objects.filter(title__icontains=event_name).order_by('id')
    categories = Event.objects.values("category").annotate(Count('category')).distinct().order_by('category')
    
    page = request.GET.get('page', 1)
     
    paginator = Paginator(event_list, 6)
    try:
        events = paginator.page(page)
        
    except PageNotAnInteger:
        events = paginator.page(1)
    except EmptyPage:
        events = paginator.page(paginator.num_pages)
     
    
    return render(request, 'events/index.html', { 'events': events, 'categories':categories, 'search':event_name })