from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import Client
from django.urls import reverse


class ViewsTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('cadastro')
        self.url2 = reverse('login')
        self.user = User.objects.create_user('usuario', 'usuario@gmail.com', '1234')

    def test_status_code_200(self):
        response = self.client.get(self.url)
        response2 = self.client.get(self.url2)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response2.status_code, 200)

    def test_template_used(self):
        response = self.client.get(self.url)
        response2 = self.client.get(self.url2)

        self.assertTemplateUsed(response, 'cadastro.html')
        self.assertTemplateUsed(response2, 'login.html')

    def test_login(self):
        self.client.login(username='usuario', password='1234')
        response = self.client.get(reverse('novo_pet'))

        self.assertEqual(response.status_code, 200)



