from django.test import TestCase, Client
from django.urls import reverse

from task_manager.statuses.models import Status
from task_manager.tasks.models import Tasks
from task_manager.tasks.views import CreateTasksView, UpdateTasksView
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