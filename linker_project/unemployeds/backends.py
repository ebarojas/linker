
from django.contrib.auth.backends import ModelBackend
# from annoying.functions import get_object_or_None
from unemployeds.models import Unemployed
import hashlib

class UnemployedBackend(ModelBackend):
    def authenticate(self, email=None, password=None):
        if not email or not password:
            return None

        # unemployed = get_object_or_None(Unemployed, email=email)

        unemployed = Unemployed.objects.get(email=email)

        print 'result unempl'+unemployed
        # return None if unemployed == None

        if not unemployed:
            return None

        if not unemployed.check_password(password):
             return None

        return unemployed

    def get_user(self, pk):
        unemployed = get_object_or_None(Unemployed, pk=pk)
        return unemployed