from django.db import models
from users.models import User
from datetime import datetime

# Create your models here.
class Headhunter(User):
    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Vacant(models.Model):
    headhunter = models.ForeignKey('headhunters.Headhunter')
    posted_date = models.DateTimeField(default=datetime.now)
    location_lat = models.FloatField()
    location_lon = models.FloatField()
    name = models.CharField(max_length=320)
    salary = models.FloatField()
    details = models.CharField(max_length=500)
    picture = models.ImageField()

    def __str__(self):
        return self.name