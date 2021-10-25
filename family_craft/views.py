"""Imports"""
from django.shortcuts import render


def handle_no_found(request, exception):
    """"""
    return render(request, '404error.html')
