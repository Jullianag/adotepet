from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages import constants
from django.shortcuts import render, redirect
from django.urls import reverse

from adotar.models import PedidoAdocao
from divulgar.models import Pet, Raca
from django.core.mail import send_mail


@login_required
def listar_pets(request):
    if request.method == 'GET':
        pets = Pet.objects.filter(status='P')
        racas = Raca.objects.all()
        cidade = request.GET.get('cidade')
        raca_filter = request.GET.get('raca')
        nome = request.GET.get('nome')

        if cidade:
            # icontains para filtar mais eficiente (caracteres que contem dentro de cidade)
            pets = pets.filter(cidade__icontains=cidade)

        if raca_filter:
            pets = pets.filter(raca__id=raca_filter)
            raca_filter = Raca.objects.get(id=raca_filter)

        if nome:
            pets = pets.filter(nome__contains=nome)

        return render(request, 'listar_pets.html', {'pets': pets, 'racas': racas, 'cidade': cidade,
                                                    'raca_filter': raca_filter, 'nome': nome})


@login_required
def pedido_adocao(request, id_pet):
    pet = Pet.objects.filter(id=id_pet).filter(status='P')

    if not pet.exists():
        messages.add_message(request, constants.WARNING, 'Esse pet já foi adotado!')

    # first pega o primeiro da lista
    pedido = PedidoAdocao(pet=pet.first(),
                          usuario=request.user,
                          data=datetime.now())

    pedido.save()

    messages.add_message(request, constants.SUCCESS, 'Pedido de adoção realizado! Você receberá um email '
                                                     'caso ele seja aprovado.')

    return redirect('/adotar')


@login_required
def ver_pedido_adocao(request):
    if request.method == 'GET':
        pedidos = PedidoAdocao.objects.filter(usuario=request.user).filter(status='AG')
        return render(request, 'ver_pedido_adocao.html', {'pedidos': pedidos})


@login_required
def processa_pedido_adocao(request, id_pedido):
    status = request.GET.get('status')
    pedido = PedidoAdocao.objects.get(id=id_pedido)

    if status == 'A':
        pedido.status = 'AP'
        string = ''' Olá, seu pedido de adoção foi aprovado! '''
    elif status == 'R':
        string = ''' Olá, seu pedido de adoção foi recusado! '''
        pedido.status = 'R'

    pedido.save()

    # TODO: alterar status pet

    email = send_mail(
        'Sua adoção foi processada!',
        string,
        'juh_g@hotmail.com',
        [pedido.usuario.email]
    )

    messages.add_message(request, constants.SUCCESS, 'Pedido de adoção processado '
                                                     'com sucesso!')
    return redirect(reverse('ver_pedido_adocao'))