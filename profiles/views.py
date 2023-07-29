from django.shortcuts import render

from .models import User


def profile_view(request):
    message = f"Welcome to IsInSpec. This is you profile of {request.user.company_name}"

    context = {"message": message}
    return render(request, "index.html", context=context)


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
