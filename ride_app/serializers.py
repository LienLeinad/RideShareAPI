from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from ride_app.models import UserRoleChoices


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    token_class = RefreshToken

    def validate(self, attrs):
        data = super().validate(attrs)
        if self.user.role and self.user.role != UserRoleChoices.ADMIN.value:
            raise ValidationError("User is not allowed to use the API.")
        return data
