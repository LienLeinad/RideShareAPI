from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from ride_app.models import Ride, RideEvent, User


class RideEventInline(TabularInline):
    can_delete = False

    def has_add_permission(self, request, obj):
        return False

    def has_change_permission(self, request, obj):
        return False

    model = RideEvent
    readonly_fields = fields = ["description", "created_at"]


# Register your models here.
@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
        (
            ("Profile Information"),
            {
                "fields": (
                    "phone_number",
                    "role",
                )
            },
        ),
    )


@admin.register(Ride)
class RideAdmin(ModelAdmin):
    inlines = [RideEventInline]


admin.site.register(RideEvent)
