from django.shortcuts import render
from django.views.generic import View


class UnemployedHome(View):
    def get(self,request):
        return render(request, 'unemployed/vacants_slide.html')
