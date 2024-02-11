from django.test import TestCase, Client
from django.urls import reverse

from task_manager.statuses.views import CreateStatusesView
from task_manager.users.models import User


class TestCreate(TestCase):
    fixtures = [
        'statuses.json',
        'users.json']

    def setUp(self):
        self.client = Client()
        self.client.force_login(User.objects.first())

    def test_statuses_create(self):
        response = self.client.get(reverse('index_statuses'))
        self.assertNotContains(response, 'Another status')

        response = self.client.get(reverse('create_statuses'))
        self.assertEquals(response.status_code, 200)
        self.assertEquals(reverse('create_statuses'), '/statuses/create/')
        self.assertIs(response.resolver_match.func.view_class,
                      CreateStatusesView)

        response = self.client.post(
            reverse('create_statuses'), data={'name': 'Another status'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], reverse('index_statuses'))

        response = self.client.get(reverse('index_statuses'))
        self.assertContains(response, 'Another status')
