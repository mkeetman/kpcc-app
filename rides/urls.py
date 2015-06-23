__author__ = 'michael'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^cancel/(?P<pk>[0-9])/$', views.CancelRideDetail.as_view(), name='cancel')

]
