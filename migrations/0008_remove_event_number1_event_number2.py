# Generated by Django 4.1 on 2023-02-22 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("run", "0007_rename_number_event_number1"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="event",
            name="number1",
        ),
        migrations.AddField(
            model_name="event",
            name="number2",
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
