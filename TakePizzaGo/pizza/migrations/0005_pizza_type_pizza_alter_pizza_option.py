# Generated by Django 4.2.6 on 2023-10-30 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0004_remove_pizza_crust_remove_pizza_pizza_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='type_pizza',
            field=models.CharField(default='Margherita', max_length=50),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='option',
            field=models.CharField(choices=[('Mica |Blat Normal|30', 'Mica |Blat Normal |30'), ('Medie|Blat Normal|42', ' Medie|Blat Normal |42'), ('Mare |Blat Normal|55', 'Mare |Blat Normal |55'), ('Mare |Blat Special|65', 'Mare |Blat Special|65')], default='Medie|Blat Normal|42', max_length=60),
        ),
    ]