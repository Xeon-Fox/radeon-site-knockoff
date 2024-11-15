from django.urls import path
from .views import (
    UserProfileView,
    RegisterView,
    UserLoginView,
    UserLogoutView,
    UserPasswordChangeView,
)

from django.urls import path
app_name = "users"

urlpatterns = [
    path("profile/", UserProfileView.as_view(), name="user_profile"),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("password_change/", UserPasswordChangeView.as_view(), name="password_change"),
]
