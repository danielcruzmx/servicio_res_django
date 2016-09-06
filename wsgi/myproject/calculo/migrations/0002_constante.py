# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Constante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('constante', models.CharField(max_length=25)),
                ('valor', models.DecimalField(null=True, max_digits=7, decimal_places=2, blank=True)),
            ],
        ),
    ]
