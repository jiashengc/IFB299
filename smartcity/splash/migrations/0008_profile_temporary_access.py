# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-30 04:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('splash', '0007_auto_20171029_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='temporary_access',
            field=models.BooleanField(default=False),
        ),
    ]
