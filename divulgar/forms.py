from django.forms import ModelForm
from divulgar.models import Pet


class FormPet(ModelForm):

    class Meta:
        model = Pet
        fields = ['usuario', 'foto', 'nome', 'descricao', 'estado', 'cidade', 'cep', 'rua',
                  'bairro', 'complemento', 'telefone', 'raca', 'status']