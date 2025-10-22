"""
    Generates n instances of rider/driver pairs,n/2 rides per pair, and n*4 ride events per ride
    Assigns all superusers with role Admin to be able to log in the login page
    For example:
        n = 3
        total new users = 6 (3 riders, 3 Drivers)
        total new rides = 60 (10 rides per pair)
        total new ride events = 240 (4 events per ride) (one created 25 hours from time of running the script)
    usage:
    python manage.py runscript scripts.generate_test_data_alot --script-args <n>
"""

import random
import string

from django.utils import timezone
from freezegun import freeze_time

from ride_app.models import Ride, RideEvent, RideStatusChoices, User, UserRoleChoices


def generate_random_string(length=5):
    return "".join(random.choices(string.ascii_letters, k=length))


# Generate a list of 7 days in a week to spread the dates of the ride's pick up through 7 days
days_in_a_week = [timezone.now() - timezone.timedelta(days=i) for i in range(7)]


def run(*args):
    ride_statuses = [choice[0] for choice in RideStatusChoices.choices]
    # Clear everything to keep db clean
    User.objects.exclude(is_superuser=True).delete()
    Ride.objects.all().delete()
    RideEvent.objects.all().delete()
    iters = int(input("Enter number of iterations: "))
    # Set all admin users to role = Admin
    User.objects.filter(is_superuser=True).update(role=UserRoleChoices.ADMIN.value)
    for i in range(iters):
        rider = User.objects.create(
            username=f"test{i}",
            password="test1234!",
            first_name=f"test{i}",
            last_name="test",
            phone_number="+639171231234",
            email=f"{generate_random_string()}+{i}@example.com",
            role=UserRoleChoices.RIDER.value,
        )
        driver = User.objects.create(
            username=f"test_driver{i}",
            password="test1234!",
            first_name=f"test{i}",
            last_name="driver",
            phone_number="+639271231234",
            role=UserRoleChoices.DRIVER.value,
        )

        num_rides = iters // 2 if iters > 1 else 1
        for j in range(num_rides):
            ride = Ride.objects.create(
                rider=rider,
                driver=driver,
                pickup_latitude=123.0,
                pickup_longitude=123.0,
                dropoff_latitude=321.0,
                dropoff_longitude=321.0,
                pickup_time=days_in_a_week[
                    j % 7
                ],  # evenly assign dates for pick up time
                status=ride_statuses[j % 4],  # evenly spread the status of the rides
            )
            # NOTE: one event is created more than 24 hours ago, to test "todays_ride_events" field
            with freeze_time(timezone.now() - timezone.timedelta(hours=25)):
                ride.events.create(
                    description="Ride Created",
                )
            ride.events.create(
                description="Picked Up",
            )
            ride.events.create(
                description="En Route",
            )
            ride.events.create(
                description="Dropped Off",
            )
