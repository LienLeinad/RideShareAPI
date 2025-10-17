from django.contrib import admin

from ride_app.models import Ride, User

# Register your models here.
admin.site.register(User)
admin.site.register(Ride)
