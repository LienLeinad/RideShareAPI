from django.contrib.auth.views import LoginView
from django.db.models import F, FloatField, QuerySet, Sum
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from ride_app.forms import CustomAuthForm
from ride_app.models import Ride
from ride_app.serializers import RideSerializer
from ride_app.utils import haversine_db


class RideViewSet(ModelViewSet):
    serializer_class = RideSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination
    queryset = (
        Ride.objects.all().prefetch_related("events").select_related("rider", "driver")
    )
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = ["pickup_time", "driver_distance"]
    filterset_fields = ["status", "rider__email"]
    ordering = ["created_at"]

    def annotate_driver_distance(
        self, queryset: QuerySet, longitude: float, latitude: float
    ):
        qs = queryset.annotate(
            driver_distance=Sum(
                haversine_db(
                    lat1=latitude,
                    lon1=longitude,
                    lat2=F("pickup_latitude"),
                    lon2=F("pickup_longitude"),
                ),
                output_field=FloatField(),
            )
        )
        return qs

    def get_queryset(self):
        qs = super().get_queryset()
        longitude = self.request.query_params.get("driver_longitude")
        latitude = self.request.query_params.get("driver_latitude")
        if longitude and latitude:
            qs = self.annotate_driver_distance(qs, float(longitude), float(latitude))
        return qs


class CustomLoginView(LoginView):
    template_name = "login.html"
    form_class = CustomAuthForm
