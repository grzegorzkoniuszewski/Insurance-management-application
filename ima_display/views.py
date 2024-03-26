from django.views.generic import TemplateView

class StartPage(TemplateView):
    # Klasa widoku strony startowej dziedzicząca po klasie TemplateView
    template_name = 'mainpage.html'
    # Ustawienie nazwy szablonu dla widoku

    def get_context_data(self, **kwargs):
        # Metoda pobierająca dane kontekstowe
        context = super().get_context_data(**kwargs)
        # Pobranie danych kontekstowych odziedziczonych z klasy nadrzędnej
        current_user = self.request.user
        # Pobranie aktualnego użytkownika
        context['current_user'] = current_user
        # Dodanie aktualnego użytkownika do danych kontekstowych
        return context
        # Zwrócenie danych kontekstowych
