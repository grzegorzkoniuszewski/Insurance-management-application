from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.db import IntegrityError
from accounts.forms import CustomCreateUserForm


def register_page(request):
    # Redirect to home if the user is already authenticated
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        # If the request method is POST, process the form
        form = CustomCreateUserForm(request.POST)
        if form.is_valid():
            # If form is valid, attempt to save the user
            username = form.cleaned_data.get("username")
            try:
                form.save()
                messages.success(request, f"Account was created for {username}.")
                return redirect("user_login")
            except IntegrityError:
                # Handle the case where the username already exists
                messages.error(request, "Username is already taken.")
    else:
        # If the request method is not POST, render the registration form
        form = CustomCreateUserForm()

    context = {"form": form}
    return render(request, "accounts/register.html", context)


def login_page(request):
    # Redirect to home if the user is already authenticated
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        # If the request method is POST, attempt to authenticate the user
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # If authentication is successful, log the user in
            login(request, user)
            return redirect("home")
        else:
            # If authentication fails, display error message
            messages.error(request, "Username or password is incorrect.")
    return render(request, "accounts/login.html")


def logout_user(request):
    # If the user is authenticated, log them out
    if request.user.is_authenticated:
        logout(request)
        return render(request, "accounts/logout.html")
    # If the user is not authenticated, redirect them to home
    return redirect("home")


@login_required
def profile(request):
    # Render the profile page only if the user is authenticated
    return render(request, "accounts/profile.html")
