"""boutique_ado URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler403, handler404, handler500 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('bag/', include('bag.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
    path('blog/', include('blog.urls')),
    path('contact/', include('contact.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler403 = 'bag.views.error_403'
handler404 = 'bag.views.error_404'
handler500 = 'bag.views.error_500'
handler403 = 'checkout.views.error_403'
handler404 = 'checkout.views.error_404'
handler500 = 'checkout.views.error_500'
handler403 = 'contact.views.error_403'
handler404 = 'contact.views.error_404'
handler500 = 'contact.views.error_500'
handler403 = 'home.views.error_403'
handler404 = 'home.views.error_404'
handler500 = 'home.views.error_500'
handler403 = 'products.views.error_403'
handler404 = 'products.views.error_404'
handler500 = 'products.views.error_500'
handler403 = 'profiles.views.error_403'
handler404 = 'profiles.views.error_404'
handler500 = 'profiles.views.error_500'
# handler403 = 'reviews.views.error_403'
# handler404 = 'reviews.views.error_404'
# handler500 = 'reviews.views.error_500'

