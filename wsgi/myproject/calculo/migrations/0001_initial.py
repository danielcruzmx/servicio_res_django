# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ispt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_fin', models.CharField(max_length=10)),
                ('fecha_ini', models.CharField(max_length=10)),
                ('tipo', models.CharField(max_length=10)),
                ('linferior', models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)),
                ('superior', models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)),
                ('bruto', models.DecimalField(null=True, max_digits=15, decimal_places=4, blank=True)),
                ('cuota', models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)),
                ('excedente', models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)),
                ('subsidio', models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Regla',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=2)),
                ('concepto', models.CharField(max_length=3)),
                ('variable', models.CharField(max_length=25)),
                ('valor', models.DecimalField(null=True, max_digits=7, decimal_places=2, blank=True)),
                ('descripcion', models.CharField(max_length=100)),
                ('formula', models.CharField(max_length=100)),
                ('jerarquias', models.CharField(max_length=100)),
                ('niveles', models.CharField(max_length=100)),
                ('nombramientos', models.CharField(max_length=100)),
                ('grupos', models.CharField(max_length=100)),
                ('tipo_calculo', models.CharField(max_length=25)),
                ('codigo_salida', models.CharField(max_length=5)),
            ],
        ),
    ]
