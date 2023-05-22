# Generated by Django 4.1.7 on 2023-05-18 14:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("computerApp", "0028_alter_groupe_nom_alter_machine_maintenancedate"),
    ]

    operations = [
        migrations.AddField(
            model_name="groupe",
            name="responsable",
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="machine",
            name="maintenanceDate",
            field=models.DateField(
                default=datetime.datetime(2023, 5, 18, 14, 38, 48, 483074)
            ),
        ),
    ]
