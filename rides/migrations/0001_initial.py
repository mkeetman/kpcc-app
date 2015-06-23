# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RideCancellations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('reason', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RideLeader',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Rides',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('ride_date', models.DateTimeField(verbose_name='Ride Date')),
                ('ride_destination', models.CharField(max_length=100)),
                ('ride_cancelled', models.DateTimeField(verbose_name='Cancellation Date & Time')),
                ('ride_cancel_reason', models.ForeignKey(to='rides.RideCancellations')),
                ('ride_leader_a', models.ForeignKey(to='rides.RideLeader', related_name='RideLeaderA')),
                ('ride_leader_b', models.ForeignKey(to='rides.RideLeader', related_name='RideLeaderB')),
            ],
        ),
    ]
