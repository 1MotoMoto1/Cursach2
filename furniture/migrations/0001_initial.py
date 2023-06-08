# Generated by Django 4.0.4 on 2022-05-28 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artikle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('artikle', models.CharField(max_length=30, verbose_name='Артикул')),
            ],
            options={
                'verbose_name': 'Автикл',
                'verbose_name_plural': 'Артиклы',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('photo', models.ImageField(upload_to='colors/', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Цвет',
                'verbose_name_plural': 'Цвета',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('photo', models.ImageField(upload_to='products/', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группы',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('width', models.PositiveIntegerField(verbose_name='Ширина')),
                ('height', models.PositiveIntegerField(verbose_name='Высота')),
                ('depth', models.PositiveIntegerField(verbose_name='Глубина')),
                ('coast', models.PositiveIntegerField(verbose_name='Цена')),
                ('ffrancia', models.PositiveIntegerField(verbose_name='Гарантия')),
                ('photo', models.ImageField(upload_to='products/', verbose_name='Фото')),
                ('artikle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='furniture.artikle', verbose_name='Артикул')),
                ('colors', models.ManyToManyField(to='furniture.color', verbose_name='Основной цвет')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='furniture.group', verbose_name='Группа')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукт',
            },
        ),
    ]