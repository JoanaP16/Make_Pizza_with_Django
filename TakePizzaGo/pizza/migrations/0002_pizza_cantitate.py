# Generated by Django 4.2.6 on 2023-10-30 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='cantitate',
            field=models.IntegerField(default=0),
        ),
    ]