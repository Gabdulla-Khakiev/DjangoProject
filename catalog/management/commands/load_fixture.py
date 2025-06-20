from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Загружает указанную фикстуру. Пример: python manage.py load_fixture test_data'

    def add_arguments(self, parser):
        parser.add_argument('fixture_name', type=str, help='Имя JSON-файла без .json')

    def handle(self, *args, **kwargs):
        fixture_name = kwargs['fixture_name']
        try:
            call_command('loaddata', fixture_name)
            self.stdout.write(self.style.SUCCESS(f"Фикстура '{fixture_name}.json' успешно загружена!"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Ошибка при загрузке: {e}"))
