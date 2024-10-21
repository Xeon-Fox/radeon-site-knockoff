from django.views.generic import ListView
from gpu.models import Gpu


class HomePageView(ListView):
    model = Gpu
    template_name = "products.html"

