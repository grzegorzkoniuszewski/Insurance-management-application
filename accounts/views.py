from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from accounts.forms import CustomCreateUserForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.db import IntegrityError


def register_page(request):
    try:
        if request.user.is_authenticated:
            return redirect('mainpage')
        else:
            if request.method == 'POST':
                form = CustomCreateUserForm(request.POST)
                if form.is_valid():
                    username = form.cleaned_data.get('username')
                    try:
                        # Attempt to save the user
                        form.save()
                        user = form.cleaned_data.get('username')
                        messages.success(request, 'Account was created for ' + user)
                        return redirect('user_login')
                    except IntegrityError:
                        # Handle the case where the username already exists
                        messages.error(request, 'Username is already taken.')
            else:
                form = CustomCreateUserForm()

            context = {'form': form}
            return render(request, 'accounts/register.html', context)

    except Exception as e:
        # Log the exception or handle it appropriately
        messages.error(request, 'An error occurred during registration.')
        # You might want to log the exception for debugging purposes
        # logging.error(str(e))
        return redirect('mainpage')  # Redirect to a generic error page or home page


def login_page(request):
    if request.user.is_authenticated:
        return redirect('mainpage')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('mainpage')
            else:
                messages.info(request, 'Username or password is incorrect.')
        context = {}
        return render(request, 'accounts/login.html', context)


def logout_user(request):
    logout(request)
    return render(request, 'accounts/logout.html')


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')