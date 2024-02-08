from django.test import TestCase, Client
from django.urls import reverse, reverse_lazy
from django.contrib.auth import get_user_model


class TestUsers(TestCase):
    def setUp(self):
        self.client = Client()
        self.test_user = {"first_name": "test_first", "last_name": "test_last",
                          "username": "test_username", "password1": "test1234",
                          "password2": "test1234"}

    def index_users(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

        response = self.client.get("/users/")
        self.assertEqual(response.status_code, 200)

    def test_users_crud(self):
        response = self.client.get(reverse('index_users'))
        self.assertNotContains(response, 'test_first test_last')

        response = self.client.post(reverse("create_users"), self.test_user)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"], "/login/")

        response = self.client.get(reverse("create_users"))
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('index_users'))
        self.assertContains(response, 'test_first test_last')

        user = \
            get_user_model().objects.get(username=self.test_user['username'])
        response = self.client.get(reverse_lazy('index_users'))
        html = response.content.decode()
        self.assertInHTML(str(user.id), html)
        self.assertInHTML(str(user.username), html)
        self.assertInHTML(str(user), html)
        self.assertInHTML(user.date_joined.strftime("%d.%m.%Y %H:%M"), html)

        update_user = \
            get_user_model().objects.get(username=self.test_user['username'])
        response = self.client.get(reverse('update_users',
                                           kwargs={'pk': update_user.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], '/login/')

        self.client.force_login(update_user)
        self.test_user['last_name'] = 'test_second'
        response = self.client.post(reverse('update_users',
                                            kwargs={'pk': update_user.pk}),
                                    self.test_user)
        self.assertEqual(response.status_code, 302)

        response = self.client.get(reverse('index_users'))
        self.assertContains(response, 'test_first test_second')

        del_user = \
            get_user_model().objects.get(username=self.test_user['username'])
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
                         (username=self.test_user['username']).exists())


class TestForms(TestCase):
    def test_registration(self):
        self.client = Client()
        self.test_user = {"first_name": "test_first", "last_name": "test_last",
                          "username": "test_username", "password1": "test1234",
                          "password2": "test1234"}

        response = self.client.post(reverse("create_users"), self.test_user)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/login/")
