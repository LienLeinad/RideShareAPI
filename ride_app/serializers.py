from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from ride_app.models import Ride, RideEvent, User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = [
            "password",
            "is_staff",
            "is_active",
            "date_joined",
            "updated_at",
            "created_at",
            "last_login",
            "is_superuser",
            "groups",
            "user_permissions",
        ]


class RideEventSerializer(ModelSerializer):
    ride = serializers.SerializerMethodField()

    def get_ride(self, obj: RideEvent):
        return obj.ride.id

    class Meta:
        model = RideEvent
        fields = "__all__"


class RideSerializer(ModelSerializer):
    rider = UserSerializer(required=False)
    driver = UserSerializer(required=False)
    todays_ride_events = RideEventSerializer(many=True, source="events")
    driver_distance = serializers.SerializerMethodField()

    def get_driver_distance(self, obj):
        return obj.driver_distance if hasattr(obj, "driver_distance") else None

    class Meta:
        model = Ride
        fields = "__all__"
