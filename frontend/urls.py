from django.urls import path

from .views import index

urlpatterns = [path("auth", index)]
