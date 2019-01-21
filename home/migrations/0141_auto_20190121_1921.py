# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-01-21 19:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0140_auto_20190121_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='midpointinternfeedback',
            name='intern_help_requests_frequency',
            field=models.CharField(choices=[('0', 'I have not asked for help'), ('U', 'Multiple times per day'), ('D', 'Once per day'), ('M', 'Multiple times per week'), ('W', 'Once per week'), ('B', 'Every other week')], default='0', max_length=1, verbose_name="How often do <b>you</b> ask for your mentor's help?"),
        ),
        migrations.AlterField(
            model_name='midpointmentorfeedback',
            name='intern_help_requests_frequency',
            field=models.CharField(choices=[('0', 'Intern has not asked for help'), ('U', 'Multiple times per day'), ('D', 'Once per day'), ('M', 'Multiple times per week'), ('W', 'Once per week'), ('B', 'Every other week')], default='0', max_length=1, verbose_name='How often does <b>your intern</b> ask for your help?'),
        ),
    ]
