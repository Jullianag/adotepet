from django.contrib.auth.models import User
from django.forms import ModelForm


class FormUsuarios(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

