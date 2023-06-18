from django.contrib import admin

from shop.models import Category, Product, Order, OrderLine

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderLine)
