# Generated by Django 4.2.1 on 2023-07-11 11:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("stock_flow", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CycleStage",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("cycle_stage_name", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Location",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("location_name", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="PartStatus",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("status_name", models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name="project",
            name="project_code",
        ),
        migrations.AddField(
            model_name="part",
            name="dispatch_date",
            field=models.DateField(auto_now_add=True, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="project",
            name="project_customer_code",
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name="project",
            name="project_internal_code",
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name="part",
            name="location",
            field=models.ForeignKey(
                default=0, on_delete=django.db.models.deletion.CASCADE, related_name="parts", to="stock_flow.location"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="part",
            name="stage",
            field=models.ForeignKey(
                default=0, on_delete=django.db.models.deletion.CASCADE, related_name="parts", to="stock_flow.cyclestage"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="part",
            name="status",
            field=models.ForeignKey(
                default=0, on_delete=django.db.models.deletion.CASCADE, related_name="parts", to="stock_flow.partstatus"
            ),
            preserve_default=False,
        ),
    ]
