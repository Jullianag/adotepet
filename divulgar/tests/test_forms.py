from django.contrib.auth.models import User
from django.http import HttpRequest
from django.test import TestCase
from divulgar.forms import FormPet
from divulgar.models import Pet, Raca


class FormTestCase(TestCase):

    def setUp(self):
        self.form = FormPet()

    def test_campos_form(self):
        self.assertIn('usuario', self.form.fields)
        self.assertIn('foto', self.form.fields)
        self.assertIn('nome', self.form.fields)
        self.assertIn('descricao', self.form.fields)
        self.assertIn('estado', self.form.fields)
        self.assertIn('cidade', self.form.fields)
        self.assertIn('cep', self.form.fields)
        self.assertIn('rua', self.form.fields)
        self.assertIn('bairro', self.form.fields)
        self.assertIn('complemento', self.form.fields)
        self.assertIn('telefone', self.form.fields)
        self.assertIn('raca', self.form.fields)
        self.assertIn('status', self.form.fields)


