# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workload', '0002_auto_20151021_1757'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='action',
            options={'verbose_name': 'Ação', 'verbose_name_plural': 'Ações', 'ordering': ['time', 'status']},
        ),
    ]
