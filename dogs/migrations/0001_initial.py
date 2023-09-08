# Generated by Django 4.2.4 on 2023-09-02 12:06

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
                ('name', models.CharField(max_length=100, verbose_name='порода')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'порода',
                'verbose_name_plural': 'породы',
            },
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Кличка')),
                ('image', models.ImageField(blank=True, null=True, upload_to='dogs/', verbose_name='Изображение')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dogs.category', verbose_name='Порода')),
            ],
            options={
                'verbose_name': 'собака',
                'verbose_name_plural': 'собаки',
            },
        ),
    ]
