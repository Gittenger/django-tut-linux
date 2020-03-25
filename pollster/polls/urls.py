"""Define url routes for polls app"""
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # first empty means /polls
    path('', views.index, name='index')
]
