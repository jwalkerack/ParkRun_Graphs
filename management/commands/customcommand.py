from django.core.management import BaseCommand, CommandError
from run.management.commands import copy_data

class Command(BaseCommand):
    help = 'Runs custom commands'

    def add_arguments(self, parser):
        parser.add_argument('command', nargs='+', type=str)

    def handle(self, *args, **options):
        command = options['command'][0]

        if command == 'copy_data':
            copy_data.Command().handle()
        else:
            raise CommandError(f'Unknown command: {command}')