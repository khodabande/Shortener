# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('title_fa', models.CharField(max_length=200, null=True, verbose_name='Title')),
                ('title_en', models.CharField(max_length=200, null=True, verbose_name='Title')),
                ('url', models.URLField(unique=True)),
                ('slug', models.CharField(verbose_name='Slug', unique=True, max_length=4, editable=False, blank=True)),
                ('views_count', models.PositiveIntegerField(default=0, verbose_name='Views Count', editable=False)),
                ('submit_time', models.DateTimeField(auto_now_add=True, verbose_name='Submit Time')),
                ('last_change', models.DateTimeField(auto_now=True, verbose_name='Last Change')),
            ],
            options={
                'ordering': ('submit_time',),
                'get_latest_by': 'submit_time',
                'verbose_name': 'Short Link',
                'verbose_name_plural': 'Short Links',
            },
        ),
    ]
