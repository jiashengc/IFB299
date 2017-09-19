from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.cities, name='cities'),
    url('([a-zA-Z]+)', views.city, name='city')
]
