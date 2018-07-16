# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-23 06:41
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_auto_20160423_0437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formfield',
            name='page',
            field=modelcluster.fields.ParentalKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='form_fields', to='home.FormPage'),
            preserve_default=False,
        ),
    ]
