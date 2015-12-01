from django.db import models
from datetime import datetime

# Create your models here.
class Match(models.Model):
    vacant = models.ForeignKey('headhunters.Vacant')
    unemployed = models.ForeignKey('unemployeds.Unemployed')
    date = models.DateTimeField(default=datetime.now)


class VacantLike(models.Model):
    vacant = models.ForeignKey('headhunters.Vacant')
    unemployed = models.ForeignKey('unemployeds.Unemployed')
    date = models.DateTimeField(default=datetime.now)


class UnemployedLike(models.Model):
    vacant = models.ForeignKey('headhunters.Vacant')
    unemployed = models.ForeignKey('unemployeds.Unemployed')
    date = models.DateTimeField(default=datetime.now)