# Generated by Django 5.0.6 on 2024-07-05 06:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topping',
            name='pizza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topping', to='pizzas.pizza'),
        ),
    ]
