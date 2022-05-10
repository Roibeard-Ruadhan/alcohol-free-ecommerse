from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KboCfIfJHnB5fGvVe2de5gjVOkDbPYwLUxs2Sl7nj1WkBt4VMg5MGsTKoWzj7njV0Ds33eUUwLgN7Umb8g5azbs00KtEZ9UYh',
        
    }

    return render(request, template, context)