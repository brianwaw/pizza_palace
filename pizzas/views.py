from django.shortcuts import render, get_object_or_404
from .models import Pizza
# Create your views here.


def home_view(request):
    all_pizzas = Pizza.objects.all()
    context = {'all_pizzas': all_pizzas}
    return render(request, 'pizzas/home.html', context)


def topping_view(request, pizza_name):
    pizza = get_object_or_404(Pizza, name__iexact=pizza_name)
    context = {'pizza': pizza}
    return render(request, 'pizzas/topping.html', context)


def contacts_view(request):
    return render(request, 'pizzas/contacts.html')


