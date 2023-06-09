from django.shortcuts import render
from shop.models import *


# Create your views here.

def welcome(request):
    return render(
        request,
        'shop/Welcome_page.html',
    )

def category(request):
    products = Product.objects.all()
    print(products[0].image)
    context = {'products':products}
    return render(
        request,
        'shop/category_page.html',
        context
    )

def product(request):
    return render(
        request,
        'shop/product_page.html',
    )