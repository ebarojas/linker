# -*- encoding: utf-8 -*-

from users.models import User
from django.db import models

# Create your models here.
class Unemployed(User):
    resume = models.CharField(max_length=500)

    #def __unicode__(self):
    #    return "{} {}".format(self.first_name, self.last_name)
