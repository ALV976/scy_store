from django.core.management import BaseCommand
from catalog.models import Category, Products
import json
from django.db import connection


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open('categories.json', encoding='UTF-8') as file:
            return json.load(file)
        # Здесь мы получаем данные из фикстурв с категориями

    @staticmethod
    def json_read_products():
        with open('products.json', encoding='UTF-8') as file:
            return json.load(file)
        # Здесь мы получаем данные из фикстурв с продуктами

    def handle(self, *args, **options):

        Products.objects.all().delete()
        Category.objects.all().delete()

        # Создайте списки для хранения объектов
        product_for_create = []
        category_for_create = []

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            category_for_create.append(
                Category(id=category['pk'], category_name=category["fields"]['category_name'], category_description=category["fields"]['category_description'])
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

        # Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for products in Command.json_read_products():
            product_for_create.append(
                Products(id=products['pk'],product_name=products["fields"]['product_name'],
                         product_description=products["fields"]['product_description'],
                        # получаем категорию из базы данных для корректной связки объектов
                        product_category=Category.objects.get(pk=products["fields"]["product_category"]),
                        product_price=products["fields"]["product_price"],
                        created_at=products["fields"]["created_at"],
                        updated_at=products["fields"]["updated_at"]
                )
            )


        # Создаем объекты в базе с помощью метода bulk_create()
        Products.objects.bulk_create(product_for_create)