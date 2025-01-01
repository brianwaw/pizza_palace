from django.urls import path
from . import views

app_name = 'pizzas'

urlpatterns = [
    path('', views.home_view, name="home"),

    path('contacts/', views.contacts_view, name="contacts"),
    path('addpizza/', views.addpizza, name="addpizza"),
    path('addtopping/', views.addtopping, name="addtopping"),
    path('<str:pizza_name>/', views.ToppingView.as_view(), name="topping"),
]

