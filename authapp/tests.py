from django.test import TestCase
from django.test.client import Client
from django.conf import settings

from authapp.models import ShopUser


class UserManagementTestCase(TestCase):
    username = 'django'
    email = 'django@gb.local'
    password = '1A!23456'
    status_code_success = 200
    status_code_redirect = 302

    new_user_data = {
        'username': 'django1',
        'first_name': 'Django',
        'last_name': 'Django',
        'password1': '1A!23456',
        'password2': '1A!23456',
        'age': 30,
        'email': 'django1@gb.local'
    }

    def SetUo(self):
        self.user = ShopUser.objects.create_superuser(username=self.username, email=self.email, password=self.password)
        self.client = Client()

    # def test_user_flow(self):
    #     self._test_login()
    #     self._test_user_register()
    # update 40 self.client.login(username=self.new_user_data['username'], password=self.new_user_data['password'])

    def _test_login(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, self.status_code_success)
        self.assertTrue(response.context['user'].is_anonymous)

        self.client.login(username=self.username, password=self.password)
        response = self.client.get('/auth/login/')
        # print(response.status_code)
        self.assertEqual(response.status_code, self.status_code_redirect)

    def _test_user_register(self):
        response = self.client.post('/auth/register/', data=self.new_user_data)
        self.assertEqual(response.status_code, self.status_code_redirect)

        new_user = ShopUser.objects.get(username=self.new_user_data['username'])

        activation_url = f'{settings.DOMAIN_NAME}/auth/verify/{new_user.email}/{new_user.activation_key}/'

        response = self.client.get(activation_url)
        self.assertEqual(response.status_code, self.status_code_success)

        new_user.refresh_from_db()
        self.assertTrue(new_user.is_active)
