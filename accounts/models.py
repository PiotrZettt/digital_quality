from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django_tenants.models import DomainMixin, TenantMixin


class Client(TenantMixin):
    name = models.CharField(max_length=100)
    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True


class User(AbstractUser):
    tenant = models.ForeignKey(Client, on_delete=models.CASCADE)
    groups = models.ManyToManyField(Group, related_name="account_users")
    user_permissions = models.ManyToManyField(Permission, related_name="accounts_permissions")


class Domain(DomainMixin):
    pass
