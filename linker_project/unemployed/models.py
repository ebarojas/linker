from users.models import User
from django.db import models

# Create your models here.
class Unemployed(User):
    linkedin_id = models.CharField(max_length=255)
    headline = models.CharField(max_length=255)
    num_connections = models.IntegerField()
    picture_url = models.CharField(max_length=320)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
