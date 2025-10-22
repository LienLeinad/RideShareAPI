from django.contrib.auth.views import LoginView
from django.db.models import F, FloatField, Prefetch, QuerySet, Sum
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.viewsets import ModelViewSet

from ride_app.forms import CustomAuthForm
from ride_app.models import Ride, RideEvent
from ride_app.serializers import RideSerializer
from ride_app.utils import haversine_db


class RideViewSet(ModelViewSet):
    serializer_class = RideSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination
    queryset = (
        Ride.objects.all()
        .prefetch_related(
            Prefetch(
                "events",
                RideEvent.objects.filter(
                    created_at__date__gte=timezone.now().date()
                    - timezone.timedelta(hours=24)
                ),
            )
        )
        .select_related("rider", "driver")
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

    def list(self, request, *args, **kwargs):
        longitude = self.request.query_params.get("driver_longitude")
        latitude = self.request.query_params.get("driver_latitude")
        # Handle case where ordering is checked for driver_distance but no long/lat is provided
        ordering = self.request.query_params.get("ordering")
        if not longitude and not latitude and ordering == "driver_distance":
            return Response(
                {
                    "detail": "Cannot order using driver distance without provided longitude and latitude in query parameters."
                },
                status=HTTP_400_BAD_REQUEST,
            )
        return super().list(request, *args, **kwargs)


class CustomLoginView(LoginView):
    template_name = "login.html"
    form_class = CustomAuthForm
