from django.conf.urls import url

from . import views

urlpatterns = [
    url('signup/', views.signup, name='signup'),
    url(r'^ce/(?P<email>.*)/$', views.ce, name='ce'),
]