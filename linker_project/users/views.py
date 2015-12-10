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
            form = HeadhunterProfile(instance=request.user)
        else:
            form = UnemployedProfile(instance=request.user)

        return render(request, 'user/edit_profile.html', {'form': form})

    def post(self, request):
        if isinstance(request.user, Headhunter):
            form = HeadhunterProfile(request.POST, instance=request.user)
        else:
            form = UnemployedProfile(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return render(request, 'user/edit_profile.html', {
                'form': form,
                'updated': True
            })

        return render(request, 'user/edit_profile.html', {'form': form})
