"""Generates 1 instance of rider driver ride and 3 ride events"""
from django.utils import timezone

from ride_app.models import Ride, RideEvent, RideStatusChoices, User, UserRoleChoices


def run():
    # Clear everything to keep db clean
    User.objects.exclude(is_superuser=True).delete()
    Ride.objects.all().delete()
    RideEvent.objects.all().delete()
    # Create an admin to test authentication
    User.objects.create(
        username="test_admin",
        password="Test1234!",
        first_name="test",
        last_name="admin",
        phone_number="+639171234123",
        role=UserRoleChoices.ADMIN.value,
    )
    for i in range(100):
        rider = User.objects.create(
            username=f"test{i}",
            password="test1234!",
            first_name=f"test{i}",
            last_name="test",
            phone_number="+639171231234",
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

        for j in range(100):
            ride = Ride.objects.create(
                rider=rider,
                driver=driver,
                pickup_latitude=123.0,
                pickup_longitude=123.0,
                dropoff_latitude=321.0,
                dropoff_longitude=321.0,
                pickup_time=timezone.now(),
                status=RideStatusChoices.DROP_OFF.value,
            )
            ride.events.create(description="Picked Up", created_at=timezone.now())
            ride.events.create(
                ride=ride,
                description="En Route",
                created_at=timezone.now(),
            )
            ride.events.create(
                ride=ride,
                description="Dropped Off",
                created_at=timezone.now(),
            )
