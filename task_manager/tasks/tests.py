from django.test import TestCase, Client
from django.urls import reverse

from task_manager.users.models import User


class TestCreate(TestCase):
    fixtures = ['tasks.json',
                'statuses.json',
                'users.json']

    def setUp(self):
        self.client = Client()
        self.client.force_login(User.objects.first())

    def test_index_tasks(self):
        response = self.client.get(reverse('index_tasks'))
        self.assertContains(response, 'Task1')
        self.assertContains(response, 'Task2')
        self.assertNotContains(response, 'Task3')
