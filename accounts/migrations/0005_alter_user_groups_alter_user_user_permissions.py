# Generated by Django 4.2.1 on 2023-07-11 22:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("accounts", "0004_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="groups",
            field=models.ManyToManyField(related_name="account_users", to="auth.group"),
        ),
        migrations.AlterField(
            model_name="user",
            name="user_permissions",
            field=models.ManyToManyField(related_name="accounts_permissions", to="auth.permission"),
        ),
    ]
