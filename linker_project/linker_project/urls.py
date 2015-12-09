"""linker_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from headhunters.views import HeadhunterHome
from unemployeds.views import UnemployedHome
from matches.views import MatchHome
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from headhunters.views import login_user
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/$', login_required(HeadhunterHome.as_view(), login_url='/login/'), name = "headhunter_home"),
    url(r'^vacants/$', login_required(UnemployedHome.as_view(), login_url='/login/'), name = "unemployed_home"),
    url(r'^matches/$', login_required(MatchHome.as_view(), login_url='/login/'), name = "match_home"),
    url(r'^login/$', login_user),
]


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)