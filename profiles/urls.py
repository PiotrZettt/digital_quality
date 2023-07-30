from django.urls import path

from .views import add_staff, welcome_screen

app_name = "profiles"

urlpatterns = [
    path("add_staff/", add_staff, name="add_staff"),
    path("", welcome_screen, name="home"),
]
