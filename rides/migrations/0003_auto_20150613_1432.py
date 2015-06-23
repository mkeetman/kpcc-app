# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0002_rides_ride_cancelled_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rides',
            name='ride_cancel_reason',
            field=models.ForeignKey(blank=True, null=True, to='rides.RideCancellations'),
        ),
        migrations.AlterField(
            model_name='rides',
            name='ride_cancelled',
            field=models.DateTimeField(blank=True, verbose_name='Cancellation Date & Time', null=True),
        ),
        migrations.AlterField(
            model_name='rides',
            name='ride_cancelled_by',
            field=models.ForeignKey(blank=True, null=True, related_name='RideCanceller', to='rides.RideLeader'),
        ),
    ]
