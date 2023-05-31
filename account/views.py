from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def account(request):
    return render(
        request,
        'account/account.html',
    )

def home(request):
    return render(
        request,
        'account/home.html',
    )

def login_view(request):
    if request.method=="GET":
        return render(
            request,
            'account/account.html',

    )
    elif request.metod=="POST":
        data = request.POST
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user=user)

        return redirect('account:home')


def logout_view(request):
    logout(request)
    return redirect('account:home')
