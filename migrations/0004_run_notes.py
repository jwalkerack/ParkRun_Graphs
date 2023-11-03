# Generated by Django 4.1 on 2023-01-12 11:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("run", "0003_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="run_notes",
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
                ("section", models.CharField(max_length=14)),
                (
                    "notes",
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
    ]