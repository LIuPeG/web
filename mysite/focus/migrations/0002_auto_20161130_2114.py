# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('focus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='avator',
            field=models.ImageField(default=b'avator/default.png', upload_to=b'avator/%Y/%m', max_length=200, blank=True, null=True, verbose_name=b'\xe5\xa4\xb4\xe5\x83\x8f'),
        ),
        migrations.AddField(
            model_name='newuser',
            name='qq',
            field=models.CharField(max_length=20, null=True, verbose_name=b'QQh\xe5\x8f\xb7\xe7\xa0\x81', blank=True),
        ),
    ]
