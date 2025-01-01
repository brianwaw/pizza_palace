from django import forms
from .models import Pizza, Topping


class AddPizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['name', 'description']


class AddToppingForm(forms.ModelForm):
    pizza = forms.ModelChoiceField(queryset=Pizza.objects.all(), to_field_name="name", empty_label="Select a Pizza")

    class Meta:
        model = Topping
        fields = ['pizza', 'name']