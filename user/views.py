from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()
        
        login(request, new_user)
        messages.success(request, "Qeydiyyatdan keçdiniz!")
        return redirect('index')

    context = {
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = LoginForm(request.POST or None)
    
    context = {
        "form": form,
    }

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user=authenticate(username=username, password=password)
    
        if user is None:
            messages.warning(request, "İstifadəçi adı və ya parol səhvdir")
            return render(request, "login.html", context)

        messages.success(request, "Sayta giriş etdiniz")
        login(request, user)
        return redirect('index')

    return render(request, "login.html", context)
    

def logout_user(request):
    logout(request)
    messages.warning(request, "Saytdan çıxış etdiniz")
    return redirect('index')
    
