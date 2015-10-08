# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('person', models.CharField(verbose_name='Pessoa', max_length=100)),
                ('action_type', models.IntegerField(choices=[(0, 'Create'), (1, 'Update'), (2, 'Delete'), (3, 'Detail')], verbose_name='Tipo da Ação')),
                ('date', models.DateTimeField(verbose_name='Data', auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('code', models.IntegerField(verbose_name='Código')),
                ('name', models.CharField(verbose_name='Nome', max_length=150)),
            ],
            options={
                'verbose_name': 'Pessoa',
                'verbose_name_plural': 'Pessoas',
            },
        ),
    ]
