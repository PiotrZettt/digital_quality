# Generated by Django 4.2.1 on 2023-06-25 17:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("audits", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="answer",
            name="comment",
            field=models.CharField(default="", max_length=300),
        ),
    ]
