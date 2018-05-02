# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-30 20:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0011_auto_20180429_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='level',
            field=models.CharField(choices=[('EASY', 'Easy'), ('MEDIUM', 'Medium'), ('HARD', 'Hard')], default='EASY', max_length=10),
        ),
    ]