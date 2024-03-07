from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


# def hello(request):
#     return HttpResponse('Witaj w aplikacji do zarządzania polisami samochodowymi')


class StartPage(TemplateView):
    template_name = 'mainpage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user = self.request.user
        context['current_user'] = current_user
        return context
