# Generated by Django 4.2.1 on 2023-07-11 11:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("audits", "0002_answer_comment"),
    ]

    operations = [
        migrations.CreateModel(
            name="Picture",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("picture", models.ImageField(upload_to="media")),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="pictures", to="audits.question"
                    ),
                ),
            ],
        ),
    ]
