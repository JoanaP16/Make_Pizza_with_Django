# Generated by Django 4.2.6 on 2023-10-30 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0003_remove_pizza_bauturi_remove_pizza_blaturi_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza',
            name='crust',
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='pizza_type',
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='price',
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='size',
        ),
        migrations.AddField(
            model_name='pizza',
            name='option',
            field=models.CharField(choices=[('Mica|Blat Normal|30', 'Mica|Blat Normal|30'), ('Medie|Blat Normal|42', 'Medie|Blat Normal|42'), ('Mare|Blat Normal|55', 'Mare|Blat Normal|55'), ('Mare|Blat Special|65', 'Mare|Blat Special|65')], default='Medie|Blat Normal|42', max_length=60),
        ),
    ]