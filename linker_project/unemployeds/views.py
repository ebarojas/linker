# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic import View
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from headhunters.models import Vacant
from matches.models import UnemployedLike
from unemployeds.models import Unemployed


class UnemployedSignup (View):
    def get(self, request):
        form = Signup()
        return render(request, 'unemployed/signup.html', {'form': form})


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
