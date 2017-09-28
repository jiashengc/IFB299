# from django.shortcuts import render
# from django.contrib.auth import authenticate, login
# from django.http import HttpResponse
#
# # Create your views here.
from django.contrib import auth


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")
