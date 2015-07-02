__author__ = 'michael'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9])/cancel/$', views.CancelRideDetail.as_view(), name='cancel_detail'),
    url(r'^(?P<pk>[0-9])/cancel/submit/$', views.cancel_ride, name='cancel_ride'),
    url(r'^(?P<pk>[0-9])/cancel/uncancel/$', views.uncancel_ride, name='un-cancel_ride'),
    url(r'^(?P<pk>[0-9])/status/$', views.RideDetail.as_view(), name='status'),
    url(r'^/nextride/status/$', views.RideDetail.as_view(), name='next_ride_status'),
]
