# Generated by Django 4.1.7 on 2023-05-22 08:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("computerApp", "0041_remove_machine_ip_alter_machine_maintenancedate"),
    ]

    operations = [
        migrations.AlterField(
            model_name="machine",
            name="maintenanceDate",
            field=models.DateField(
                default=datetime.datetime(2023, 6, 5, 8, 12, 7, 969362)
            ),
        ),
    ]
