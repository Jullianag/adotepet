from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages import constants
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from adotar.models import PedidoAdocao
from divulgar.models import Tag, Raca, Pet
from django.views.decorators.csrf import csrf_exempt


@login_required
def novo_pet(request):
    if request.method == 'GET':

        tags = Tag.objects.all()
        racas = Raca.objects.all()

        return render(request, 'novo_pet.html', {'tags': tags, 'racas': racas})

    elif request.method == 'POST':
        foto = request.FILES.get('foto')
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        estado = request.POST.get('estado')
        cidade = request.POST.get('localidade')
        cep = request.POST.get('cep')
        bairro = request.POST.get('bairro')
        rua = request.POST.get('logradouro')
        complemento = request.POST.get('complemento')
        telefone = request.POST.get('telefone')
        tags = request.POST.getlist('tags')
        raca = request.POST.get('raca')

        pet = Pet(
            usuario=request.user,
            foto=foto,
            nome=nome,
            descricao=descricao,
            estado=estado,
            cidade=cidade,
            cep=cep,
            rua=rua,
            complemento=complemento,
            bairro=bairro,
            telefone=telefone,
            raca_id=raca,

        )

        pet.save()

        for tag_id in tags:
            tag = Tag.objects.get(id=tag_id)
            pet.tags.add(tag)

        tags = Tag.objects.all()
        racas = Raca.objects.all()

        if len(telefone.strip()) == 0:
            messages.add_message(request, constants.WARNING, 'O campo "telefone" não pode ser vazio!')
            return render(request, 'novo_pet.html', {'tags': tags, 'racas': racas})

        if not foto:
            messages.add_message(request, constants.WARNING, 'Você deve adicionar uma foto do pet!')
            return render(request, 'novo_pet.html', {'tags': tags, 'racas': racas})

        pet.save()

        messages.add_message(request, constants.SUCCESS, 'Pet cadastrado com sucesso!')
        return render(request, 'novo_pet.html', {'tags': tags, 'racas': racas})


@login_required
def seus_pets(request):
    if request.method == 'GET':
        pets = Pet.objects.filter(usuario=request.user)
        return render(request, 'seus_pets.html', {'pets': pets})


@login_required
def remover_pet(request, id):
    pet = Pet.objects.get(id=id)

    if not pet.usuario == request.user:
        messages.add_message(request, constants.ERROR, 'Esse pet não é seu!')
        return redirect(reverse('seus_pets'))

    pet.delete()
    messages.add_message(request, constants.SUCCESS, 'Pet removido com sucesso!')
    return redirect(reverse('seus_pets'))


@login_required
def ver_pet(request, id):
    if request.method == 'GET':
        pet = Pet.objects.get(id=id)
        return render(request, 'ver_pet.html', {'pet': pet})


@login_required
def dashboard(request):
    if request.method == "GET":
        return render(request, 'dashboard.html')


@csrf_exempt
def api_adocoes_por_raca(request):
    racas = Raca.objects.all()

    qtd_adocoes = []
    for raca in racas:
        adocoes = PedidoAdocao.objects.filter(pet__raca=raca).count()
        qtd_adocoes.append(adocoes)

    racas = [raca.raca for raca in racas]
    data = {'qtd_adocoes': qtd_adocoes,
            'labels': racas}

    return JsonResponse(data)