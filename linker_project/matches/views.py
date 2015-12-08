# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import View
from .models import Match
from headhunters.models import Headhunter
from unemployeds.models import Unemployed

# Create your views here.

class MatchHome(View):
    def get(self,request):
        matches = Match.objects.all()
        return render(request, 'match/home_match.html', {'matches': matches})
