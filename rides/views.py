from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.utils import timezone
from datetime import timedelta

from .models import Rides, RideCancellations

class IndexView(generic.ListView):
    template_name = 'rides/index.html'
    context_object_name = 'rides'

    def get_queryset(self):
        return Rides.objects.filter(ride_date__gte=timezone.now()).order_by('ride_date')


class CancelRideDetail(generic.DetailView):
    template_name = 'rides/cancel.html'
    model = Rides

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CancelRideDetail, self).dispatch(*args, **kwargs)

def faq(request):
    return render(request, 'rides/faq.html')

@login_required()
def cancel_ride(request, pk):
    r = get_object_or_404(Rides, pk=pk)

    try:
        selected_reason = RideCancellations.objects.get(pk=request.POST['cancel_reason'])

    except (KeyError, RideCancellations.DoesNotExist):
        selected_reason = None

    r.ride_cancel_reason = selected_reason
    r.ride_cancelled_by = request.user
    r.ride_cancelled = timezone.now()
    r.save()
    return HttpResponseRedirect(reverse('rides:index'))

@login_required()
def uncancel_ride(request, pk):
    r = get_object_or_404(Rides, pk=pk)

    r.ride_cancel_reason = None
    r.ride_cancelled_by = None
    r.ride_cancelled = None
    r.save()

    return HttpResponseRedirect(reverse('rides:index'))


# We only want a response here if the following is true:
#
def next_ride(request):

    # TODO we potentially need to cater for multiple rides (e.g. track and tuesday ride)
    query_start = timezone.now() - timedelta(hours=3)
    query_end = timezone.now() + timedelta(days=1)

    r = Rides.objects.filter(ride_date__gte=query_start
                             ).filter(ride_date__lte=query_end).order_by('ride_date')[:2]

    if r[0].ride_cancelled is None:
        message_start = r[0].ride_date - timedelta(hours=12)
        message_end = r[0].ride_date + timedelta(hours=3)

        context = {'rides': r,
                   'start': message_start,
                   'end': message_end
                   }
        # return render(request, 'rides/nextride.html', context)

        if message_start < timezone.now() < message_end:
            # context = {'nextride': r}
            return render(request, 'rides/nextride.html', context)

    context = {'rides': r}
    return render(request, 'rides/nextride.html', context)


