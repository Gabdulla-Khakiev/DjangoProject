from django.core.management.base import BaseCommand
from django.db import connection
from catalog.models import Product, Category


class Command(BaseCommand):
    help = 'Удаляет все продукты и категории и сбрасывает id'

    def handle(self, *args, **kwargs):
        # Удаляем все данные
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Сброс автоинкрементов для PostgreSQL
        with connection.cursor() as cursor:
            cursor.execute("ALTER SEQUENCE catalog_product_id_seq RESTART WITH 1;")
            cursor.execute("ALTER SEQUENCE catalog_category_id_seq RESTART WITH 1;")

        self.stdout.write(self.style.SUCCESS("Данные удалены и счетчики ID сброшены."))
