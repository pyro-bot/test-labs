# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-02 13:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=255)),
                ('sex', models.CharField(max_length=1)),
                ('age', models.IntegerField()),
            ],
        ),
    ]