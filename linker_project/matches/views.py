# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import View
from matches.models import Match
from headhunters.models import Headhunter, Vacant
from unemployeds.models import Unemployed
from django.contrib.auth.decorators import login_required

# Create your views here.
class MatchHome(View):
    def get(self,request):

        if isinstance(request.user, Headhunter):

            matches = Match.objects.filter(vacant=Vacant.objects.filter(headhunter=request.user))

            role = 'headhunter'
        else:
            matches = Match.objects.filter(unemployed=request.user)
            role = 'unemployed'

        return render(request, 'match/home_match.html', {
            'matches': matches,
            'role': role
        })
