from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required()
def profile_view(request):
    context = {"user": request.user, "company": request.tenant.name}
    return render(request, "index.html", context)
