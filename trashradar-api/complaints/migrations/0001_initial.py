# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 23:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('twitter', models.CharField(max_length=20)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('template_message', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Entity',
            },
        ),
    ]
