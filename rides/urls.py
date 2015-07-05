__author__ = 'michael'

from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9])/cancel/$', views.CancelRideDetail.as_view(), name='cancel_detail'),
    url(r'^(?P<pk>[0-9])/cancel/submit/$', views.cancel_ride, name='cancel_ride'),
    url(r'^(?P<pk>[0-9])/cancel/uncancel/$', views.uncancel_ride, name='un-cancel_ride'),
    url(r'^nextride/status/$', views.next_ride, name='next_ride_status'),
    #url(r'^login/$', auth_views.login),
    #url(r'^(?P<pk>[0-9])/status/$', views.RideDetail.as_view(), name='status'),

]
