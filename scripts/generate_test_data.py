"""
    Generates n instances of rider/driver pairs,n/2 rides per pair, and n*3 ride events per ride
    and 1 admin user
    For example:
        n = 3
        total new users = 6 (3 riders, 3 Drivers)
        total new rides = 60 (10 rides per pair)
        total new ride events = 180 (3 events per ride)
    usage:
    python manage.py runscript scripts.generate_test_data_alot --script-args <n>
"""

from django.utils import timezone

from ride_app.models import Ride, RideEvent, RideStatusChoices, User, UserRoleChoices


def run(*args):
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
