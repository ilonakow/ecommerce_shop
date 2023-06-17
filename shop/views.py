from django.shortcuts import render, get_object_or_404, redirect
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
    product = get_object_or_404(Product, pk=my_pk)

    if request.method == "GET":
        return render(
            request,
            'shop/product_page.html',
            context={
                'product': product,
            }
        )

    elif request.method == "POST":
        data = request.POST
        quantity = data.get('quantity')

        order = request.user.order_set.first()
        order_line = order.products.add(
            product,
            through_defaults={'quantity': quantity}
        )

        return redirect('cart:cart')
