# -*- encoding: utf-8 -*-
from django.db import models
from datetime import datetime

# Create your models here.
class Match(models.Model):
    vacant = models.ForeignKey('headhunters.Vacant')
    unemployed = models.ForeignKey('unemployeds.Unemployed')
    date = models.DateTimeField(default=datetime.now)
    new = models.BooleanField(default=True)


class VacantLike(models.Model):
    vacant = models.ForeignKey('headhunters.Vacant')
    unemployed = models.ForeignKey('unemployeds.Unemployed')
    date = models.DateTimeField(default=datetime.now)

    def save(self, *args, **kwargs):
        unemployed_like = UnemployedLike.objects.filter(
            vacant=self.vacant,
            unemployed=self.unemployed
        )

        if unemployed_like:
            match = Match(vacant=self.vacant, unemployed=self.unemployed)
            match.save()

        super(VacantLike, self).save(*args, **kwargs)



class UnemployedLike(models.Model):
    vacant = models.ForeignKey('headhunters.Vacant')
    unemployed = models.ForeignKey('unemployeds.Unemployed')
    date = models.DateTimeField(default=datetime.now)

    def save(self, *args, **kwargs):
        vacant_like = VacantLike.objects.filter(
            vacant=self.vacant,
            unemployed=self.unemployed
        )

        if vacant_like:
            match = Match(vacant=self.vacant, unemployed=self.unemployed)
            match.save()

        super(UnemployedLike, self).save(*args, **kwargs)
