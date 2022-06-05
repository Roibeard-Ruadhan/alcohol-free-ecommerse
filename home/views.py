from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse)
from django.shortcuts import render



def handler_403(request, exception):
    '''403 error view'''
    return render(request, '403.html', status=403)


def handler_404(request, exception):
    '''
    A 404 error handling view
    '''
    return render(request, '404.html', status=404)


def handler_500(request, *args, **argv):
    '''
    A 500 error handling view
    '''
    return render(request, '500.html', status=500)


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')
