# Generated by Django 4.1.4 on 2023-03-15 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_image_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='product',
            name='main_image',
            field=models.ImageField(blank=True, default='GettyImages_1177471633.jpg', null=True, upload_to='products/'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, default='GettyImages_1177471633.jpg', null=True, upload_to='products/'),
        ),
    ]