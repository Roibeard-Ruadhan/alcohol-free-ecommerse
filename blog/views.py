from django.shortcuts import render

# Create your views here.

def blog(request):
    """ A view to render the blogs page """
    return render(request, 'blog/blog.html')