from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^events/', views.index, name='events'),
    url(r'^event/(?P<event_id>\d+)/$', views.event_detail, name='event_detail'),
    url(r'^event_category/(?P<event_category>.*)/$', views.event_category, name='event_category'),
    url(r'^event_search/(?P<event_name>.*)/$', views.event_search, name='event_search'),
]