from django.contrib.auth.models import AbstractUser
from django.db import models

from ride_app.mixins import BaseModelMixin


class UserRoleChoices(models.TextChoices):
    ADMIN = "Admin", "Admin"
    RIDER = "Rider", "Rider"
    DRIVER = "Driver", "Driver"


class RideStatusChoices(models.TextChoices):
    NEW = "New", "New"
    EN_ROUTE = "En Route", "En Route"
    PICK_UP = "Pick Up", "Pick Up"
    DROP_OFF = "Drop Off", "Drop Off"


class User(BaseModelMixin, AbstractUser):
    phone_number = models.CharField(max_length=255, db_index=True)
    email = models.EmailField(null=True, blank=True, db_index=True)
    role = models.CharField(
        max_length=50,
        choices=UserRoleChoices.choices,
        null=True,
        blank=True,
        db_index=True,
    )


class Ride(BaseModelMixin, AbstractUser):
    status = models.CharField(
        max_length=50,
        choices=RideStatusChoices.choices,
        default=RideStatusChoices.NEW.value,
        db_index=True,
    )
    rider = models.ForeignKey(
        to=User,
        related_name="rides_taken",
        db_index=True,
        on_delete=models.SET_NULL,
        null=True,
        limit_choices_to={"role": UserRoleChoices.RIDER.value},
    )
    driver = models.ForeignKey(
        to=User,
        related_name="rides_driven",
        db_index=True,
        on_delete=models.SET_NULL,
        null=True,
        limit_choices_to={"role": UserRoleChoices.DRIVER.value},
    )
    pickup_latitude = models.FloatField(default=0.0)
    pickup_longitude = models.FloatField(default=0.0)
    dropoff_latitude = models.FloatField(default=0.0)
    dropoff_longitude = models.FloatField(default=0.0)
    pickup_time = models.DateTimeField(null=True, blank=True, db_index=True)


class RideEvent(BaseModelMixin):
    # NOTE: Overriding this from BaseModelMixin to add db index
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    ride = models.ForeignKey(to=Ride, related_name="events", on_delete=models.CASCADE)
