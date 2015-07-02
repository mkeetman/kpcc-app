#import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class RideLeader(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)
    shortname = models.CharField(max_length=20, blank=True)

class RideCancellations(models.Model):

    def __str__(self):
        return self.reason

    reason = models.CharField(max_length=100)

class Rides(models.Model):

    PARCOURS_CHOICES = (
        ('Flat','Flat: very little climbing'),
        ('Undulating', 'Undulating, constantly up and down short hills'),
        ('Hilly', 'Hilly: Long / steep climbs'),

    )
    SPEED_CHOICES = (
         ('Easy', 'Easy Pace: 27-30Kmph on the flat, 25Kmph average'),
         ('Medium', 'Medium Pace: 30-33Kmph on the flat, 28Kmph average'),
         ('Fast', 'Fast Pace: 33Kmph+ on the flat, 30Kmph average'),

    )

    def __str__(self):
        return str(self.ride_date) + ': ' + self.ride_destination

    ride_leader_a = models.ForeignKey(RideLeader, related_name='RideLeaderA', verbose_name='Ride Leader')
    ride_leader_b = models.ForeignKey(RideLeader,
                                      related_name='RideLeaderB',
                                      verbose_name='Secondary Ride Leader',
                                      null=True, blank=True)
    ride_date = models.DateTimeField(verbose_name='Ride Date')
    ride_destination = models.CharField(max_length=100, verbose_name='Ride Destination')
    ride_map = models.URLField(verbose_name='Link to Ride Route', blank=True)
    ride_parcours = models.CharField(max_length=30, choices=PARCOURS_CHOICES, verbose_name='Ride Parcours')
    ride_speed = models.CharField(max_length=10, choices=SPEED_CHOICES, verbose_name='Ride Speed')
    ride_description = models.TextField(blank=True, verbose_name='Ride Description or Additional Information')
    ride_expected_duration = models.DurationField(null=True, blank=True, verbose_name='Expected Ride Time')
    ride_expected_length = models.FloatField(null=True, blank=True, verbose_name='Expected Ride Length')
    ride_cancelled = models.DateTimeField('Cancellation Date & Time', null=True, blank=True)
    ride_cancel_reason = models.ForeignKey(RideCancellations, null=True, blank=True)
    ride_cancelled_by = models.ForeignKey(RideLeader, related_name='RideCanceller', null=True, blank=True)

