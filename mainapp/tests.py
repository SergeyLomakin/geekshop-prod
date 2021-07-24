from django.test import TestCase
from django.test.client import Client

from mainapp.models import ProductCategory, Product


class TestMainSmokeTest(TestCase):
    status_code_success = 200

    def SetUp(self):
        cat_1 = ProductCategory.objects.create(
            name='cat 1'
        )
        Product.objects.create(
            category=cat_1,
            name='prod 1'
        )
        self.client = Client()

    def test_main_app_urls(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, self.status_code_success)

    def test_products_urls(self):
        for product_item in Product.objects.all():
            response = self.client.get(f'/products/product/{product_item.pk}/')
            self.assertEqual(response.status_code, self.status_code_success)
