from django.urls import path
from .views import (
    UserProfileView,
    RegisterView,
    UserLoginView,
    UserLogoutView,
    UserPasswordChangeView,
)

from django.urls import path
from .views import HomeView, ProductsView, RDNAView
app_name = "users"

urlpatterns = [
    path("profile/", UserProfileView.as_view(), name="user_profile"),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("password-change/", UserPasswordChangeView.as_view(), name="password_change"),
    path('', HomeView.as_view(), name='home'),
    path('series/', ProductsView.as_view(), name='products'),
    path('rdna/', RDNAView.as_view(), name='rdna'),
]
