
from django.contrib.auth.backends import ModelBackend
from annoying.functions import get_object_or_None
from headhunters.models import Headhunter
import hashlib

class HeadhunterBackend(ModelBackend):
    def authenticate(self, email=None, password=None):
        if not email or not password:
            return None
        headhunter = get_object_or_None(Headhunter, email=email)
        if not headhunter:
            return None
        if not headhunter.check_password(password): # If user was saved through python admin, it will fail here.
            return None
        return headhunter

    def get_user(self, pk):
        headhunter = get_object_or_None(Headhunter, pk=pk)
        return headhunter