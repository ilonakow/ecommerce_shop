from django.urls import path

from shop import views

urlpatterns = [
    path('welcome/', views.welcome),
    path('category/', views.category),
    path('product/', views.product),



]
