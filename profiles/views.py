from django.shortcuts import render


def profile_view(request):
    context = {"user": request.user, "company": request.tenant.name}
    return render(request, "index.html", context)
