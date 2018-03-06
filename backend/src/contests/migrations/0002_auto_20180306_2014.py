# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-06 20:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('contests', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='participants',
            field=models.ManyToManyField(to='accounts.Profile'),
        ),
        migrations.AlterField(
            model_name='contest',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='creator', to='accounts.Profile'),
        ),
    ]
