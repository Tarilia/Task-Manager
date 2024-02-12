from django.test import TestCase, Client
from django.urls import reverse

from task_manager.statuses.models import Status
from task_manager.statuses.views import (CreateStatusesView,
                                         UpdateStatusesView)
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


class TestUpdate(TestCase):
    fixtures = [
        'statuses.json',
        'users.json']

    def setUp(self):
        self.client = Client()
        self.client.force_login(User.objects.first())

    def test_statuses_update(self):
        old_status = Status.objects.get(name='Status1')
        url_update = reverse('update_statuses', kwargs={'pk': old_status.pk})
        updated_status = {'name': 'updated_status'}

        response = self.client.get(url_update)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(url_update, f'/statuses/{old_status.pk}/update/')
        self.assertIs(response.resolver_match.func.view_class,
                      UpdateStatusesView)

        response = self.client.post(url_update, updated_status)
        self.assertEquals(url_update, f'/statuses/{old_status.pk}/update/')
        self.assertRedirects(response, reverse('index_statuses'), 302)
        self.assertIs(response.resolver_match.func.view_class,
                      UpdateStatusesView)
        self.assertEqual(response['Location'], reverse('index_statuses'))

        [current_status] = Status.objects.filter(pk=old_status.pk).values()
        expected_status = updated_status['name']
        assert expected_status == current_status['name']

        response = self.client.get(reverse('index_statuses'))
        self.assertNotContains(response, 'Status1')
        self.assertContains(response, 'updated_status')
