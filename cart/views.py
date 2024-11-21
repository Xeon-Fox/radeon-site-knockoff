from django.views.generic import ListView, DetailView, CreateView
from .models import Order, OrderItem
from .forms import OrderForm, OrderItemForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'order_list.html'
    context_object_name = 'orders'  

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('-created_at')

class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'order_detail.html'  
    context_object_name = 'order'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

class CreateOrderView(LoginRequiredMixin, CreateView):
    model = Order
    form_class = OrderForm
    
    template_name = 'order_form.html'
    success_url = reverse_lazy('cart:order_list')

    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)
csrf_exempted_view = csrf_exempt(CreateOrderView.as_view())
class GpuDataView(View):
    def post(self, request):
        cart_data = json.loads(request.body)

        #и тут типо сохраняется

        return JsonResponse({'message': 'Data received successfully!'})

