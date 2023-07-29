from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

from .models import Client, User


class CreateTenantForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ["name"]


class RegistrationForm(UserCreationForm):
    company_name = forms.CharField(
        label=_("Company name"),
        strip=False,
    )

    class Meta:
        model = User
        fields = ["company_name", "first_name", "email"]
