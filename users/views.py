from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, FormView
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import TemplateView



from .forms import UserLoginForm, UserRegistrationForm
# from orders.models import Order

# откоментировать после рабочего вида cart
class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = "register/profile.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["orders"] = Order.objects.filter(user=self.request.user)
#         return context

class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = "users/profile.html"  # Убедитесь, что путь к шаблону правильный

class RegisterView(FormView):
    template_name = "users/register.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("users:user_profile")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data["password"])
        user.save()
        login(self.request, user)
        return super().form_valid(form)

class UserLoginView(LoginView):
    template_name = "users/login.html"
    authentication_form = UserLoginForm

    def get_success_url(self):
        return reverse_lazy("users:user_profile")

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('users:login')
    template_name = 'users/logged_out.html'

class UserPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = "users/password_change.html"
    success_url = reverse_lazy("users:user_profile")



# Главная страница
class HomeView(TemplateView):
    template_name = 'home.html'

# Страница с продуктами
class ProductsView(TemplateView):
    template_name = 'products.html'

# Страница RDNA
class RDNAView(TemplateView):
    template_name = 'rdna.html'

# Страница корзины
class CartView(TemplateView):
    template_name = 'cart.html'




