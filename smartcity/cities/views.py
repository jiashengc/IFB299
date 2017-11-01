from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseForbidden
from django.shortcuts import HttpResponseRedirect
from django.core import serializers
from splash import models
import json

def cities(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')

    cities = models.City.objects.all()
    return render(request, 'cities/cities.html', context={
        "cities": serializers.serialize('json', cities),
    })

def city(request, cityName):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')

    foundCity = [1]
    foundCity[0] = models.City.objects.get(name=cityName)

    return render(request, 'cities/city.html', context = {
        "city": serializers.serialize('json', foundCity),
    })

def locationType(request, cityName, locationType):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')

    foundCity = [1]
    foundCity[0] = models.City.objects.get(name=cityName)
    pk = foundCity[0].pk

    if not checkPermission(locationType, request.user.profile.account_type, request):
        return HttpResponseForbidden()

    foundLocations = models.Location.objects.filter(city=pk).filter(type=locationType)

    return render(request, 'cities/locationType.html', context = {
        "city": serializers.serialize('json', foundCity),
        "locations": serializers.serialize('json', foundLocations),
    })

def location(request, cityName, locationType, location):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')

    foundCity = [1]
    foundCity[0] = models.City.objects.get(name=cityName)
    pk = foundCity[0].pk

    if not checkPermission(locationType, request.user.profile.account_type, request):
        return HttpResponseForbidden()

    foundLocation = [1]
    foundLocation[0] = models.Location.objects.get(pk=location)
    log = models.PreviousLocation(user=request.user, location=foundLocation[0])
    log.save()

    return render(request, 'cities/location.html', context = {
        "city": serializers.serialize('json', foundCity),
        "location": serializers.serialize('json', foundLocation)
    })

def compareLocations(request):

    cities = models.City.objects.all()
    locations = models.Location.objects.all()

    return render(request, 'compare_location/compare.html', context = {
        "cities": serializers.serialize('json', cities),
        "locations": serializers.serialize('json', locations),
    })


def checkPermission(locationType, accountType, request):
    if request.session['access'] == 1:
        return True

    if accountType == 'Student':
        return locationType == 'CL'\
            or locationType == 'LI'

    if accountType == 'Tourist':
        return locationType == 'HO'

    if accountType == 'Businessman':
        return locationType == 'IN'\
            or locationType == 'HO'

    return True

