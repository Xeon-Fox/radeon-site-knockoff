from django.views.generic import CreateView, ListView, DetailView
from gpu.models import Gpu
from gpu.forms import CreateUpdateGpuForm
from django.shortcuts import redirect

class CreateGpuView(CreateView):
    model = Gpu
    form_class = CreateUpdateGpuForm
    success_url = ""