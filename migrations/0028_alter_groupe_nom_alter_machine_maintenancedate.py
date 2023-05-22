# Generated by Django 4.1.7 on 2023-05-18 14:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("computerApp", "0027_groupe_alter_machine_maintenancedate"),
    ]

    operations = [
        migrations.AlterField(
            model_name="groupe",
            name="nom",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="machine",
            name="maintenanceDate",
            field=models.DateField(
                default=datetime.datetime(2023, 5, 18, 14, 16, 9, 828666)
            ),
        ),
    ]