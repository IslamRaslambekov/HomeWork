from django.contrib.auth.models import User
from django.test import Client, TestCase
from mixer.backend.django import mixer

from .models import *


class ViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.doctor = mixer.blend(Doctor)
        User.objects.create_user(
            username='test_user',
            is_staff=True,
            email='test@email.ru',
            password='0000'
        )
        User.objects.create_superuser(
            username='test_super_user',
            email='test@email.ru',
            password='0000'
        )

    def test_status_code_main_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_status_code_add_doctors(self):
        response = self.client.get('/add_doctors/')
        self.assertEqual(response.status_code, 302)

    def test_status_code_add_doctors_auth(self):
        self.client.login(
            username='test_user',
            password='0000'
        )
        response = self.client.get('/add_doctors/')
        self.assertEqual(response.status_code, 200)

    def test_status_code_add_doctors_post_request(self):
        response = self.client.post(
            '/add_doctors/',
            {'name': 'user',
             'last_name': 'last_name_user',
             'title': 'Dentist'}
        )
        self.assertEqual(response.status_code, 302)

    def test_status_code_add_doctors_post_request_auth(self):
        self.client.login(
            username='test_user',
            password='0000'
        )
        response = self.client.post(
            '/add_doctors/',
            {'name': 'user',
             'last_name': 'last_name_user',
             'title': 'Dentist'}
        )
        self.assertEqual(response.status_code, 200)