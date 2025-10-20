from django.views.generic import TemplateView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

from ride_app.models import Ride
from ride_app.serializers import CustomTokenObtainPairSerializer, RideSerializer


class UserLoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class RideViewSet(ModelViewSet):
    serializer_class = RideSerializer
    permission_classes = (
        AllowAny,
    )  # TODO: Put back to IsAuthenticated once done debugging
    pagination_class = PageNumberPagination
    queryset = Ride.objects.none()

    def list(self, request, *args, **kwargs):
        rides = (
            Ride.objects.all()
            .select_related("rider", "driver")
            .prefetch_related("events")
        )
        serializer = RideSerializer(rides, many=True)
        return Response(serializer.data)


class DebugView(TemplateView):
    template_name = "index.html"
