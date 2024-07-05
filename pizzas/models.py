from django.db import models


class Pizza(models.Model):
    """the type of pizza"""
    name = models.CharField(max_length=50)
    description = models.TextField(default='For the love of satisfaction and sweetness')

    class Meta:
        verbose_name_plural = 'pizzas'

    def __str__(self):
        if len(self.description) > 20:
            desc = f"{self.description[:20]}..."
        else:
            desc = self.description
        return f"{self.name} - {desc}"


class Topping(models.Model):
    """the toppings associated with the pizza"""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, related_name='topping')
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'toppings'

    def __str__(self):
        """what to print when Topping model is called"""
        return self.name




