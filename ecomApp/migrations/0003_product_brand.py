# Generated by Django 4.0.3 on 2022-04-16 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecomApp', '0002_category_category_image_alter_category_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecomApp.brand'),
        ),
    ]