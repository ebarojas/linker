from users.models import User
from django.db import models

# Create your models here.
class Unemployed(User):
    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
