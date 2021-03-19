# Generated by Django 3.1.7 on 2021-03-19 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('product', '0001_initial'),
        ('subscription', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.product'),
        ),
        migrations.AddField(
            model_name='wishlist',
            name='subscription',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='subscription.subscription'),
        ),
        migrations.AddField(
            model_name='additionalinformation',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.account'),
        ),
    ]
