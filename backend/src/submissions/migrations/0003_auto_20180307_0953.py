# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-07 09:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0002_auto_20180307_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contestsubmission',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contests.Participant'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile'),
        ),
    ]
