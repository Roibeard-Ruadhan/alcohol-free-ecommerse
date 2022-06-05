from django.contrib import admin
from .models import BlogPost, BlogComment
from reviews.models import Reviews


class BlogPostAdmin(admin.ModelAdmin):
    """
    Setup Blog Post section of Admin Panel
    """

    list_display = (
        'title',
        'created_on',
        'image',
    )

    search_fields = (
        'title',
        'body_text',
    )


class BlogCommentAdmin(admin.ModelAdmin):
    """
    Setup Blog Comment section of Admin Panel
    """
    list_display = (
        'user',
        'blog_post',
        'subject',
        'comment',
        'created_on',
    )

    search_fields = (
        'user',
        'subject',
        'comment',
    )

    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(published=True)


class ReviewsAdmin(admin.ModelAdmin):
    """
    Setup Reviews section of Admin Panel
    """
    list_display = (
        'user',
        'subject',
        'review',
        'created_on',
    )

    search_fields = (
        'user',
        'subject',
        'review',
    )

    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(published=True)




admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BlogComment, BlogCommentAdmin)
admin.site.register(Reviews, ReviewsAdmin)