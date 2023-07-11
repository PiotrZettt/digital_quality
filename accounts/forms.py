from allauth.account.forms import LoginForm, SignupForm
from django.contrib.auth import get_user_model
from django.forms import CharField, ModelForm

from .models import Client


class CustomSignupForm(SignupForm):
    company = CharField(max_length=200)


class CustomLoginForm(LoginForm):
    def get_user(self):
        user = get_user_model()
        return user.objects.get(username=self.cleaned_data["login"])


class CreateTenantForm(ModelForm):
    class Meta:
        model = Client
        fields = ["name"]
