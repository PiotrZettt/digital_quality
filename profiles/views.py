from django.shortcuts import render

from .models import User


def welcome_screen(request):
    return render(request, "auth.html")


def add_staff(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        User.objects.create_user(
            username=username,
            password=password,
            is_staff=False,
            is_superuser=False,
        )

    return render(request, "add_staff.html")
