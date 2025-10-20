from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
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
    permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination
    queryset = (
        Ride.objects.all().prefetch_related("events").select_related("rider", "driver")
    )
