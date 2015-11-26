from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField(max_length=320)
    phone = models.CharField(max_length=320)
    location_lat = models.FloatField()
    location_lon = models.FloatField()
    role = models.IntegerField(choices=role_choices, default=1)

    USERNAME_FIELD = 'email'

    class Meta:
        abstract = True