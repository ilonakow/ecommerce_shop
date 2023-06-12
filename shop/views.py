from django.shortcuts import render, get_object_or_404
from shop.models import *


# Create your views here.

def welcome(request):
    return render(
        request,
        'shop/Welcome_page.html',
    )

def category(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(
        request,
        'shop/category_page.html',
        context
    )

def product(request, my_pk):
    # task = Task.objects.get(id=pk)
    product = get_object_or_404(Product, pk=my_pk)

    return render(
        request,
        'shop/product_page.html',
        context={
            'product': product,
        }
    )