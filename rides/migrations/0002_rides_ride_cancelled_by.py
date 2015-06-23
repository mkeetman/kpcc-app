# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rides',
            name='ride_cancelled_by',
            field=models.ForeignKey(related_name='RideCanceller', default=0, to='rides.RideLeader'),
            preserve_default=False,
        ),
    ]
