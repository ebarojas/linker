# -*- encoding: utf-8 -*-
from django.db import models
from users.models import User
from datetime import datetime


class Headhunter(User):
    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Vacant(models.Model):
    headhunter = models.ForeignKey('headhunters.Headhunter')
    posted_date = models.DateTimeField(default=datetime.now)
    location = models.CharField(max_length=80)
    location_lat = models.FloatField(default=0)
    location_lon = models.FloatField(default=0)
    name = models.CharField(max_length=320)
    salary = models.FloatField()
    headline = models.CharField(max_length=255)
    details = models.CharField(max_length=500)
    picture = models.ImageField(upload_to='vacants_pics')

    def __str__(self):
        return self.name
