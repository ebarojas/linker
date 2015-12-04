from django.shortcuts import render

from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
# from birthdayreminder.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


from django.views.generic import View
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from unemployeds.models import Unemployed

class HeadhunterHome(View):
    def get(self,request):
        users = listing(request)
        return render_to_response('headhunter/users_slides.html', {"users": users})


def listing(request):
    user_list = Unemployed.objects.all()
    paginator = Paginator(user_list, 1)
    page = request.GET.get('page')

    try:
        vacants = paginator.page(page)
    except PageNotAnInteger:
        vacants = paginator.page(1)
    except EmptyPage:
        vacants = paginator.page(paginator.num_pages)

    return vacants


def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/main/')
    return render_to_response('login.html', context_instance=RequestContext(request))

# @login_required(login_url='/login/')
# def main(request):
#     ....