# Generated by Django 3.2.15 on 2022-08-30 10:49
from django.contrib.auth import get_user_model
from django.db import migrations, models
import django.db.models.deletion

User = get_user_model


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                (
                    'image',
                    models.ImageField(blank=True, null=True, upload_to='media/blog/', verbose_name='Изображение')),
                ('short_description', models.CharField(max_length=255, verbose_name='Краткого описания')),
                ('description', models.TextField(verbose_name='Полного описания')),
                ('created', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Блог',
                'verbose_name_plural': 'Блоги',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('photo',
                 models.ImageField(blank=True, null=True, upload_to='media/category/', verbose_name='Изображение')),
                ('created', models.DateField(auto_now_add=True)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories',
                                           to='blog.blog', verbose_name='Блог')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['-created'],
            },
        ),
    ]
