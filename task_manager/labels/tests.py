from django.test import TestCase, Client
from django.urls import reverse

from task_manager.labels.models import Label
from task_manager.labels.views import (CreateLabelsView, UpdateLabelsView,
                                       DeleteLabelsView)
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


class TestUpdate(TestCase):
    fixtures = [
        'labels.json',
        'users.json']

    def setUp(self):
        self.client = Client()
        self.client.force_login(User.objects.first())
        self.old_label = Label.objects.all().first()
        self.updated_label = {'name': 'test_updated_label'}

    def test_label_update(self):
        url_update = reverse('update_labels', kwargs={'pk': self.old_label.pk})

        response = self.client.get(url_update)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(url_update, f'/labels/{self.old_label.pk}/update/')
        self.assertIs(response.resolver_match.func.view_class,
                      UpdateLabelsView)

        response = self.client.post(url_update, self.updated_label)
        self.assertRedirects(response, reverse('index_labels'), 302)
        self.assertEqual(response['Location'], reverse('index_labels'))

        response = self.client.get(reverse('index_labels'))
        self.assertContains(response, 'test_updated_label')


class TestDelete(TestCase):
    fixtures = ['labels.json',
                'users.json']

    def setUp(self):
        self.client = Client()
        self.client.force_login(User.objects.first())
        self.del_label = Label.objects.all().first()

    def test_delete_label(self):
        response = self.client.get(reverse('index_labels'))
        self.assertContains(response, 'label1')

        url_delete = reverse('delete_labels', kwargs={'pk': self.del_label.pk})
        response = self.client.get(url_delete)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(url_delete, f'/labels/{self.del_label.pk}/delete/')
        self.assertIs(response.resolver_match.func.view_class,
                      DeleteLabelsView)

        response = self.client.post(url_delete)
        self.assertRedirects(response, reverse('index_labels'), 302)
        self.assertEqual(response['Location'], reverse('index_labels'))

        response = self.client.get(reverse('index_labels'))
        self.assertNotContains(response, 'label1')
