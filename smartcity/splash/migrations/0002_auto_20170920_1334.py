# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-20 03:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('splash', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='cities',
            new_name='city',
        ),
        migrations.AlterField(
            model_name='location',
            name='type',
            field=models.CharField(choices=[('CL', 'College'), ('LI', 'Library'), ('IN', 'Industry'), ('HO', 'Hotel'), ('ZO', 'Zoo'), ('MU', 'Musuem'), ('RE', 'Restaurant'), ('MA', 'Mall'), ('PK', 'Park')], max_length=2),
        ),
    ]