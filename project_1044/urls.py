"""
URL configuration for project_1044 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from apps.views import ProductListView, ProductDetailView, ProfileView, SettingsView, RegisterView, LoginView, \
    LogoutView, WishlistCreateView, WishlistListView
from project_1044 import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('like/<int:pk>/', WishlistCreateView.as_view(), name='like'),
    path('wishlist/', WishlistListView.as_view(), name='wishlist'),


    path('profile/', ProfileView.as_view(), name='profile'),
    path('settings/', SettingsView.as_view(), name='settings'),


    path('signup/', RegisterView.as_view(), name='signup'),
    path('signin/', LoginView.as_view(), name='signin'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


