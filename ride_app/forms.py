from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError

from ride_app.models import UserRoleChoices


class CustomAuthForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if user.role != UserRoleChoices.ADMIN.value:
            raise ValidationError("User must be admin role to login")
        return super().confirm_login_allowed(user)
