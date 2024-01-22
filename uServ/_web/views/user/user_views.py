from django.shortcuts import render


def home(request):
    return render(request, 'user/index.html')

def login(request):
    return render(request, 'user/login/login.html')

def logout(request):
    return render(request, 'user/login/login.html')

def register(request):
    return render(request, 'user/register/register.html')