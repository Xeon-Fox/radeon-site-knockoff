from django.urls import path
from .views import ProductListView, ProductDetailView, CartView, AddToCartView, UpdateCartItemView

app_name = 'store'

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/add/', AddToCartView.as_view(), name='add_to_cart'),
    path('cart/update/<int:pk>/', UpdateCartItemView.as_view(), name='update_cart_item'),
]
