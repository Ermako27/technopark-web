from django.shortcuts import render


# Create your views here.
def register(request):
    return render(request, 'users/register.html', {'title': 'Registration'})


def login(request):
    return render(request, 'users/login.html', {'title': 'Login'})


def settings(request):
    return render(request, 'users/settings.html')