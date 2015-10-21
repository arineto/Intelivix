# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workload', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='workload',
            options={'verbose_name': 'Carga Horária', 'verbose_name_plural': 'Cargas Horária', 'ordering': ['day', 'user']},
        ),
    ]
