from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django_tenants.utils import schema_context
from rest_framework import parsers, permissions, renderers, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import RegistrationForm
from .models import Client, Domain, User
from .serializers import ClientSerializer, DomainSerializer


def home(request):
    company = request.user.company_name
    first_name = request.user.first_name

    print(first_name)

    context = {"company": company, "first_name": first_name}
    return render(request, "home.html", context)


def create_tenant_user_view(request):
    if request.method == "POST":
        # Retrieve the form data submitted by the user
        company_name = request.POST["company_name"]
        first_name = request.POST["first_name"]
        schema_name = "".join(company_name.split(" ")).lower()
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        print("prints:", company_name, first_name)

        if password1 == password2:
            tenant = Client(
                schema_name=schema_name,
                name=company_name,
            )
            tenant.save()

            # Add one or more domains for the tenant
            domain = Domain()
            domain.domain = (
                schema_name + ".localhost"
            )  # don't add your port or www here! on a local server you'll want to use localhost here
            domain.tenant = tenant
            domain.is_primary = True
            domain.save()

            # Create the tenant user within the appropriate schema context
            with schema_context(schema_name):
                User.objects.create_user(
                    username=schema_name,
                    password=password1,
                    tenant=tenant,
                    is_staff=False,
                    is_superuser=False,
                )

            # Return a success[ response or redirect to another page]
            return HttpResponseRedirect(f"http://{domain}:8000/accounts/login")
        else:
            context = {"error_message": "Your confirmation password doesn't match"}
            return render(request, "register.html", context=context)

    # Render the form template for user input
    return render(request, "register.html")


class UserRegistrationView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, "register.html", {"form": form})

    def post(self, request):
        form = RegistrationForm(request.POST)

        if form.is_valid():
            company_name = form.cleaned_data["company_name"]
            schema_name = "".join(company_name.split(" ")).lower()
            first_name = request.POST["first_name"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password2"]

            tenant = Client(
                schema_name=schema_name,
                name=company_name,
            )
            tenant.save()

            # Add one or more domains for the tenant
            domain = Domain()
            domain.domain = (
                schema_name + ".localhost"
            )  # don't add your port or www here! on a local server you'll want to use localhost here
            domain.tenant = tenant
            domain.is_primary = True
            domain.save()

            # Create a new user object
            with schema_context(schema_name):
                User.objects.create_user(
                    username=schema_name,
                    password=password,
                    company_name=company_name,
                    first_name=first_name,
                    email=email,
                    tenant=tenant,
                    is_staff=False,
                    is_superuser=False,
                )
            send_mail(
                subject="IsInSpec Registration",
                message=f"Hi {first_name}. Please go to http://{domain}:8000/accounts/login and"
                f" activate your account with the username: {schema_name}"
                f" and the password submitted during registration",
                from_email="pythonzet@gmail.com",
                recipient_list=[email],
                fail_silently=False,
            )

            return HttpResponseRedirect(f"http://{domain}:8000/accounts/login")

        return render(request, "register.html", {"form": form})


class CustomLoginView(LoginView):
    template_name = "accounts/login.html"  # Specify the path to your login template

    def form_valid(self, form):
        user = form.get_user()
        if user.tenant == self.request.tenant:
            return super().form_valid(form)
        else:
            # Handle the case where user.tenant doesn't match request.tenant
            return render(self.request, "accounts/login.html", {"error_message": "Invalid username or password."})


class ClientSerializerViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.BasePermission]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    ordering_fields = ["id"]


class DomainSerializerViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.BasePermission]
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer
    ordering_fields = ["id"]


class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (
        parsers.FormParser,
        parsers.MultiPartParser,
        parsers.JSONParser,
    )
    renderer_classes = (renderers.JSONRenderer,)

    def post(self, request):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]

        Token.objects.filter(user=user).delete()
        token = Token.objects.create(user=user)

        return Response({"token": token.key, "user_id": user.id})
