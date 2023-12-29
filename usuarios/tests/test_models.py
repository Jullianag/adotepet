from django.contrib.auth.models import User
from django.test import TestCase


class UsuariosTestCase(TestCase):

    def setUp(self):
        self.nome = User.objects.create(username='username', email='username@gmail.com', password='123456')

    def test_models_criado(self):
        usuario = User.objects.get(username='username', email='username@gmail.com', password='123456')

        self.assertEqual(self.nome, usuario)