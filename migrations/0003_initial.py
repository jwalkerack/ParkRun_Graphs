# Generated by Django 4.1 on 2023-01-12 02:29

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("run", "0002_remove_timings_event_remove_timings_runner_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="event",
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
                ("number", models.TextField()),
                ("Date", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="location",
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
                (
                    "Name",
                    models.CharField(
                        max_length=100,
                        validators=[
                            django.core.validators.MinLengthValidator(
                                2, "Title must be greater than 2 characters"
                            )
                        ],
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="runner",
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
                (
                    "Name",
                    models.CharField(
                        max_length=100,
                        validators=[
                            django.core.validators.MinLengthValidator(
                                2, "Title must be greater than 2 characters"
                            )
                        ],
                    ),
                ),
                ("ParkRunId", models.PositiveIntegerField()),
                ("Gender", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="timings",
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
                ("runnerPosition", models.TextField()),
                ("runnerTime", models.TextField()),
                ("runnerTimeInSeconds", models.PositiveIntegerField()),
                ("runnerClub", models.TextField()),
                ("runnerGroup", models.TextField()),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="run.event"
                    ),
                ),
                (
                    "runner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="run.runner"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="event",
            name="location",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="run.location"
            ),
        ),
    ]