from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.

def welcome(request):
    return render(
        request,
        'shop/Welcome_page.html',
    )

def category(request):
    return render(
        request,
        'shop/category_page.html',
    )

def product(request):
    return render(
        request,
        'shop/product_page.html',
    )