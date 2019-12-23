from django.conf.urls import url

from . import views

urlpatterns = [
    url('celebs/', views.index, name='celebs'),
    url(r'^celebs_list/(?P<letter>.*)/$', views.celeb_letter, name='celeb_letter'),
    url(r'^celeb_search/(?P<celeb_name>.*)/$', views.celeb_search, name='celeb_search'),
    url(r'^celeb_view/(?P<cid>\d+)/$', views.view_celeb, name='view_celeb'),
   
    
    
]