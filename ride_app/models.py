from django.contrib.auth.models import AbstractUser
from django.db import models

from ride_app.mixins import BaseModelMixin


class UserTypeChoices(models.TextChoices):
    ADMIN = "Admin", "Admin"
    RIDER = "Rider", "Rider"
    DRIVER = "Driver", "Driver"


class User(BaseModelMixin, AbstractUser):
    phone_number = models.CharField(max_length=255, db_index=True)
    email = models.EmailField(null=True, blank=True, db_index=True)
    user_type = models.CharField(
        max_length=50,
        choices=UserTypeChoices.choices,
        null=True,
        blank=True,
        db_index=True,
    )
