# -*- encoding: utf-8 -*-
from django.shortcuts import render, render_to_response, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import View
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from headhunters.models import Vacant
from matches.models import VacantLike, Match
from headhunters.forms import Signup

from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.template.context_processors import csrf

from headhunters.models import Headhunter
from unemployeds.models import Unemployed

class HeadhunterSignup(View):
    def get(self, request):
        form = Signup()
        return render(request, 'headhunter/signup.html', {'form': form})

    def post(self, request):
        logout(request) #not sure if necessary
        form = Signup(request.POST)

        if form.is_valid():
            form_commit = form.save(commit=False)
            form_commit.set_password(request.POST.get('password'))
            form_commit.save()
            # Login user
            username = request.POST['email']
            password = request.POST['password']

            user = authenticate(email=username, password=password)
            login(request, user)
            if isinstance(user, Headhunter):
                return HttpResponseRedirect('/users/')
            elif isinstance(user, Unemployed):
                return HttpResponseRedirect('/vacants/')
            else:
                return HttpResponseRedirect('/login/')

            return redirect(reverse('headhunter_home'))

        return render(request, 'headgunter/signup.html', {'form': form})



class HeadhunterHome(View):
    def get(self,request):
        users = listing(request)
        return render(request, 'headhunter/users_slides.html', {"users": users})

    def post(self, request):
        vacant = Vacant.objects.get(headhunter=request.user)
        user = Unemployed.objects.get(id=request.POST.get('userId'))
        like = VacantLike(vacant=vacant, unemployed=user)
        like.save()

        users = listing(request)
        if users.has_next():
            return render(request, 'headhunter/users_slides.html', {"users": users})
        else:
            return render(request, 'headhunter/users_slides.html', {"users": users})

class VacantPublic(View):
    def get(self, request, *args, **kwargs):
        user = Unemployed.objects.get(id=request.user.id)
        exists_match = self.validate_match(kwargs['vacant_id'], user)

        if not exists_match:
            return redirect('/vacants/')

        vacant = Vacant.objects.get(id=kwargs['vacant_id'])
        return render(request, 'headhunter/vacant_public_profile.html', {
            "vacant": vacant
        })


    def validate_match(self, vacant_id, user):
        try:
            vacant = Vacant.objects.get(id=vacant_id)
            match = Match.objects.get(unemployed=user, vacant=vacant)
        except Exception as e:
            return False

        return True



@login_required(login_url='/login/')
def listing(request):
    user_list = Unemployed.objects.all()
    paginator = Paginator(user_list, 1)
    page = request.GET.get('page') if request.GET.get('page') else request.POST.get('page')

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
        user = authenticate(email=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if isinstance(user, Headhunter):
                    return HttpResponseRedirect('/users/')
                elif isinstance(user, Unemployed):
                    return HttpResponseRedirect('/vacants/')
                else:
                    return HttpResponseRedirect('/login/')
    return render_to_response('login.html', context_instance=RequestContext(request))


def logout_user(request):
    logout(request)
    return redirect('/login/')

def home(request):
    if isinstance(request.user, Headhunter):
        return HttpResponseRedirect('/users/')
    elif isinstance(request.user, Unemployed):
        return HttpResponseRedirect('/vacants/')
