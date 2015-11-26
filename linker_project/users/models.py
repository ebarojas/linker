from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField(max_length=320)
    # profile_picture = models.ImageField()
    phone = models.CharField(max_length=320)
    location = models.CharField(max_length=320)

    USERNAME_FIELD = 'email'

    class Meta:
        abstract = True