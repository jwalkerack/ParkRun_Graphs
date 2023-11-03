from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Copy data from running_* tables to run_* tables'

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO run_event SELECT * FROM running_event")
            cursor.execute("INSERT INTO run_location SELECT * FROM running_location")
            cursor.execute("INSERT INTO run_runner SELECT * FROM running_runner")
            cursor.execute("INSERT INTO run_timings SELECT * FROM running_timings")