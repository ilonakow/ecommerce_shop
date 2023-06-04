from django.urls import path

from account import views

app_name = 'account'

urlpatterns = [
    # path('account/', views.account),
    path('login/', views.login_view, name='login_view'),
    path('home/', views.home, name='home_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('register/', views.register_view, name='register'),

]