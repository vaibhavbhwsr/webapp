from django.contrib.auth.models import AbstractUser
from django.db import models  # noqa: F401


class User(AbstractUser):
    phone = models.CharField(max_length=32, blank=True, null=True)
    address = models.CharField(max_length=64, blank=True, null=True)
