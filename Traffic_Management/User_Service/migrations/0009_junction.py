# Generated by Django 4.2.6 on 2024-02-19 18:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("User_Service", "0008_alter_finelog_driverid"),
    ]

    operations = [
        migrations.CreateModel(
            name="Junction",
            fields=[
                ("junctionID", models.AutoField(primary_key=True, serialize=False)),
                ("junctionName", models.CharField(max_length=255)),
                ("latitude", models.IntegerField(default=0)),
                ("longitude", models.IntegerField(default=0)),
            ],
        ),
    ]
