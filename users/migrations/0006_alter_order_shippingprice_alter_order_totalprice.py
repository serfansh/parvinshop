# Generated by Django 4.1.4 on 2023-03-25 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_order_shippingprice_alter_order_totalprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shippingPrice',
            field=models.IntegerField(blank=True, default=15000, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='totalPrice',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
