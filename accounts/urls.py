from django.urls import include, path
from rest_framework import routers

from .views import ClientSerializerViewSet, DomainSerializerViewSet, ObtainAuthToken

router = routers.DefaultRouter()

router.register(r"tenants", ClientSerializerViewSet)
router.register(r"domains", DomainSerializerViewSet)

urlpatterns = [
    path("login", ObtainAuthToken.as_view()),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api/", include(router.urls)),
]
