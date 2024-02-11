from django.test import TestCase, Client
from django.urls import reverse

from task_manager.users.models import User


class IndexStatus(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_status(self):
        response = self.client.get("/statuses/")
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('index_statuses'))
        self.assertNotContains(response, 'Name status')


class TestCreate(TestCase):
    fixtures = [
        'statuses.json',
        'users.json']

    def setUp(self):
        self.client = Client()
        self.client.force_login(User.objects.first())

    def test_statuses_crud(self):
        response = self.client.get(reverse('index_statuses'))
        self.assertNotContains(response, 'Another status')

        response = self.client.post(
            reverse('create_statuses'), data={'name': 'Another status'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], reverse('index_statuses'))

        response = self.client.get(reverse('index_statuses'))
        self.assertContains(response, 'Another status')
