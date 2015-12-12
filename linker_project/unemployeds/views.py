# -*- encoding: utf-8 -*-
from django.shortcuts import render, render_to_response, redirect
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from headhunters.models import Vacant
from headhunters.models import Headhunter
from matches.models import UnemployedLike, Match
from unemployeds.models import Unemployed
from unemployeds.forms import Signup
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.template.context_processors import csrf
from django.template import RequestContext
from django.http import HttpResponseRedirect

class UnemployedSignup(View):
    def get(self, request):
        form = Signup()
        return render(request, 'unemployed/signup.html', {'form': form})

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
            # raise error
            return redirect(reverse('unemployed_home'))

        return render(request, 'unemployed/signup.html', {'form': form})




class UnemployedHome(View):
    def get(self,request):
        vacants = listing(request)
        return render(request, 'unemployed/vacants_slide.html', {"vacants": vacants})

    def post(self, request):
        user = Unemployed.objects.get(id=request.user.id)
        vacant = Vacant.objects.get(id=request.POST.get('vacantId'))
        like = UnemployedLike(vacant=vacant, unemployed=user)
        like.save()

        vacants = listing(request)
        return render(request, 'unemployed/vacants_slide.html', {"vacants": vacants})


class UnemployedPublic(View):
    def get(self, request, *args, **kwargs):
        vacant = Vacant.objects.filter(headhunter=request.user)[:1]
        exists_match = self.validate_match(kwargs['user_id'], vacant)
        print(vacant)
        if not exists_match:
            return redirect(reverse("match_home"))

        user = Unemployed.objects.get(id=kwargs['user_id'])
        return render(request, 'unemployed/public_profile.html', {
            "user": user
        })


    def validate_match(self, user_id, vacant):
        try:
            user = Unemployed.objects.get(id=user_id)
            match = Match.objects.get(unemployed=user, vacant=vacant)
            print(user)
            match.new = False
            match.save()
        except Exception as e:
            return False

        return True


@login_required(login_url='/login/')
def listing(request):
    vacant_list = Vacant.objects.all()
    paginator = Paginator(vacant_list, 1)
    page = request.GET.get('page') if request.GET.get('page') else request.POST.get('page')

    try:
        vacants = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        vacants = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        vacants = paginator.page(paginator.num_pages)
    return vacants
