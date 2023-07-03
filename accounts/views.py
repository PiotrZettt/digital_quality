from allauth.account.views import LoginView, SignupView
from django.http import HttpResponse
from django.shortcuts import render
from django_tenants.utils import schema_context
from rest_framework import parsers, permissions, renderers, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Client, Domain, User
from .serializers import ClientSerializer, DomainSerializer


def create_tenant_user_view(request):
    if request.method == "POST":
        # Retrieve the form data submitted by the user
        company_name = request.POST["company_name"]
        schema_name = "".join(company_name.split(" ")).lower()
        username = request.POST["username"]
        password = request.POST["password"]

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
                username=username, password=password, tenant=tenant, is_staff=True, is_superuser=True
            )

        # Return a success response or redirect to another page
        return HttpResponse("Tenant user created successfully!")

    # Render the form template for user input
    return render(request, "create_tenant_user.html")


class CustomSignupView(SignupView):
    def form_valid(self, form):
        # Get the company name from the form input
        company = form.cleaned_data["company"]

        # Create the tenant name based on the company name
        schema_name = "".join(company.split(" ")).lower()

        # Create the schema using django-tenants
        with schema_context(schema_name):
            # Create the tenant
            tenant = Client(name=company, schema_name=schema_name)
            tenant.save()

            # Assign the tenant to the user
            user = form.save(self.request)
            user.tenant = tenant
            user.save()

        # Call the parent class's form_valid method
        return super().form_valid(form)


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
