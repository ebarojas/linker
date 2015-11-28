from django.db import models
from datetime import datetime

# Create your models here.
class Match(models.Model):
    vacant = models.ForeignKey('headhunter.Vacant')
    unemployed = models.ForeignKey('unemployed.Unemployed')
    date = models.DateTimeField(default=datetime.now)


class VacantLike(models.Model):
    vacant = models.ForeignKey('headhunter.Vacant')
    unemployed = models.ForeignKey('unemployed.Unemployed')
    date = models.DateTimeField(default=datetime.now)


class UnemployedLike(models.Model):
    headhunter = models.ForeignKey('headhunter.Headhunter')
    unemployed = models.ForeignKey('unemployed.Unemployed')
    date = models.DateTimeField(default=datetime.now)