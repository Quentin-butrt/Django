# Generated by Django 4.1.7 on 2023-05-18 13:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("computerApp", "0026_alter_machine_maintenancedate_alter_personne_sexe"),
    ]

    operations = [
        migrations.CreateModel(
            name="Groupe",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nom", models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name="machine",
            name="maintenanceDate",
            field=models.DateField(
                default=datetime.datetime(2023, 5, 18, 13, 53, 39, 727453)
            ),
        ),
    ]
