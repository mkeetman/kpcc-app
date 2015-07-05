# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0005_auto_20150705_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rides',
            name='ride_cancelled_by',
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, related_name='RideCanceller', blank=True),
        ),
        migrations.AlterField(
            model_name='rides',
            name='ride_leader_a',
            field=models.ForeignKey(verbose_name='Ride Leader', to=settings.AUTH_USER_MODEL, related_name='RideLeaderA'),
        ),
        migrations.AlterField(
            model_name='rides',
            name='ride_leader_b',
            field=models.ForeignKey(null=True, verbose_name='Secondary Ride Leader', to=settings.AUTH_USER_MODEL, related_name='RideLeaderB', blank=True),
        ),
    ]
