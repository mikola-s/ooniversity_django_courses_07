# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-25 17:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('surname', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('date_of_birth', models.DateField(verbose_name='Дата рождения')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20, verbose_name='Контактный телефон')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('skype', models.CharField(max_length=20)),
                ('courses', models.ManyToManyField(to='courses.Course', verbose_name='Курсы')),
            ],
        ),
    ]
