from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse
from django.views import generic

from datetime import datetime


from .models import Rides, RideCancellations

class IndexView(generic.ListView):
    template_name = 'rides/index.html'
    context_object_name = 'rides'

    def get_queryset(self):
        return Rides.objects.order_by('ride_date')



class CancelRideDetail(generic.DetailView):
    template_name = 'rides/status.json'
    model = Rides


class RideDetail(generic.DetailView):
    template_name = 'rides/cancel.html'
    model = Rides

def cancel_ride(request, pk):
    r = get_object_or_404(Rides, pk=pk)

    try:
        selected_reason = RideCancellations.objects.get(pk=request.POST['cancel_reason'])

    except (KeyError, RideCancellations.DoesNotExist):
        selected_reason = None

    r.ride_cancel_reason = selected_reason
    r.ride_cancelled_by = None
    r.ride_cancelled = datetime.now()
    r.save()
    return HttpResponseRedirect(reverse('rides:index'))

def uncancel_ride(request, pk):
    r = get_object_or_404(Rides, pk=pk)

    r.ride_cancel_reason = None
    r.ride_cancelled_by = None
    r.ride_cancelled = None
    r.save()

    return HttpResponseRedirect(reverse('rides:index'))