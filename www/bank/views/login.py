from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, resolve_url, reverse
from ..forms import CustomAuthenticationForm

__all__ = ['login_view', 'logout_view']

from django.contrib.auth.views import LoginView


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)

        if form.is_valid():
            # Restablece el contador de intentos fallidos si el inicio de sesión es exitoso
            user = form.get_user()
            user.failed_login_attempts = 0
            user.save()
            login(request, user)
            if user.is_staff or user.is_superuser:
                return redirect(resolve_url('admin:index'))

            return redirect(resolve_url('bank:home'))
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect(resolve_url('bank:login'))
