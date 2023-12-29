from django.http import HttpRequest
from django.test import TestCase
from usuarios.forms import FormUsuarios


class FormTestCase(TestCase):

    def setUp(self):
        self.form = FormUsuarios()

    def test_campos_form(self):
        self.assertIn('username', self.form.fields)
        self.assertIn('email', self.form.fields)
        self.assertIn('password', self.form.fields)

    def test_form_is_valid(self):
        request = HttpRequest()
        request.POST = {
            'username': 'username',
            'email': 'email@gmail.com',
            'password': '1234'
        }

        form = FormUsuarios(request.POST)
        self.assertTrue(form.is_valid())