from django.test import TestCase, Client
from django.urls import reverse, reverse_lazy
from django.contrib.auth import get_user_model

from task_manager.users.forms import CreateUserForm, UpdateUserForm


class TestStatusAndHtml(TestCase):
    fixtures = ['users.json']

    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.get(username='User_test')

    def test_status_code(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse("create_users"))
        self.assertEqual(response.status_code, 200)

    def test_html(self):
        user = get_user_model().objects.get(username='User_test')
        response = self.client.get(reverse_lazy('index_users'))
        html = response.content.decode()
        self.assertInHTML(str(user.id), html)
        self.assertInHTML(str(user.username), html)
        self.assertInHTML(str(user), html)
        self.assertInHTML(user.date_joined.strftime("%d.%m.%Y %H:%M"), html)


class TestCreateUser(TestCase):
    fixtures = ['users.json']

    def setUp(self):
        self.client = Client()
        self.new_user = {"first_name": "User3", "last_name": "User3_last",
                         "username": "User3_test", "password1": "Password3",
                         "password2": "Password3"}

    def test_create_user(self):
        response = self.client.get(reverse('index_users'))
        self.assertNotContains(response, 'User3 User3_last')

        response = self.client.get(reverse('create_users'))
        self.assertEquals(reverse('create_users'), '/users/create/')
        self.assertIsInstance(response.context['form'], CreateUserForm)

        response = self.client.post(reverse("create_users"), self.new_user)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"], "/login/")

        response = self.client.get(reverse('index_users'))
        self.assertContains(response, 'User3 User3_last')


class TestUpdateUser(TestCase):
    fixtures = ['users.json']

    def setUp(self):
        self.user = get_user_model().objects.get(username='User1_test')
        self.new_user = {'username': 'User_new_test',
                         'first_name': 'User_new',
                         'last_name': 'User_new_last',
                         'password1': 'Password_new',
                         'password2': 'Password_new'}
        self.url = reverse('update_users', kwargs={'pk': self.user.pk})

        self.client.force_login(self.user)
        response = self.client.get(self.url)

        self.assertEquals(response.status_code, 200)
        self.assertEquals(self.url, f'/users/{self.user.pk}/update/')
        self.assertIsInstance(response.context['form'], UpdateUserForm)

        self.client.force_login(self.user)
        response = self.client.post(self.url, self.new_user)

        self.assertEquals(self.url, f'/users/{self.user.pk}/update/')
        self.assertRedirects(response, reverse('index_users'), 302)
        self.assertEqual(response['Location'], '/users/')

        self.client.force_login(self.user)
        self.client.post(self.url, self.new_user)

        [current_user_data] = \
            get_user_model().objects.filter(pk=self.user.pk).values()

        for key in ('username', 'first_name', 'last_name'):
            self.assertEquals(self.new_user[key], current_user_data[key])

        current_user_data: get_user_model() = \
            get_user_model().objects.get(pk=self.user.pk)
        self.assertTrue(current_user_data.check_password('Password_new'))

        response = self.client.get(reverse('index_users'))
        self.assertContains(response, 'User_new User_new_last')


class TestDeleteUser(TestCase):
    fixtures = ['users.json']

    def setUp(self):
        self.client = Client()

    def test_delete_users(self):
        del_user = \
            get_user_model().objects.get(username='User2_test')
        response = self.client.get(reverse('delete_users',
                                           kwargs={'pk': del_user.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], '/login/')

        self.client.force_login(del_user)
        response = self.client.post(reverse('delete_users',
                                            kwargs={'pk': del_user.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], '/users/')
        self.assertFalse(get_user_model().objects.filter
                         (username='User2_test').exists())
