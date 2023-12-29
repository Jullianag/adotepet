from django.contrib.auth.models import User
from django.test import TestCase
from divulgar.models import Pet, Raca


class DivulgarTestCase(TestCase):

    def setUp(self):
        racas = Raca.objects.create(raca='racas')
        user = User.objects.create_user(username='username', email='email@gmail.com', password='1234')
        self.nome = Pet.objects.create(usuario=user, foto='foto', nome='nome', descricao='descricao',
                                       estado='estado', cidade='cidade', cep='31245678', rua='rua',
                                       bairro='bairro', complemento='comp', telefone='123456789',
                                       raca=racas, status='X')

    def test_model_criar_no_banco(self):
        pet = Pet.objects.get(usuario='1', foto='foto', nome='nome', descricao='descricao',
                              estado='estado', cidade='cidade', cep='31245678', rua='rua',
                              bairro='bairro', complemento='comp', telefone='123456789', status='X',
                              raca='1')

        self.assertEqual(self.nome, pet)
