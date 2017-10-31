from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session

# Create your views here.
def index(request):
    return render(request, 'index.html')

def changeAccess(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')

    checked = request.POST.get('access', '')

    # if checked not in ['yes']:
    #     user.profile.temporary_access = False
    # else:
    #     user.profile.temporary_access = True
    #
    # user.profile.temporary_access = Tr
    # user.profile.save()
    # user.save()
    if checked not in ['yes']:
        request.session['access'] = 0
        # s.access = False
    else:
        request.session['access'] = 1
        # s.access = True

    request.session['access'] = 1

    request.session.modified = True

    return HttpResponseRedirect('/cities')
