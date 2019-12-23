from django.conf.urls import url

from . import views

urlpatterns = [
    url('home/', views.index, name='home'),
    url(r'^all_search/(?P<s_name>.*)/$', views.search, name='search'),
]