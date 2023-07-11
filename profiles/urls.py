from django.urls import path

from .views import add_staff, profile_view

app_name = "profiles"

urlpatterns = [
    path("add_staff/", add_staff, name="add_staff"),
    path("home/", profile_view, name="home"),
]
