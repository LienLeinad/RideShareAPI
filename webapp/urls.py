"""
URL configuration for webapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import SimpleRouter

from ride_app import views as ride_app_views

router = SimpleRouter()

router.register("ride", ride_app_views.RideViewSet, "ride-view")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("login", ride_app_views.CustomLoginView.as_view()),
] + debug_toolbar_urls()
