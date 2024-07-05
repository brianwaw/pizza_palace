from django.urls import path
from . import views

app_name = 'pizzas'

urlpatterns = [
    path('', views.home_view, name="home"),
    path('<str:pizza_name>/', views.topping_view, name="topping"),
    path('contacts/', views.contacts_view, name="contacts"),
]
