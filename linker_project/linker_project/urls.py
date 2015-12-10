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
from headhunters.views import HeadhunterHome, HeadhunterSignup, VacantPublic
from unemployeds.views import UnemployedHome, UnemployedSignup, UnemployedPublic
from matches.views import MatchHome
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from headhunters.views import home
from headhunters.views import login_user, logout_user
from django.contrib.auth.decorators import login_required
from users.views import Profile

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', login_user),
    url(r'^home/$', home),
    url(r'^logout/$', logout_user),
    url(r'^profile/$', Profile.as_view(), name="profile"),
    url(r'^users/$', login_required(HeadhunterHome.as_view(), login_url='/login/'), name = "headhunter_home"),
    url(r'^vacants/$', login_required(UnemployedHome.as_view(), login_url='/login/'), name = "unemployed_home"),
    url(r'^matches/$', login_required(MatchHome.as_view(), login_url='/login/'), name = "match_home"),
    url(r'^users/signup/$', UnemployedSignup.as_view(), name = "unemployed_signup"),
    url(r'^headhunters/signup/$', HeadhunterSignup.as_view(), name = "headhunter_signup"),
    url(r'^users/(?P<user_id>\d+)/$', UnemployedPublic.as_view(), name='unemployed_public'),
    url(r'^vacants/(?P<vacant_id>\d+)/$', VacantPublic.as_view(), name='vacant_public'),
]


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
