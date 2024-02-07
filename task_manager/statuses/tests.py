from django.test import TestCase, Client
from django.urls import reverse


class TestStatus(TestCase):
    def setUp(self):
        self.client = Client()

    def index_status(self):
        response = self.client.get("/statuses/")
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('index_statuses'))
        self.assertNotContains(response, 'Name status')
