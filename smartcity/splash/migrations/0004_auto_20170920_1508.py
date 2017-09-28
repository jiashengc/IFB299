# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-20 05:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('splash', '0003_auto_20170920_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='description',
            field=models.CharField(default='', max_length=1080),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='location',
            name='type',
            field=models.CharField(choices=[('CL', 'College'), ('LI', 'Library'), ('IN', 'Industry'), ('HO', 'Hotel'), ('ZO', 'Zoo'), ('MU', 'Museum'), ('RE', 'Restaurant'), ('MA', 'Mall'), ('PA', 'Park')], max_length=2),
        ),
    ]
