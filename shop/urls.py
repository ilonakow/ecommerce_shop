from django.urls import path

from shop import views

app_name = 'shop'

urlpatterns = [
    path('welcome/', views.welcome, name="welcome"),
    path('category/', views.category, name="category"),
    path('product/<int:my_pk>/', views.product, name="product"),

]
url_patterns=[
    ...


]