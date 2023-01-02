from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name   = models.CharField(max_length=50)
    last_name    = models.CharField(max_length=50)
    username     = models.CharField(max_length=127, unique=True)
    email        = models.CharField(max_length=127, unique=True)
    password     = models.CharField(max_length=127)