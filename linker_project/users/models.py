# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    default_pic = "http://www.komarketingassociates.com/images/2014/08/linkedin-default.png"

    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField(max_length=320)
    phone = models.CharField(max_length=10, default="")
    location = models.CharField(max_length=80, default="")
    location_lat = models.FloatField(default=0)
    location_lon = models.FloatField(default=0)
    linkedin_id = models.CharField(max_length=255)
    headline = models.CharField(max_length=255, default="")
    num_connections = models.IntegerField(default=0)
    picture_url = models.CharField(max_length=320, default=default_pic)

    USERNAME_FIELD = 'email'

    class Meta:
        abstract = True
