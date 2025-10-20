from django.contrib.auth.views import LoginView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from ride_app.forms import CustomAuthForm
from ride_app.models import Ride
from ride_app.serializers import RideSerializer


class RideViewSet(ModelViewSet):
    serializer_class = RideSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination
    queryset = (
        Ride.objects.all().prefetch_related("events").select_related("rider", "driver")
    )


class CustomLoginView(LoginView):
    template_name = "login.html"
    form_class = CustomAuthForm
