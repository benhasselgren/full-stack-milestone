# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-28 12:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0003_auto_20180526_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='status',
            field=models.CharField(choices=[('todo', 'To do'), ('doing', 'Doing'), ('done', 'Done')], default='todo', max_length=5),
        ),
    ]
