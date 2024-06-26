import json
from django.core.management import BaseCommand
from catalog.models import Product, Category
from config.settings import BASE_DIR


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        """Получение данных категорий из фикстуры"""
        with open(f'{BASE_DIR}/fixtures/01_catalog_category_data.json', encoding='UTF-8') as file:
            data = json.load(file)
        return data

    @staticmethod
    def json_read_products():
        """Получение данных продуктов из фикстуры"""
        with open(f'{BASE_DIR}/fixtures/02_catalog_product_data.json', encoding='UTF-8') as file:
            data = json.load(file)
        return data

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        category_for_create = []
        product_for_create = []

        for category in Command.json_read_categories():
            category_for_create.append(Category(pk=category['pk'],
                                                name=category['fields']['name'],
                                                description=category['fields']['description']))

        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products():
            product_for_create.append(Product(pk=product['pk'],
                                              name=product['fields']['name'],
                                              description=product['fields']['description'],
                                              image=product['fields']['image'],
                                              category=Category.objects.get(pk=product['fields']['category']),
                                              price=product['fields']['price'],
                                              created_at=product['fields']['created_at'],
                                              updated_at=product['fields']['updated_at']))

        Product.objects.bulk_create(product_for_create)