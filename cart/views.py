from django.shortcuts import render
from shop.models import *
from django.shortcuts import render
# Create your views here.


def cart(request):
    products = []
    if request.method == "POST":
        data = request.POST
        if request.user.is_authenticated:
            order = Order.objects.create(
                customer=request.user
            )


            order.products.add(...)


    elif request.method=="GET":

        return render(
            request,
            'cart/cart_page.html',
            context={'products': products}
        )