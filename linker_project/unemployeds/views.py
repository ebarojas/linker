from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic import View

from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
# from headhunters.models import Headhunter # Maybe remove this
from headhunters.models import Vacant

class UnemployedHome(View):
    def get(self,request):
        vacants = listing(request)
        return render_to_response('unemployed/vacants_slide.html', {"vacants": vacants})

def listing(request):
    vacant_list = Vacant.objects.all()
    paginator = Paginator(vacant_list, 1) # Show 1 contacts per page

    page = request.GET.get('page')
    try:
        vacants = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        vacants = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        vacants = paginator.page(paginator.num_pages)

    return vacants