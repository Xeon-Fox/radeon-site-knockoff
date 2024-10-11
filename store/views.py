from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import CartItem, Cart
from gpu.models import (
    Gpu,
)  # Импорт Gpu для использования в представлениях
from .forms import AddToCartForm, UpdateCartItemForm

from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class ProductListView(ListView):
    model = Gpu  # Используем модель Gpu
    template_name = "store/product_list.html"
    context_object_name = "products"
    paginate_by = 10


class ProductDetailView(DetailView):
    model = Gpu  # Используем модель Gpu
    template_name = "store/product_detail.html"
    context_object_name = "product"


class CartView(LoginRequiredMixin, DetailView):
    model = Cart
    template_name = "store/cart.html"
    context_object_name = "cart"

    def get_object(self):
        return get_object_or_404(Cart, user=self.request.user)


class AddToCartView(LoginRequiredMixin, CreateView):
    model = CartItem
    form_class = AddToCartForm
    template_name = "store/add_to_cart.html"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        gpu_id = kwargs["data"].get(
            "gpu_id"
        )  # Извлекаем ID товара из URL или других данных
        kwargs["gpu_id"] = gpu_id  # Передаем ID в форму
        return kwargs

    def form_valid(self, form):
        cart, created = Cart.objects.get_or_create(
            user=self.request.user, defaults={"user": self.request.user}
        )
        # cart = get_object_or_404(Cart, user=self.request.user)
        form.instance.cart = cart
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("store:cart")


class UpdateCartItemView(LoginRequiredMixin, UpdateView):
    model = CartItem
    form_class = UpdateCartItemForm
    template_name = "store/update_cart_item.html"

    def get_success_url(self):
        return reverse_lazy("store:cart")
