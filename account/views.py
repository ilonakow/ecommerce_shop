from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model

# Create your views here.
User = get_user_model()
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

def register_view(request):
    if request.method == "GET":
        return render(
            request,
            'account/register.html',
            )
    else:
        data = request.POST
        username = data.get('username')
        password1 = data.get('password1')
        password2 = data.get('password2')

        if password1 == password2:
            User.objects.create_user(
                username=username,
                password=password1
            )
        return redirect('account:login_view')


def logout_view(request):
    logout(request)
    return redirect('account:home')
