from django.shortcuts import (
    render, redirect, reverse,
    get_object_or_404, HttpResponse)
from products.models import Product
from django.contrib import messages


def error_403(request, exception):
    '''403 error view'''
    return render(request, '403.html', status=403)


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


def view_bag(request):
    """ A view to return the shopping bag """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of item to bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] = quantity
    else:
        bag[item_id] = quantity
        messages.success(
            request, f'Added "{product.name}" to your bag.')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(
            request, f'Updated {product.name} quantity to {bag[item_id]}.')
    else:
        messages.error(
            request, f'{"You must update to a value greater than 0."}')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove item from bag"""
    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})

        bag.pop(item_id)
        messages.success(
            request, f'Removed {product.name} from your bag.')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
