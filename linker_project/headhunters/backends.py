
from django.contrib.auth.backends import ModelBackend
# from annoying.functions import get_object_or_None
from headhunters.models import Headhunter
import hashlib

class HeadhunterBackend(ModelBackend):
    def authenticate(self, email=None, password=None):
        print 'this is headhunter backend'
        if not email or not password:
            return None


        headhunter = Headhunter.objects.get(email=email)
        print headhunter
        # return None if not headhunter


        # headhunter = get_object_or_None(Headhunter, email=email)

        if not headhunter:
            return None

        if not headhunter.check_password(password):
            print headhunter.check_password(password)
            print '2   '+password
            return None
        print 'antes del return'
        return headhunter

    def get_user(self, pk):
        headhunter = get_object_or_None(Headhunter, pk=pk)
        return headhunter