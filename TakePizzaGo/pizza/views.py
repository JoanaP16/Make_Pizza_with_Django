from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pizza
from .forms import PizzaForm

pizza_type = [{'id': 1,
               'type': 'carnivora',
               'pret': 39
               },
              {'id': 2,
               'type': 'branza',
               'pret': 42
               },
              {'id': 3,
               'type': 'vegan',
               'pret': 41}]


def choose_pizza(request):
    pizza_type = Pizza.objects.all()

    form=PizzaForm()
    context={'pizza': pizza_type, 'form':form}

    return render(request, 'pizza/choose_pizza.html', context)


def adauga_pizza(request, pk):
    pizza = Pizza.objects.get(pk=int(pk))
    pizza.cantitate += 1
    return redirect('home')

def elimina_pizza(request, pk):
    pizza = Pizza.objects.get(pk=int(pk))
    if pizza.cantitate:
        pizza.cantitate -= 1
    else:
        pizza.cantitate=0
    return redirect('home')


def about (request):
    return render(request, 'pizza/about.html')
