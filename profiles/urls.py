from django.urls import include, path
from rest_framework import routers

from .views import ProfileSerializerViewSet

router = routers.DefaultRouter()

router.register(r"profiles", ProfileSerializerViewSet)

urlpatterns = [path("api/", include(router.urls))]
