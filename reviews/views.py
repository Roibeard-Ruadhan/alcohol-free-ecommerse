from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse)
from django.shortcuts import render
from django.views.generic import UpdateView, DeleteView
from .models import Reviews
from django.contrib import messages
from .form import ReviewForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from products.models import Product, Category


# Create your views here.
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

@login_required
def submit_review(request, product_id):
    """ View to review a product """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)

        if review_form.is_valid():
            already_reviewed = Reviews.objects.filter(product=product,
                                                           user=request.user)
            if not already_reviewed:
                Reviews.objects.create(
                        product=product,
                        user=request.user,
                        subject=request.POST['subject'],
                        rating=request.POST['rating'],
                        review=request.POST['review'],
                )
                reviews = Reviews.objects.filter(product=product)
                rating_average = find_rating_average(reviews)
                Product.objects.filter(id=product.id).update(
                    rating=rating_average)
                messages.success(
                    request, 'Your review has been successfully added!')
            else:
                messages.error(request, 'You have already reviewed '
                                        'this product!')
            return redirect(reverse('product_detail', args=[product.id]))

        messages.error(request, 'Your review has not been submitted')
    messages.error(request, 'Invalid Method.')
    return redirect(reverse('product_detail', args=[product.id]))


def find_rating_average(reviews):
    """
    Function to get the average rating of product
    from the reviews
    """
    total_reviews = 0
    ratings_total = 0
    rating_average = 0
    for review in reviews:
        total_reviews = total_reviews + 1
        ratings_total = ratings_total + review.rating

    if total_reviews > 0:
        average_rating = (ratings_total / total_reviews)
        rating_average = round(average_rating, 1)
        return rating_average
    else:
        return rating_average


# Redirect to previous page from askdevz.com 
class RedirectToPreviousMixin:
    """
    A view to Redirect back to page
    """
    default_redirect = '/'

    def get(self, request, *args, **kwargs):
        request.session['previous_page'] = request.META.get(
            'HTTP_REFERER', self.default_redirect)
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return self.request.session['previous_page']


class UpdateReview(RedirectToPreviousMixin, LoginRequiredMixin,
                       SuccessMessageMixin, UpdateView):
    """
    A view to edit a Review
    """
    model = Reviews
    form_class = ReviewForm
    template_name = "products/update_review.html"
    success_message = "Your review has been updated"


class DeleteReview(LoginRequiredMixin, DeleteView):
    '''
    View displays the option to delete the review to the user.
    '''
    model = Reviews
    template_name = 'products/delete_review.html'
    success_url = reverse_lazy('products')

    def delete(self, request, *args, **kwargs):
        """ delete product message """
        response = super().delete(request, *args, **kwargs)
        messages.success(
            self.request, 'Your Review has been deleted sucessfully!')
        return response
