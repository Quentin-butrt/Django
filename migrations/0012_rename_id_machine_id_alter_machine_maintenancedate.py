# Generated by Django 4.1.7 on 2023-05-11 08:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("computerApp", "0011_alter_machine_maintenancedate"),
    ]

    operations = [
        migrations.RenameField(
            model_name="machine",
            old_name="id",
            new_name="Id",
        ),
        migrations.AlterField(
            model_name="machine",
            name="maintenanceDate",
            field=models.DateField(
                default=datetime.datetime(2023, 5, 11, 8, 34, 54, 726631)
            ),
        ),
    ]
