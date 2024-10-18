from django import forms
from .models import Order, OrderItem
from django.utils.translation import gettext_lazy as _  

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user']
        labels = {
            'user': _("Пользователь"),
        }

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['gpu', 'quantity']
        labels = {
            'gpu': _("Видеокарта"),
            'quantity': _("Количество"),
        }
