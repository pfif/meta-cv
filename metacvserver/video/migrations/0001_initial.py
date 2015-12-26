# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-04 10:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VideoIntroduction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=50)),
                ('youtube_id', models.CharField(max_length=11, unique=True)),
                ('end_introduction', models.DurationField()),
                ('current', models.BooleanField()),
            ],
        ),
    ]
