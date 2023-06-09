# Generated by Django 4.1.4 on 2023-03-15 02:02

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('name', models.CharField(max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('description', models.TextField()),
                ('material', models.CharField(blank=True, max_length=250, null=True)),
                ('height', models.IntegerField()),
                ('collar', models.IntegerField()),
                ('shoulder', models.IntegerField()),
                ('chest', models.IntegerField()),
                ('waist', models.IntegerField()),
                ('hips', models.IntegerField()),
                ('wrist', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('name', models.CharField(max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('name', models.CharField(max_length=250)),
                ('category', models.CharField(blank=True, max_length=250, null=True)),
                ('clothes_for', models.CharField(blank=True, choices=[('b', 'Boy'), ('g', 'Girl'), ('w', 'Women')], max_length=250, null=True)),
                ('price', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('color', models.ManyToManyField(to='store.size')),
                ('detail', models.ManyToManyField(blank=True, to='store.detail')),
                ('size', models.ManyToManyField(to='store.color')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('image', models.ImageField(upload_to='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
    ]
