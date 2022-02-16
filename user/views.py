from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import login

def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()
        
        login(request, new_user)
        return redirect('index')

    context = {
        "form": form,
    }
    return render(request, "register.html", context)

    # if request.method=="POST":
    #     form = RegisterForm(request.POST)
    #     if form.is_valid():
    #         username = form.cleaned_data.get('username')
    #         password = form.cleaned_data.get('password')
    #         new_user = User(username=username)
    #         new_user.set_password(password)
    #         new_user.save()
            
    #         login(request, new_user)
    #         return redirect('index')

    #     context = {
    #         "form": form,
    #     }
    #     return render(request, "register.html", context)
        
    # else:    
    #     form = RegisterForm()
    #     context = {
    #         "form": form,
    #     }
    #     return render(request, "register.html", context)

def login_user(request):
    return render(request, "login.html")
    

def logout_user(request):
    return render(request, "login.html")
    
