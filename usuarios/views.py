from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.messages import constants
from django.contrib import messages, auth
import re



def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')

    elif request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if len(nome.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Campo vazio!')
            return render(request, 'cadastro.html')

        if senha != confirmar_senha:
            messages.add_message(request, constants.WARNING, 'As senhas devem ser iguais!')
            return render(request, 'cadastro.html', {'form': request.POST})

        if not re.search(r'^[a-zA-Z0-9._-]+@[a-z0-9]+\.[a-z]', email):
            messages.add_message(request, constants.ERROR, 'Digite um email válido!')
            return redirect(reverse('cadastro'), {'form': request.POST})

        while not (
            re.search(r'.{6,}', senha) and
            re.search(r'[A-Z]', senha) and
            re.search(r'\d', senha)
        ):
            messages.add_message(request, constants.INFO, 'Senha fora dos requisitos')
            return render(request, 'cadastro.html', )

        usuario = User.objects.filter(email=email)

        if usuario.exists():
            messages.add_message(request, constants.INFO, 'Já existe um usuário com este email!')
            return render(request, 'cadastro.html', {'form': request.POST})

        usuario = User.objects.create_user(username=nome, email=email, password=senha)
        usuario.save()
        messages.add_message(request, constants.SUCCESS, 'Cadastrado com sucesso!')
        return redirect(reverse('login'), {'form': request.POST})


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    elif request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        nome = User.objects.get(email=email).username
        usuario = auth.authenticate(username=nome, password=senha)

        if not usuario:
            messages.add_message(request, constants.ERROR, 'Senha incorreta!')
            return redirect(reverse('login'))

        auth.login(request, usuario)

        return redirect('/divulgar/novo_pet')


def logout(request):
    auth.logout(request)
    messages.add_message(request, constants.WARNING, 'Faça login para entrar no sistema!')
    return redirect(reverse('login'))


def handler404(request, exception):
    return render(request, 'not_found.html')
