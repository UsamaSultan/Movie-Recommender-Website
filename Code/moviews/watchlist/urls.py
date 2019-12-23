from django.conf.urls import url

from . import views

urlpatterns = [
    url('watchlist/', views.index, name='watchlist'),
    
   
    
    
]