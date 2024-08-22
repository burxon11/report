from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    TemplateView, ListView,
    DetailView, CreateView, FormView, UpdateView
)

from apps.forms import UserRegisterForm, UserLoginForm, UserUpdateForm
from apps.mixins import NotLoginRequiredMixin
from apps.models import Product, User, WishList


# Create your views here.


class ProductListView(ListView):
    template_name = 'product/products.html'
    model = Product
    context_object_name = 'products'
    # ordering = ['-created_at']

    def get_queryset(self):
        qs = super().get_queryset()
        data = self.request.GET.get('search')
        if data is not None and len(data) > 0:
            qs = qs.filter(name__icontains=data)
        return qs


class ProductDetailView(DetailView):
    template_name = 'product/product-details.html'
    model = Product


class SettingsView(UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'user/settings.html'
    success_url = reverse_lazy('profile')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        user = self.request.user
        data['user'] = user
        return data

    def get_object(self, queryset=None):
        user = self.request.user
        return user


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'user/profile.html'
    login_url = reverse_lazy('signin')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        user = self.request.user
        data['user'] = user
        return data


class RegisterView(NotLoginRequiredMixin, CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'auth/register.html'
    success_url = '/'


class LoginView(FormView):
    form_class = UserLoginForm
    template_name = 'auth/login.html'
    success_url = '/'

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = User.objects.filter(username=username).first()
        if user is not None and user.check_password(password):
            login(self.request, user)
            return redirect('/')
        # print(username, password)
        return super().form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(self.request)
        return redirect('/')


class WishlistCreateView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        user = self.request.user
        pk = self.kwargs.get('pk')
        product = Product.objects.filter(pk=pk).first()
        if user and pk:
            if not WishList.objects.filter(product=product).exists():
                WishList.objects.create(
                    user=user,
                    product=product
                )
            else:
                wishlist = WishList.objects.filter(product=product).first()
                wishlist.delete()
        return redirect('/')


class WishlistListView(ListView):
    model = WishList
    template_name = 'product/shopping-cart.html'
    context_object_name = 'wishlist'







