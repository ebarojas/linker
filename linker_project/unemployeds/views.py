# -*- encoding: utf-8 -*-
from django.shortcuts import render, render_to_response, redirect
from django.views.generic import View
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from headhunters.models import Vacant
from matches.models import UnemployedLike, Match
from unemployeds.models import Unemployed

class UnemployedHome(View):
    def get(self,request):
        vacants = listing(request)
        return render(request, 'unemployed/vacants_slide.html', {"vacants": vacants})

    def post(self, request):
        user = Unemployed.objects.get(id=2) # Cambiar por sesion de usuario
        vacant = Vacant.objects.get(id=request.POST.get('vacantId'))
        like = UnemployedLike(vacant=vacant, unemployed=user)
        like.save()

        vacants = listing(request)
        return render(request, 'unemployed/vacants_slide.html', {"vacants": vacants})



class UnemployedPublic(View):
    def get(self, request, *args, **kwargs):
        vacant = Vacant.objects.get(id=2) # Cambiar por sesion de usuario
        exists_match = self.validate_match(kwargs['user_id'], vacant)

        if not exists_match:
            return redirect('/users/')

        user = Unemployed.objects.get(id=kwargs['user_id'])
        return render(request, 'unemployed/public_profile.html', {
            "user": user
        })


    def validate_match(self, user_id, vacant):
        try:
            user = Unemployed.objects.get(id=user_id)
            match = Match.objects.get(unemployed=user, vacant=vacant)
        except Exception as e:
            return False

        return True



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
