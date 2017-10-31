from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def changeAccess(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')

    checked = request.POST.getlist('check')
    if not checked:
        request.user.profile.temporary_access = False
    else :
        request.user.profile.temporary_access = True

    return HttpResponseRedirect('/')

def event(request):
    event_list = models.Event.objects.order_by('date_time')[:10]
    context = {'event_list': event_list}
    return render(request, 'events/events.html', context)
