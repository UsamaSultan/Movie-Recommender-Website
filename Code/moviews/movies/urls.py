from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^movies/', views.index, name='movies'),
    url(r'^movie/(?P<movie_id>\d+)/$', views.movie_single, name='movie_detail'),
    url(r'^movie_category/(?P<movie_category>.*)/$', views.movie_category, name='movie_category'),
    url(r'^movie_search/(?P<movie_name>.*)/$', views.movie_search, name='movie_search'),
    url(r'^add_rating/(?P<rating>.*)/(?P<movie_id>.*)/$', views.add_rating, name='add_rating')
]