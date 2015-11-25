from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    role_choices = (
        (1, 'headhunter'), 
        (2, 'unemployed'),
    )

    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField(max_length=320)
    profile_picture = models.FileField(max_length=320)
    phone = models.CharField(max_length=320)
    location = models.CharField(max_length=320)
    role = models.IntegerField(choices=role_choices, default=1)

    USERNAME_FIELD = 'email'

    class Meta:
        abstract = True