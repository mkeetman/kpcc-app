from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Rides

class IndexView(generic.ListView):
    template_name = 'rides/index.html'
    context_object_name = 'rides'

    def get_queryset(self):
        return Rides.objects.order_by('ride_date')



class CancelRideDetail(generic.DetailView):
    template_name = 'rides/cancel.html'
    model = Rides
