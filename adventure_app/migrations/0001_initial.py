# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-07-08 23:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('log_reg_adventure_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adventure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('destination', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('plan', models.TextField()),
                ('attending_adventure', models.ManyToManyField(related_name='pirates_attending_adventures_list', to='log_reg_adventure_app.User')),
                ('hosting_adventure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pirates_hosting_adventures_list', to='log_reg_adventure_app.User')),
            ],
        ),
    ]