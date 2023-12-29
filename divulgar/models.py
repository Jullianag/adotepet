from django.contrib.auth.models import User
from django.db import models


class Tag(models.Model):
    tag = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Tag'

    def __str__(self):
        return self.tag


class Raca(models.Model):
    raca = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Raca'

    def __str__(self):
        return self.raca


class Pet(models.Model):
    status_choice = (
        ('P', 'Para adoção'),
        ('A', 'Adotado')
    )

    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    foto = models.ImageField(upload_to='fotos_pets')
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    estado = models.CharField(max_length=50, default='Escolha o estado do pet')
    cidade = models.CharField(max_length=50)
    cep = models.CharField(max_length=9)
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    complemento = models.CharField(max_length=100)
    telefone = models.CharField(max_length=50)
    tags = models.ManyToManyField(Tag)
    raca = models.ForeignKey(Raca, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=1, choices=status_choice, default='P')

    class Meta:
        verbose_name_plural = 'Pet'

    def __str__(self):
        return self.nome