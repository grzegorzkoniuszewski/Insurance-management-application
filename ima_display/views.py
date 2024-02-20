from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


# def hello(request):
#     return HttpResponse('Witaj w aplikacji do zarządzania polisami samochodowymi')


class StartPage(TemplateView):
    template_name = 'index.html'

# Create your views here.
