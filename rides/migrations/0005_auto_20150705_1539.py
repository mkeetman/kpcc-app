# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rides', '0004_auto_20150613_1853'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rideleader',
            name='name',
        ),
        migrations.AddField(
            model_name='rideleader',
            name='phonenumber',
            field=models.CharField(max_length=10, blank=True),
        ),
        migrations.AddField(
            model_name='rideleader',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, default=1),
            preserve_default=False,
        ),
    ]
