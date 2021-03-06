# Generated by Django 3.2.8 on 2021-10-21 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('image', models.ImageField(upload_to='allProducts/')),
            ],
        ),
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.TextField(max_length=12)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='allProducts/')),
                ('color', models.CharField(max_length=50)),
                ('dimensions', models.CharField(max_length=50)),
                ('weight', models.CharField(max_length=50)),
                ('material', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=300)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.category')),
            ],
        ),
        migrations.CreateModel(
            name='Offers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='offers/')),
                ('color', models.CharField(max_length=50)),
                ('dimensions', models.CharField(max_length=50)),
                ('weight', models.CharField(max_length=50)),
                ('material', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=300)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.category')),
            ],
        ),
        migrations.CreateModel(
            name='NewArrivals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='newArivals/')),
                ('color', models.CharField(max_length=50)),
                ('dimensions', models.CharField(max_length=50)),
                ('weight', models.CharField(max_length=50)),
                ('material', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=300)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.category')),
            ],
        ),
    ]
