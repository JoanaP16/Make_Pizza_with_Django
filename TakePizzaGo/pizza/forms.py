from django.db import models
from django.forms import ModelForm
from .models import Pizza
from django import forms


class PizzaForm(ModelForm):
    class Meta:
        model=Pizza
        fields=['option']




