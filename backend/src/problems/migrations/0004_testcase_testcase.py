# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-06 15:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0003_testcase_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='testcase',
            name='testcase',
            field=models.IntegerField(default=1, unique=True),
            preserve_default=False,
        ),
    ]