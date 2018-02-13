# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Discussion', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='added_by',
        ),
        migrations.RemoveField(
            model_name='discussion',
            name='added_by',
        ),
    ]
