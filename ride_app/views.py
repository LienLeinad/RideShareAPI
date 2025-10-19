from rest_framework_simplejwt.views import TokenObtainPairView

from ride_app.serializers import CustomTokenObtainPairSerializer


class UserLoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
