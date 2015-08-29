from django.contrib import admin

# Register your models here.
from .models import Rides, RideCancellations, RideLeader

class RidesAdmin(admin.ModelAdmin):
    fields = ['ride_leader_a',
              'ride_date',
              'ride_destination',
              'ride_description',
              ]
    list_display = ('ride_date', 'ride_destination', 'ride_leader_a')

admin.site.register(Rides, RidesAdmin)
admin.site.register(RideCancellations)
admin.site.register(RideLeader)

