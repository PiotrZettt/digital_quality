from django.urls import include, path
from rest_framework import routers

from .views import (
    ClientSerializerViewSet,
    CustomLoginView,
    DomainSerializerViewSet,
    create_tenant_user_view,
)

router = routers.DefaultRouter()

router.register(r"tenants", ClientSerializerViewSet)
router.register(r"domains", DomainSerializerViewSet)

urlpatterns = [
    path("", include("allauth.urls")),
    path("login", CustomLoginView.as_view(), name="login"),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("create_tenant_user", create_tenant_user_view, name="create_tenant_user"),
    path("api/", include(router.urls)),
]
