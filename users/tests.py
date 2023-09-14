from django.urls import reverse
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User


class UserRegistrationTests(APITestCase):

    def test_customer_registration(self):
        url = reverse('register')
        data = {
            'email': 'customer@example.com',
            'username': 'customer_user',
            'password': 'customer_password',
            'role': User.Role.CUSTOMER
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().role, User.Role.CUSTOMER)


class UserLoginTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='user@example.com',
            username='test_user',
            password='test_password',
            role=User.Role.CUSTOMER
        )

    def test_user_login(self):
        url = reverse('token_obtain_pair')
        data = {
            'username': 'test_user',
            'password': 'test_password'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_invalid_user_login(self):
        url = reverse('token_obtain_pair')
        data = {
            'username': 'test_user',
            'password': 'incorrect_password'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class CreateStuffUserViewTestCase(APITestCase):
    def setUp(self):
        # Create a SUPERADMIN user
        self.superadmin_user = User.objects.create_user(
            email='stuff@example.com',
            username='superadmin',
            password='superadminpassword',
            role=User.Role.SUPERADMIN
        )
        # Create a CUSTOMER user
        self.user = User.objects.create_user(
            email='user@example.com',
            username='customer_user',
            password='customer_password',
            role=User.Role.CUSTOMER
        )
        # STUFF data
        self.data = {
            'email': 'stuff@example.com',
            'username': 'stuffuser',
            'password': 'stuffpassword',
            'role': User.Role.STUFF  # Ensure the role is set to STUFF
        }

    def test_create_stuff_user(self):
        # Define the data for creating a new STUFF user

        # Create a JWT token for the SUPERADMIN user
        refresh = RefreshToken.for_user(self.superadmin_user)
        access_token = str(refresh.access_token)

        # Include the JWT token in the HTTP headers
        headers = {'Authorization': f'Bearer {access_token}'}
        # Send a POST request to create the new STUFF user with JWT token authentication
        url = reverse('create-stuff')  # Use the name of the URL pattern

        response = self.client.post(url, self.data, format='json', headers=headers)

        # Assert that the response status code is 201 (Created)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert that the new user was created in the database
        self.assertTrue(User.objects.filter(username='stuffuser').exists())

    def test_permission_invalid_create_stuff_user(self):

        # Create a JWT token for the Customer user
        refresh = RefreshToken.for_user(self.user)
        access_token = str(refresh.access_token)
        # Include the JWT token in the HTTP headers
        headers = {'Authorization': f'Bearer {access_token}'}
        # Send a POST request to create the new STUFF user with JWT token authentication
        url = reverse('create-stuff')  # Use the name of the URL pattern
        response = self.client.post(url, self.data, format='json', headers=headers)
        # Assert that the response status code is 401 (UNAUTHORIZED )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)



class CreateSuperUserUserViewTestCase(APITestCase):
    def setUp(self):
        # Create a SUPERADMIN user
        self.superadmin_user = User.objects.create_user(
            email='superadmin@example.com',
            username='superadmin',
            password='superadminpassword',
            role=User.Role.SUPERADMIN
        )
        # Create a CUSTOMER user
        self.user = User.objects.create_user(
            email='user@example.com',
            username='customer_user',
            password='customer_password',
            role=User.Role.CUSTOMER
        )
        # STUFF data
        self.data = {
            'email': 'superadmin1@example.com',
            'username': 'superadmin1',
            'password': 'superadminpassword',
            'role': User.Role.SUPERADMIN  # Ensure the role is set to STUFF
        }

    def test_create_stuff_user(self):
        # Define the data for creating a new STUFF user

        # Create a JWT token for the SUPERADMIN user
        refresh = RefreshToken.for_user(self.superadmin_user)
        access_token = str(refresh.access_token)

        # Include the JWT token in the HTTP headers
        headers = {'Authorization': f'Bearer {access_token}'}
        # Send a POST request to create the new SUPER ADMIN user with JWT token authentication
        url = reverse('create-superadmin')  # Use the name of the URL pattern

        response = self.client.post(url, self.data, format='json', headers=headers)

        # Assert that the response status code is 201 (Created)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert that the new user was created in the database
        self.assertTrue(User.objects.filter(username='superadmin1').exists())

    def test_permission_invalid_create_stuff_user(self):

        # Create a JWT token for the Customer user
        refresh = RefreshToken.for_user(self.user)
        access_token = str(refresh.access_token)
        # Include the JWT token in the HTTP headers
        headers = {'Authorization': f'Bearer {access_token}'}
        # Send a POST request to create the new STUFF user with JWT token authentication
        url = reverse('create-superadmin')  # Use the name of the URL pattern
        response = self.client.post(url, self.data, format='json', headers=headers)
        # Assert that the response status code is 401 (UNAUTHORIZED )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


