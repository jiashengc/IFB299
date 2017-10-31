# from django.shortcuts import render
# from django.contrib.auth import authenticate, login
# from django.http import HttpResponse
#
# # Create your views here.
from django.contrib import auth
from django.shortcuts import HttpResponseRedirect


def logout(request):
    auth.logout(request)
    request.session['access'] = 0
    request.session.modified = True
    return HttpResponseRedirect("/")
