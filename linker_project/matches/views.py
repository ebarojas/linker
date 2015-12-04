# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class MatchHome(View):
    def get(self,request):
        return render(request, 'match/home_match.html')
