"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from splash import views as splashviews
from django.contrib import auth

urlpatterns = [
    url(r'^$', splashviews.index, name='index'),
    url(r'^admin/', admin.site.urls, name='adminDash'),
    url(r'^login/', include('login.urls')),
    url(r'^hotel/', include('hotel.urls')),
    url(r'^register/', include('register.urls')),
    url(r'^cities/', include('cities.urls')),
    url(r'^profile/', include('profile.urls')),
    url(r'^logout/', include('logout.urls')),
    url(r'^change-access/', splashviews.changeAccess, name='change-access'),
    url(r'^events/', splashviews.event, name='events'),
]
