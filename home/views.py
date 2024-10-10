from django.shortcuts import render
from django.views.generic import ListView
from vinyls.models import VinylRecord, Tag
from orders.models import Order
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q


class HomePageView(ListView):
    model = VinylRecord
    template_name = "mainpage/index.html"
    context_object_name = "vinyls"
    paginate_by = 10  # Пагинация: 10 пластинок на странице

    def get_queryset(self):
        # Получаем все виниловые пластинки, сортируем по названию
        return VinylRecord.objects.all().order_by("title")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Топ-10 тегов
        context["top_tags"] = Tag.objects.all()[:10]
        # Если пользователь авторизован, добавляем заказы
        if self.request.user.is_authenticated:
            context["orders"] = Order.objects.filter(user=self.request.user)
        return context


class SearchResultsView(ListView):
    model = VinylRecord
    template_name = "mainpage/search_results.html"
    context_object_name = "vinyls"

    def get_queryset(self):
        query = self.request.GET.get("query")
        return VinylRecord.objects.filter(
            Q(title__icontains=query) | Q(artist__icontains=query)
        )
