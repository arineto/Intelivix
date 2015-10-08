# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='log',
            options={'verbose_name': 'Log', 'verbose_name_plural': 'Logs', 'ordering': ['-date']},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Pessoa', 'verbose_name_plural': 'Pessoas', 'ordering': ['-name']},
        ),
    ]
