from django import forms
from django.utils.translation import gettext_lazy as _
from .models import CartItem
from gpu.models import Gpu  # Импорт модели Gpu


class AddToCartForm(forms.ModelForm):
    gpu = forms.ModelChoiceField(
        queryset=Gpu.objects.none(),  # Изначально устанавливаем пустой queryset
        label=_("Видеокарта"),
        help_text=_("Выберите видеокарту для добавления в корзину."),
    )
    gpu_id = forms.IntegerField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        gpu_id = kwargs.pop('gpu_id', None)  # Извлекаем переданный ID пластинки
        super().__init__(*args, **kwargs)

        if gpu_id:
            self.fields['gpu_id'].initial = gpu_id
            gpu = Gpu.objects.get(id=gpu_id)
            # Устанавливаем queryset, фильтруя по переданному ID
            self.fields['gpu'].queryset = Gpu.objects.filter(pk=gpu_id)
            self.fields['gpu'].initial = gpu
            self.fields['gpu'].empty_label = None

    class Meta:
        model = CartItem
        fields = ["gpu", "quantity"]
        labels = {
            "quantity": _("Количество"),
        }



class UpdateCartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ["quantity"]
        labels = {
            "quantity": _("Количество"),
        }
