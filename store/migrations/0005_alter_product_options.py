# Generated by Django 4.1.4 on 2023-03-24 00:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_product_amount'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-rating']},
        ),
    ]