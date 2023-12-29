from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import Client
from django.urls import reverse


class ViewsTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url_novo = reverse('novo_pet')
        self.url_seus = reverse('seus_pets')
        self.url_d = reverse('dashboard')
        self.user = User.objects.create_user('usuario', 'usuario@gmail.com', '1234')

    def test_status_code_200(self):
        self.client.login(username='usuario', password='1234')
        response1 = self.client.get(self.url_seus)
        response2 = self.client.get(self.url_d)

        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 200)

    def test_template_used(self):
        self.client.login(username='usuario', password='1234')
        response1 = self.client.get(self.url_novo)
        response2 = self.client.get(self.url_seus)
        response3 = self.client.get(self.url_d)

        self.assertTemplateUsed(response1, 'novo_pet.html')
        self.assertTemplateUsed(response2, 'seus_pets.html')
        self.assertTemplateUsed(response3, 'dashboard.html')