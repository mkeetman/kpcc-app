from django.contrib import admin

# Register your models here.
from .models import Rides, RideCancellations, RideLeader

class RidesAdmin(admin.ModelAdmin):
    fields = ['ride_leader_a',
              'ride_leader_b',
              'ride_date',
              'ride_destination',
              'ride_map',
              'ride_parcours',
              'ride_speed',
              'ride_description',
              'ride_expected_duration',
              'ride_expected_length']
    list_display = ('ride_date', 'ride_destination', 'ride_leader_a','ride_leader_b')

admin.site.register(Rides, RidesAdmin)
admin.site.register(RideCancellations)
admin.site.register(RideLeader)

