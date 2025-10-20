from datetime import datetime

from django.utils import timezone
from rest_framework.test import APITestCase

from ride_app.models import Ride, RideStatusChoices, User, UserRoleChoices


class RideAPITestCase(APITestCase):
    def setUp(self):
        self.rider = User.objects.create(
            username="test",
            password="test1234!",
            first_name="test",
            last_name="test",
            phone_number="+639171231234",
            role=UserRoleChoices.RIDER.value,
        )
        self.driver = User.objects.create(
            username="test_driver",
            password="test1234!",
            first_name="test",
            last_name="driver",
            phone_number="+639271231234",
            role=UserRoleChoices.DRIVER.value,
        )
        self.admin = User.objects.create(
            username="test_admin",
            password="Test1234!",
            first_name="test",
            last_name="admin",
            phone_number="+639171234123",
            role=UserRoleChoices.ADMIN.value,
        )

        self.ride_1 = Ride.objects.create(
            rider=self.rider,
            driver=self.driver,
            pickup_latitude=123.0,
            pickup_longitude=123.0,
            dropoff_latitude=321.0,
            dropoff_longitude=321.0,
            pickup_time=datetime(2025, 1, 1),
            status=RideStatusChoices.DROP_OFF.value,
        )

        self.ride_event_1 = self.ride_1.events.create(description="Picked Up")
        self.ride_event_2 = self.ride_1.events.create(
            ride=self.ride_1,
            description="En Route",
            created_at=timezone.now(),
        )
        self.ride_event_3 = self.ride_1.events.create(
            ride=self.ride_1,
            description="Dropped Off",
            created_at=timezone.now(),
        )
        self.client.force_authenticate(self.admin)

    def test_get_api(self):
        response = self.client.get("/ride/")
        self.assertEqual(200, response.status_code)
