# Generated by Django 4.0.3 on 2022-04-20 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecomApp', '0009_cart_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='brand_name',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='category_name',
        ),
    ]
