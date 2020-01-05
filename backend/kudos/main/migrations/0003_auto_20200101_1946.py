# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2020-01-01 19:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20191230_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='members',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]