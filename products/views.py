from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse)
from django.contrib import messages
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from reviews.views import submit_review, find_rating_average, UpdateReview, DeleteReview
from reviews.form import ReviewForm
from reviews.models import Reviews
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import ProductForm


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

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    review_form = ReviewForm(data=request.POST or None)
    reviews = Reviews.objects.filter(
        product=product).order_by('-created_on')
    total_reviews = reviews.count()
    rating_average = find_rating_average(reviews)
    Product.objects.filter(id=product.id).update(
        rating=rating_average)

    context = {
        'product': product,
        'review_form': review_form,
        'reviews': reviews,
        'total_reviews': total_reviews,
        'rating_average': rating_average
    }

    return render(request, 'products/product_detail.html', context)



@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


# Delete Product by the superuser
class Delete_Product(LoginRequiredMixin, DeleteView):
    '''
    View displays the option to delete the product to the user.
    '''
    model = Product
    template_name = 'products/delete_product.html'
    success_url = reverse_lazy('products')

    def delete(self, request, *args, **kwargs):
        """ delete product message """
        response = super().delete(request, *args, **kwargs)
        messages.success(
            self.request, 'The Product has been deleted successfully!')
        return response
