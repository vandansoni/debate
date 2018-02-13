# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Discussion', '0002_auto_20180209_1002'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='added_by',
            field=models.ForeignKey(related_name=b'Comments', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='discussion',
            name='added_by',
            field=models.ForeignKey(related_name=b'discussions', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
