from django.urls import path

from .views import profile_view

app_name = "profiles"

urlpatterns = [
    path("home/", profile_view, name="home"),
]
