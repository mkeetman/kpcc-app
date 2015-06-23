# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0003_auto_20150613_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='rideleader',
            name='shortname',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='rides',
            name='ride_description',
            field=models.TextField(blank=True, verbose_name='Ride Description or Additional Information'),
        ),
        migrations.AddField(
            model_name='rides',
            name='ride_expected_duration',
            field=models.DurationField(blank=True, verbose_name='Expected Ride Time', null=True),
        ),
        migrations.AddField(
            model_name='rides',
            name='ride_expected_length',
            field=models.FloatField(blank=True, verbose_name='Expected Ride Length', null=True),
        ),
        migrations.AddField(
            model_name='rides',
            name='ride_map',
            field=models.URLField(blank=True, verbose_name='Link to Ride Route'),
        ),
        migrations.AddField(
            model_name='rides',
            name='ride_parcours',
            field=models.CharField(choices=[('Flat', 'Flat: very little climbing'), ('Undulating', 'Undulating, constantly up and down short hills'), ('Hilly', 'Hilly: Long / steep climbs')], default='Undulating', verbose_name='Ride Parcours', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rides',
            name='ride_speed',
            field=models.CharField(choices=[('Easy', 'Easy Pace: 27-30Kmph on the flat, 25Kmph average'), ('Medium', 'Medium Pace: 30-33Kmph on the flat, 28Kmph average'), ('Fast', 'Fast Pace: 33Kmph+ on the flat, 30Kmph average')], default='Medium', verbose_name='Ride Speed', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rides',
            name='ride_destination',
            field=models.CharField(verbose_name='Ride Destination', max_length=100),
        ),
        migrations.AlterField(
            model_name='rides',
            name='ride_leader_a',
            field=models.ForeignKey(to='rides.RideLeader', verbose_name='Ride Leader', related_name='RideLeaderA'),
        ),
        migrations.AlterField(
            model_name='rides',
            name='ride_leader_b',
            field=models.ForeignKey(blank=True, to='rides.RideLeader', verbose_name='Secondary Ride Leader', related_name='RideLeaderB', null=True),
        ),
    ]
