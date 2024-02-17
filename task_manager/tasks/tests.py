from django.test import TestCase, Client
from django.urls import reverse

from task_manager.statuses.models import Status
from task_manager.tasks.models import Tasks
from task_manager.tasks.views import (CreateTasksView, UpdateTasksView,
                                      DeleteTasksView, DetailTasksView)
from task_manager.users.models import User


class TestCreate(TestCase):
    fixtures = ['tasks.json',
                'statuses.json',
                'users.json']

    def setUp(self):
        self.client = Client()
        self.client.force_login(User.objects.first())
        self.status = Status.objects.get(name='Status1')
        self.executor = User.objects.get(username='User_test')
        self.created_task = {'name': 'Test task',
                             'description': 'Test',
                             'status': self.status.pk,
                             'executor': self.executor.pk}

    def test_index_tasks(self):
        response = self.client.get(reverse('index_tasks'))
        self.assertContains(response, 'Task1')
        self.assertContains(response, 'Task2')
        self.assertNotContains(response, 'Task3')

    def test_tasks_create(self):
        response = self.client.get(reverse('index_tasks'))
        self.assertNotContains(response, 'Test task')

        response = self.client.get(reverse('create_tasks'))
        self.assertEquals(response.status_code, 200)
        self.assertEquals(reverse('create_tasks'), '/tasks/create/')
        self.assertIs(response.resolver_match.func.view_class, CreateTasksView)

        response = self.client.post(reverse('create_tasks'), self.created_task)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], reverse('index_tasks'))

        response = self.client.get(reverse('index_tasks'))
        self.assertContains(response, 'Test task')


class TestUpdate(TestCase):
    fixtures = ['tasks.json',
                'statuses.json',
                'users.json']

    def setUp(self):
        self.client = Client()
        self.client.force_login(User.objects.first())
        self.status = Status.objects.all().first()
        self.task = Tasks.objects.all().first()
        self.executor = User.objects.get(username='User_test')
        self.updated_task = {'name': 'Test_update_task',
                             'status': self.status.pk,
                             'executor': self.executor.pk}

    def test_tasks_update(self):
        url_update = reverse('update_tasks', kwargs={'pk': self.task.pk})

        response = self.client.get(reverse('index_tasks'))
        self.assertNotContains(response, 'Test_update_task')

        response = self.client.get(url_update)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(url_update, f'/tasks/{self.task.pk}/update/')
        self.assertIs(response.resolver_match.func.view_class, UpdateTasksView)

        response = self.client.post(url_update, self.updated_task)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], reverse('index_tasks'))

        response = self.client.get(reverse('index_tasks'))
        self.assertContains(response, 'Test_update_task')


class TestDelete(TestCase):
    fixtures = ['tasks.json',
                'statuses.json',
                'users.json']

    def setUp(self):
        self.client = Client()
        self.client.force_login(User.objects.first())
        self.del_task = Tasks.objects.all().first()

    def test_delete_tasks(self):
        response = self.client.get(reverse('index_tasks'))
        self.assertContains(response, 'Task1')

        url_delete = reverse('delete_tasks', kwargs={'pk': self.del_task.pk})

        response = self.client.get(url_delete)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(url_delete, f'/tasks/{self.del_task.pk}/delete/')
        self.assertIs(response.resolver_match.func.view_class,
                      DeleteTasksView)

        response = self.client.post(url_delete)
        self.assertRedirects(response, reverse('index_tasks'), 302)
        self.assertEqual(response['Location'], reverse('index_tasks'))

        response = self.client.get(reverse('index_tasks'))
        self.assertNotContains(response, 'Task1')


class TestDetail(TestCase):
    fixtures = ['tasks.json',
                'statuses.json',
                'users.json']

    def setUp(self):
        self.client = Client()
        self.client.force_login(User.objects.first())
        self.task = Tasks.objects.all().first()

    def test_detail_tasks(self):
        url_detail = reverse('detail_tasks', kwargs={'pk': self.task.pk})
        response = self.client.get(url_detail)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(url_detail, f'/tasks/{self.task.pk}/')
        self.assertIs(response.resolver_match.func.view_class,
                      DetailTasksView)
