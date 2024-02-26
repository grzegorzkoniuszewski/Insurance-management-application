from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db import IntegrityError


def register_page(request):
    try:
        if request.user.is_authenticated:
            return redirect("home")
        else:
            if request.method == "POST":
                form = UserCreationForm(request.POST)
                if form.is_valid():
                    username = form.cleaned_data.get("username")
                    try:
                        # Attempt to save the user
                        form.save()
                        user = form.cleaned_data.get("username")
                        messages.success(request, "Konto zostało utworzone dla " + user)
                        return redirect("user_login")
                    except IntegrityError:
                        # Handle the case where the username already exists
                        messages.error(request, "Nazwa użytkownika jest już zajęta.")
            else:
                form = UserCreationForm()

            context = {"form": form}
            return render(request, "register.html", context)
    except Exception as e:
        # Obsługa innych wyjątków, jeśli zachodzi taka potrzeba
        messages.error(request, "Wystąpił błąd podczas przetwarzania żądania rejestracji.")
        return redirect("home")  # Przekierowanie na stronę główną w przypadku błędu