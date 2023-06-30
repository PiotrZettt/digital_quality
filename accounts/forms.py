from django.forms import ModelForm

from .models import Client


class CreateTenantForm(ModelForm):
    class Meta:
        model = Client
        fields = ["name"]
