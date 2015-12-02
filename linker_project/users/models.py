from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField(max_length=320)
    phone = models.CharField(max_length=10)
    location_lat = models.FloatField()
    location_lon = models.FloatField()
    linkedin_id = models.CharField(max_length=255)
    headline = models.CharField(max_length=255)
    num_connections = models.IntegerField()
    picture_url = models.CharField(max_length=320)

    USERNAME_FIELD = 'email'

    class Meta:
        abstract = True