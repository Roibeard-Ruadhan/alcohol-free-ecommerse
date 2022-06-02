from django.shortcuts import render



def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def error_404(request, exception):
    '''
    A 404 error handling view
    '''
    return render(request, '404.html', status=404)

def error_500(request, *args, **argv):
    '''
    A 500 error handling view
    '''
    return render(request, '500.html', status=500)
