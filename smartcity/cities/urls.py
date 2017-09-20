from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.cities, name='cities'),
    url(r'^(?P<cityName>[a-zA-Z]+)/$', views.city, name='city'),
    url(r'^(?P<cityName>[a-zA-Z]+)/(?P<locationType>[a-zA-Z]+)/$', views.locationType, name='locationType')
]
