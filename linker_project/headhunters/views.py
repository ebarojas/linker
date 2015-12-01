from django.shortcuts import render
from django.views.generic import View
#from headhunter.models import
# Create your views here.

class HeadhunterHome(View):
    def get(self,request):
        return render(request, 'headhunter/users_slides.html')
