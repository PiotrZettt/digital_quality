from django.contrib.auth.models import AbstractUser
from django.db import models
from django_tenants.models import DomainMixin, TenantMixin


class Client(TenantMixin):
    name = models.CharField(max_length=100)
    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True


class User(AbstractUser):
    tenant = models.ForeignKey(Client, on_delete=models.CASCADE)


class Domain(DomainMixin):
    pass
