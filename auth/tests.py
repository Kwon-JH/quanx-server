from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class AccountTests(APITestCase):

    TEST_USER = { 'username': 'testuser',
                  'email': 'test@example.com',
                  'password': 'testpassword'
                }

    def setUp(self):
        # We want to go ahead and originally create a user.
        self.test_user = User.objects.create_user(AccountTests.TEST_USER['username'],
                                                  AccountTests.TEST_USER['email'],
                                                  AccountTests.TEST_USER['password'],)

        # URL for creating an account.
        self.create_url = reverse('rest_register')
        self.login_url = reverse('rest_login')
        self.logout_url = reverse('rest_logout')

    def test_create_account(self):
        """
            Ensure creating a new account
        """

        password = 'somepassword'
        data = {
            'username': 'foobar',
            'email': 'foobar@example.com',
            'password1': password,
            'password2': password
        }

        response = self.client.post(self.create_url, data, format='json')

        # We want to make sure we have two users in the database..
        self.assertEqual(User.objects.count(), 2)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        user = response.data['user']
        self.assertEqual(user['username'], data['username'])
        self.assertEqual(user['email'], data['email'])
        self.assertFalse('password' in response.data)

    # def test_remove_account(self):
    #     self.assertTrue(True, "failed to remove an account.")

    def test_login(self):
        response = self.client.post(self.login_url,
                                    AccountTests.TEST_USER,
                                    format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in response.data)
        self.assertTrue('user' in response.data)

        user = response.data['user']
        self.assertTrue(user['username'], AccountTests.TEST_USER['username'])

    def test_logout(self):
        # response = self.client.post(self.login_url,
        #                             AccountTests.TEST_USER,
        #                             format='json')
        #
        # self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertTrue('token' in response.data)

        response = self.client.post(self.logout_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['detail'], 'Successfully logged out.')




