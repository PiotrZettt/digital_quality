from django.urls import include, path
from rest_framework import routers

from .views import CustomerSerializerViewSet, ProjectSerializerViewSet, PartSerializerViewSet

router = routers.DefaultRouter()

router.register(r"customers", CustomerSerializerViewSet)
router.register(r"projects", ProjectSerializerViewSet)
router.register(r"parts", PartSerializerViewSet)


urlpatterns = [path("api/", include(router.urls))]
