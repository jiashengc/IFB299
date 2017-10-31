from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseForbidden
from django.shortcuts import HttpResponseRedirect
from django.core import serializers
from splash import models
import json


def profile(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')

    profile = models.Profile.objects.all()
    return render(request, 'profiles/profile.html', context={
        "profile": serializers.serialize('json', profile),
    })