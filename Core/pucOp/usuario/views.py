from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("core:home")
        else:
            messages.error(request, "Usuário ou senha incorretos.")

    return render(request, "usuario/login.html")


def logout_view(request):
    logout(request)
    return redirect("usuario:login")


def cadastro_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Esse nome de usuário já existe.")
            return redirect("usuario:cadastro")

        User.objects.create_user(username=username, email=email, password=password)

        messages.success(request, "Conta criada com sucesso! Faça login.")
        return redirect("usuario:login")

    return render(request, "usuario/cadastro.html")