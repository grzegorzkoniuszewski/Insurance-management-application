from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Widok StartPage oparty na klasie TemplateView

class StartPage(TemplateView):
    # Definicja klasy StartPage dziedziczącej po klasie TemplateView

    template_name = 'mainpage.html'
    # Zdefiniowanie nazwy szablonu, który będzie renderowany przez ten widok

    def get_context_data(self, **kwargs):
        # Metoda do pobierania kontekstu danych dla szablonu

        context = super().get_context_data(**kwargs)
        # Pobranie kontekstu z klasy nadrzędnej

        current_user = self.request.user
        # Pobranie informacji o aktualnym użytkowniku

        context['current_user'] = current_user
        # Dodanie informacji o aktualnym użytkowniku do kontekstu

        return context
        # Zwrócenie kontekstu danych
