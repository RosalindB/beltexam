from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.submit_register),
    url(r'^signin$', views.submit_signin),
    url(r'^bright_ideas$', views.logon),
    url(r'^logout$', views.logout),
    url(r'^submit_ideas$', views.submit_ideas),
    url(r'^user/(?P<id>[0-9]+)$', views.uprof),
    url(r'^createLike', views.createLike),
]