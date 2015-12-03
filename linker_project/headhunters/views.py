from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic import View
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from unemployeds.models import Unemployed

class HeadhunterHome(View):
    def get(self,request):
        users = listing(request)
        return render_to_response('headhunter/users_slides.html', {"users": users})


def listing(request):
    user_list = Unemployed.objects.all()
    paginator = Paginator(user_list, 1)
    page = request.GET.get('page')

    try:
        vacants = paginator.page(page)
    except PageNotAnInteger:
        vacants = paginator.page(1)
    except EmptyPage:
        vacants = paginator.page(paginator.num_pages)

    return vacants
