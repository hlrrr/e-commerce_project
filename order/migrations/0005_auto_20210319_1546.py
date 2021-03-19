# Generated by Django 3.1.7 on 2021-03-19 15:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20210319_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessoncart',
            name='attending_date',
            field=models.DateField(default=datetime.datetime(2021, 3, 19, 15, 46, 49, 125749), null=True, verbose_name='attending_date'),
        ),
        migrations.AlterField(
            model_name='productcart',
            name='delivery_date',
            field=models.DateField(default=datetime.datetime(2021, 3, 19, 15, 46, 49, 124697), null=True, verbose_name='delivery_date'),
        ),
        migrations.AlterField(
            model_name='subscriptioncart',
            name='delivery_date',
            field=models.DateField(default=datetime.datetime(2021, 3, 19, 15, 46, 49, 125200), null=True, verbose_name='delivery_date'),
        ),
        migrations.AlterModelTable(
            name='subscriptioncart',
            table='subscription_carts',
        ),
    ]
