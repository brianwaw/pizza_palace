from django.shortcuts import render, get_object_or_404, redirect
from .models import Pizza
from .forms import AddPizzaForm, AddToppingForm
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


def addpizza(request):
    if request.method == 'POST':
        form = AddPizzaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pizzas:addpizza')
    else:
        form = AddPizzaForm()

    all_pizza = Pizza.objects.all()
    context = {'all_pizza': all_pizza, 'form': form}

    return render(request, 'pizzas/addpizza.html', context)


def addtopping(request):
    selected_pizza = None
    if request.method == 'POST':
        form = AddToppingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pizzas:addtopping')
    else:
        form = AddToppingForm()

    context = {'form': form, 'selected_pizza': selected_pizza}
    return render(request, 'pizzas/addtopping.html', context)



