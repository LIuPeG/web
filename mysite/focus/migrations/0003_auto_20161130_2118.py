# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('focus', '0002_auto_20161130_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='qq',
            field=models.CharField(max_length=20, null=True, verbose_name=b'QQ\xe5\x8f\xb7\xe7\xa0\x81', blank=True),
        ),
    ]
