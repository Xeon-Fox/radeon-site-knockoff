

from django.shortcuts import render
from django.views.generic import ListView
from gpu.models import Gpu
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q


class HomePageView(ListView):
    model = Gpu
    template_name = "main.html"

