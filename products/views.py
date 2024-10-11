# доделать как его хтмл будет1!!!

from django.shortcuts import render
from django.views.generic import ListView
from gpu.models import Gpu
# from cart.models import Order
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q


class HomePageView(ListView):
    model = Gpu
    template_name = "main.html"
#     context_object_name = "gpu"
#     paginate_by = 10 

#     def get_queryset(self):
        # Получаем все видеокарты, сортируем по названию
        # return Gpu.objects.all().order_by("title")

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
        # Если пользователь авторизован, добавляем заказы
        # if self.request.user.is_authenticated:
        #     context["cart"] = Order.objects.filter(user=self.request.user)
        # return context

# class SearchResultsView(ListView):
    # model = Gpu
    # template_name = "mainpage/search_results.html"
    # context_object_name = "gpu"

    # def get_queryset(self):
    #     query = self.request.GET.get("query")
    #     return Gpu.objects.filter(
    #         Q(title__icontains=query) | Q(artist__icontains=query)
    #     )
