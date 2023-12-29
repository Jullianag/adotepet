from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail


def envia_email(request):
    send_mail('Adoção', 'Aprovação para adoção.', 'juh_g@hotmail.com',
              ['jullianagnecco@gmail.com'])

    return HttpResponse('teste')