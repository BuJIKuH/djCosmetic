# Generated by Django 4.1.2 on 2022-10-22 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorylinemodels',
            name='slug',
            field=models.SlugField(blank=True, max_length=150, verbose_name='Слаг'),
        ),
        migrations.AddField(
            model_name='productsmodel',
            name='slug',
            field=models.SlugField(blank=True, max_length=150, verbose_name='Слаг'),
        ),
    ]
