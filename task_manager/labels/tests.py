from django.test import TestCase, Client
from django.urls import reverse

from task_manager.labels.views import CreateLabelsView
from task_manager.users.models import User


class TestCreate(TestCase):
    fixtures = ['labels.json',
                'users.json']

    def setUp(self):
        self.client = Client()
        self.client.force_login(User.objects.first())

    def test_index_labels(self):
        response = self.client.get(reverse('index_labels'))
        self.assertContains(response, 'label1')
        self.assertContains(response, 'label2')
        self.assertNotContains(response, 'label4')

    def test_labels_create(self):
        response = self.client.get(reverse('index_labels'))
        self.assertNotContains(response, 'Test label')

        response = self.client.get(reverse('create_labels'))
        self.assertEquals(response.status_code, 200)
        self.assertEquals(reverse('create_labels'), '/labels/create/')
        self.assertIs(response.resolver_match.func.view_class,
                      CreateLabelsView)

        response = self.client.post(
            reverse('create_labels'), data={'name': 'Test label'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], reverse('index_labels'))

        response = self.client.get(reverse('index_labels'))
        self.assertContains(response, 'Test label')
