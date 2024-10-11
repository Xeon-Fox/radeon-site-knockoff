from django.db import models
from django.utils.translation import gettext_lazy as _
from gpu.models import Gpu
from django.contrib.auth import get_user_model


User = get_user_model()

class Cart(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name=_("Пользователь"),
        related_name="cart"
    )

    class Meta:
        verbose_name = _("Корзина")
        verbose_name_plural = _("Корзины")

    def __str__(self):
        return f"Корзина пользователя {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name="items",
        verbose_name=_("Корзина")
    )
    gpu = models.ForeignKey(
        Gpu,
        on_delete=models.CASCADE,
        related_name="cart_items",
        verbose_name=_("Видеокарта")
    )
    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name=_("Количество"),
        help_text=_("Укажите количество видеокарт.")
    )

    class Meta:
        verbose_name = _("Элемент корзины")
        verbose_name_plural = _("Элементы корзины")

    def __str__(self):
        return f"{self.gpu.title} (x{self.quantity})"
