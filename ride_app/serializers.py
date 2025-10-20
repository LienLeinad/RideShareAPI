from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from ride_app.models import Ride, RideEvent, User, UserRoleChoices


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    token_class = RefreshToken

    def validate(self, attrs):
        data = super().validate(attrs)
        if self.user.role and self.user.role != UserRoleChoices.ADMIN.value:
            raise ValidationError("User is not allowed to use the API.")
        return data


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

    class Meta:
        model = Ride
        fields = "__all__"
