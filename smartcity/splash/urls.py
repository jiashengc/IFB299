from django.conf.urls import url
from splash import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
