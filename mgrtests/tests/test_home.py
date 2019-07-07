from django.test import TestCase
from django.urls import reverse, resolve


class TestHome(TestCase):
    path = reverse('home')

    def test_home_url(self):
        assert resolve(self.path).view_name == 'home'

    def test_home_status(self):
        response = self.client.get(self.path)
        assert response.status_code == 200
