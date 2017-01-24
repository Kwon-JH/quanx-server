# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-24 12:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    # replaces = [('manseCalendar', '0001_squashed_0004_auto_20170104_2129'), ('manseCalendar', '0004_auto_20170118_1705'), ('manseCalendar', '0005_day_day_of_week'), ('manseCalendar', '0006_auto_20170123_1654')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SolarTerm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('name', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('year', models.PositiveSmallIntegerField(null=True)),
                ('month', models.PositiveSmallIntegerField(null=True)),
                ('day', models.PositiveSmallIntegerField(null=True)),
                ('year_heaven_letter', models.CharField(max_length=6, null=True)),
                ('year_ground_letter', models.CharField(max_length=6, null=True)),
                ('month_heaven_letter', models.CharField(max_length=6, null=True)),
                ('day_heaven_letter', models.CharField(max_length=6, null=True)),
                ('day_ground_letter', models.CharField(max_length=6, null=True)),
                ('is_lunar_leap_month', models.BooleanField(default=False)),
                ('is_solar_term', models.BooleanField(default=False)),
                ('lunar_day', models.PositiveSmallIntegerField(null=True)),
                ('lunar_month', models.PositiveSmallIntegerField(null=True)),
                ('lunar_year', models.PositiveSmallIntegerField(null=True)),
                ('month_ground_letter', models.CharField(max_length=6, null=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='day',
            options={'ordering': ['date']},
        ),
        migrations.AlterModelOptions(
            name='solarterm',
            options={'ordering': ['time']},
        ),
        migrations.AddField(
            model_name='day',
            name='week_day',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]
