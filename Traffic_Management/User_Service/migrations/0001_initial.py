<<<<<<< HEAD
# Generated by Django 5.0.1 on 2024-01-29 21:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('driverID', models.AutoField(primary_key=True, serialize=False)),
                ('driverName', models.CharField(max_length=100)),
                ('driverEmail', models.EmailField(max_length=254)),
                ('driverPhone', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Plate',
            fields=[
                ('numberPlate', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('region', models.CharField(max_length=100)),
                ('postal_area', models.CharField(max_length=100)),
                ('age_identifier', models.JSONField()),
                ('random_letters', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='JunctionsLog',
            fields=[
                ('logID', models.AutoField(primary_key=True, serialize=False)),
                ('dateTime', models.DateTimeField()),
                ('location', models.CharField(max_length=100)),
                ('event', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('numberPlate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User_Service.plate')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('numberPlate', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='User_Service.plate')),
                ('vehicleType', models.CharField(max_length=50)),
                ('ownerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User_Service.driver')),
=======
# Generated by Django 4.2.6 on 2024-01-29 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Driver",
            fields=[
                ("driverID", models.AutoField(primary_key=True, serialize=False)),
                ("driverName", models.CharField(max_length=100)),
                ("driverEmail", models.EmailField(max_length=254)),
                ("driverPhone", models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="JunctionsLog",
            fields=[
                ("logID", models.AutoField(primary_key=True, serialize=False)),
                ("numberPlate", models.CharField(max_length=100)),
                ("dateTime", models.DateTimeField()),
                ("period", models.CharField(max_length=100)),
                ("location", models.CharField(max_length=100)),
                ("event", models.CharField(max_length=100)),
                ("status", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Plate",
            fields=[
                (
                    "numberPlate",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                ("region", models.CharField(max_length=100)),
                ("postal_area", models.CharField(max_length=100)),
                ("age_identifier", models.JSONField()),
                ("random_letters", models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name="Vehicle",
            fields=[
                (
                    "numberPlate",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="User_Service.plate",
                    ),
                ),
                ("vehicleType", models.CharField(max_length=50)),
                (
                    "ownerID",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="User_Service.driver",
                    ),
                ),
>>>>>>> bd06404d148486bd045a4b2050a5e37bef0479bb
            ],
        ),
    ]
