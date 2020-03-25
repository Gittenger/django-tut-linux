"""Def views for pages app"""
from django.shortcuts import render


def index(request):
    """Return index view"""
    return render(request, 'pages/index.html')
