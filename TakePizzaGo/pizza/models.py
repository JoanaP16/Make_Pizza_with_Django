from django.db import models


class Pizza(models.Model):
    PIZZA_Option = [
        ('Mica |Blat Normal|30',  'Mica |Blat Normal |30'),
        ('Medie|Blat Normal|42',  'Medie|Blat Normal |42'),
        ('Mare |Blat Normal|55',  'Mare |Blat Normal |55'),
        ('Mare |Blat Special|65', 'Mare |Blat Special|65')
    ]
    type_pizza=models.CharField(max_length=50, default='Margherita')
    cantitate=models.IntegerField(default=0)
    option = models.CharField(max_length=60, choices=PIZZA_Option, default='Medie|Blat Normal|42')


    def __str__(self):
        return f'{self.type_pizza}'



