from allauth.account.adapter import DefaultAccountAdapter

from .models import Client, Domain


class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        company_name = data.get("company")
        schema_name = "".join(company_name.split(" ")).lower()

        # create tenant
        tenant = Client(
            schema_name=schema_name,
            name=company_name,
        )
        tenant.save()

        # create domain
        domain = Domain()
        domain.domain = (
            schema_name + ".localhost"
        )  # don't add your port or www here! on a local server you'll want to use localhost here
        domain.tenant = tenant
        domain.is_primary = True
        domain.save()

        user.tenant = tenant

        user = super().save_user(request, user, form, commit=False)

        if commit:
            user.save()

        return user
