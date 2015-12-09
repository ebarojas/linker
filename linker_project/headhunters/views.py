# -*- encoding: utf-8 -*-
from django.shortcuts import render, render_to_response, redirect
from django.views.generic import View
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from unemployeds.models import Unemployed
from headhunters.models import Vacant
from matches.models import VacantLike, Match

class HeadhunterHome(View):
    def get(self,request):
        users = listing(request)
        return render(request, 'headhunter/users_slides.html', {"users": users})

    def post(self, request):
        vacant = Vacant.objects.get(id=1) # Cambiar por sesion de usuario
        user = Unemployed.objects.get(id=request.POST.get('userId'))
        like = VacantLike(vacant=vacant, unemployed=user)
        like.save()

        users = listing(request)
        return render(request, 'headhunter/users_slides.html', {"users": users})


class VacantPublic(View):
    def get(self, request, *args, **kwargs):
        user = Unemployed.objects.get(id=2) # Cambiar por sesion de usuario
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



def listing(request):
    user_list = Unemployed.objects.all()
    paginator = Paginator(user_list, 1)
    page = request.GET.get('page') if request.GET.get('page') else request.POST.get('page')

    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return users
