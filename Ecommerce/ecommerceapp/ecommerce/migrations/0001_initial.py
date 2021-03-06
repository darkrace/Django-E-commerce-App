# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-13 19:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PName', models.CharField(max_length=200)),
                ('Price', models.CharField(max_length=200)),
                ('Item', models.CharField(max_length=200)),
                ('Image', models.FileField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Password', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='Name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.Registration'),
        ),
        migrations.AddField(
            model_name='product',
            name='Prod',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.PProduct'),
        ),
    ]
