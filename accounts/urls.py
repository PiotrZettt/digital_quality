from django.urls import include, path
from rest_framework import routers

from .views import (
    ClientSerializerViewSet,
    CustomLoginView,
    DomainSerializerViewSet,
    UserRegistrationView,
    home,
)

router = routers.DefaultRouter()

router.register(r"tenants", ClientSerializerViewSet)
router.register(r"domains", DomainSerializerViewSet)

urlpatterns = [
    path("signin", UserRegistrationView.as_view(), name="signin"),
    path("login", CustomLoginView.as_view(), name="login"),
    path("home/", home, name="home"),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api/", include(router.urls)),
]
