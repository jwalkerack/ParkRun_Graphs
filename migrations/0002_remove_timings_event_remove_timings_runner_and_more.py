# Generated by Django 4.1 on 2023-01-12 02:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("run", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="timings",
            name="event",
        ),
        migrations.RemoveField(
            model_name="timings",
            name="runner",
        ),
        migrations.DeleteModel(
            name="event",
        ),
        migrations.DeleteModel(
            name="location",
        ),
        migrations.DeleteModel(
            name="runner",
        ),
        migrations.DeleteModel(
            name="timings",
        ),
    ]
