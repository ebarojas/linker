# -*- encoding: utf-8 -*-
from django.shortcuts import render, redirect
from django.views.generic import View
from users.forms import HeadhunterProfile, UnemployedProfile
from headhunters.models import Headhunter
from unemployeds.models import Unemployed

# Create your views here.
class Profile(View):
    def get(self, request):
        if isinstance(request.user, Headhunter):
            form = HeadhunterProfile()
        else:
            form = UnemployedProfile()

        return render(request, 'user/edit_profile.html', {'form': form})

    def post(self, request):
        if isinstance(request.user, Headhunter):
            form = HeadhunterProfile(request.POST)
        else:
            form = UnemployedProfile(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/home')

        return render(request, 'user/edit_profile.html', {'form': form})
