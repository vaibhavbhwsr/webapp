from django.contrib.auth.models import AbstractUser
from django.db import models  # noqa: F401


class User(AbstractUser):
    USER_ROLE = (
        ("Instructor", "Instructor"),
        ("Learner", "Learner"),
        ("Other", "Other"),
        ("None", None)
    )

    phone = models.CharField(max_length=32, blank=True, null=True)
    address = models.CharField(max_length=64, blank=True, null=True)
    role = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        choices=USER_ROLE,
        default="Learner",
    )
