# tests/test_views.py
import json
from django.test import TestCase
from django.urls import reverse, NoReverseMatch
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Ice Cream", price=80, inventory=100)
        Menu.objects.create(title="Pizza",   price=120, inventory=50)

    def test_getall(self):
        url = "/restaurant/menu/"  # adjust if your route is different
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]["title"], "Ice Cream")
        self.assertEqual(data[1]["title"], "Pizza")
