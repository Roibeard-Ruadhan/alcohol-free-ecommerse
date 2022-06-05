from django.shortcuts import (
    render, redirect, reverse, get_object_or_404)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import BlogPost, BlogComment
from .forms import BlogCommentForm, BlogForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView


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

    
# All blog posts view
def all_blog_posts(request):
    """
    A view to show the blog page
    """

    blog_posts = BlogPost.objects.all()

    template = 'blog/blog.html'

    context = {
        'blog_posts': blog_posts,
    }

    return render(request, template, context)


# Blog detail view
def blog_detail(request, blog_post_id):
    """
    A view to show individual blog post, comments
    and to allow logged in users to leave a comment.
    """
    blog_post = get_object_or_404(BlogPost, pk=blog_post_id)
    comments = blog_post.comments.all()
    subject = None
    new_comment = None

    if request.method == 'POST':
        comment_form = BlogCommentForm(request.POST)
        if comment_form.is_valid() and request.user.is_authenticated:
            new_comment = comment_form.save(commit=False)
            new_comment.blog_post = blog_post
            new_comment.user = request.user
            new_comment.save()
            messages.success(request, 'Comment added successfully!')
            return redirect(reverse('blog_detail', args=[blog_post.id]))
        else:
            messages.error(request, 'Please check the form for errors. \
                Comment failed to post.')
    else:
        comment_form = BlogCommentForm()

    template = 'blog/blog_detail.html'

    context = {
        'blog_post': blog_post,
        'subject': subject,
        'comments': comments,
        'comment_form': comment_form,
        'new_comment': new_comment,
    }

    return render(request, template, context)


# Blog Admin:
# Add blog
@login_required
def add_blog_post(request):
    """
    Allow an admin user to add a blog post
    """
    if request.user.is_superuser:

        if request.method == 'POST':
            form = BlogForm(request.POST, request.FILES)
            if form.is_valid():
                blog_post = form.save(commit=False)
                blog_post.user = request.user
                blog_post.save()
                messages.info(request, 'Blog added successfully!')
                return redirect(reverse('blog_detail', args=[blog_post.id]))
            else:
                messages.error(request, 'Please check the form for errors. \
                    Blog failed to add.')
        else:
            form = BlogForm()
    else:
        messages.error(request, 'Sorry, you do not have permission for that.')
        return redirect(reverse('home'))

    template = 'blog/add_blog.html'

    context = {
        'form': form,
    }

    return render(request, template, context)


# Edit Blog Post
@login_required
def edit_blog(request, blog_post_id):
    """
    Allow an admin user to edit a product to the store
    """
    if request.user.is_superuser:

        blog_post = get_object_or_404(BlogPost, pk=blog_post_id)

        if request.method == 'POST':
            form = BlogForm(request.POST, request.FILES, instance=blog_post)
            if form.is_valid():
                form.save()
                messages.info(request, 'Blog post updated successfully!')
                return redirect(reverse('blog_detail', args=[blog_post.id]))
            else:
                messages.error(request, 'Please check the form for errors. \
                    Blog post failed to update.')
        else:
            form = BlogForm(instance=blog_post)
            messages.info(request, f'Editing {blog_post.title}')
    else:
        messages.error(request, 'Sorry, you do not have permission for that.')
        return redirect(reverse('home'))

    template = 'blog/edit_blog.html'

    context = {
        'form': form,
        'blog_post': blog_post,
    }

    return render(request, template, context)


# Delete Blog Post
class Delete_Blog_Post(LoginRequiredMixin, DeleteView):
    """
    Allow an admin user to delete a blog post
    """
    model = BlogPost
    template_name = 'blog/delete_blog.html'
    success_url = reverse_lazy('blog')

    def delete(self, request, *args, **kwargs):
        """ delete blogpost message """
        response = super().delete(request, *args, **kwargs)
        messages.success(
            self.request, 'The Mocktail blogpost has been deleted sucessfully!')
        return response


# Class from askdevs.com after going to stackoverflow
class RedirectToPreviousMixin:

    default_redirect = '/'

    def get(self, request, *args, **kwargs):
        request.session['previous_page'] = request.META.get('HTTP_REFERER', self.default_redirect)
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return self.request.session['previous_page']


# Update Comment
class EditCommentView(RedirectToPreviousMixin, LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    A view to edit a comment in Mocktails blog
    """
    model = BlogComment
    form_class = BlogCommentForm
    template_name = "blog/update_comment.html"
    success_message = "Your comment has been updated successfully"



# Delete Comment
class DeleteComment(LoginRequiredMixin, DeleteView):
    '''
    View displays the option to delete the comment to the user.
    '''
    model = BlogComment
    template_name = 'blog/delete_comment.html'
    success_url = reverse_lazy('blog')

    def delete(self, request, *args, **kwargs):
        """ delete blog comment success """
        response = super().delete(request, *args, **kwargs)
        messages.success(
            self.request, 'Your Comment has been deleted sucessfully!')
        return response
