from django.urls import path
from .views import HomePageView


app_name = 'series'

urlpatterns = [
    path('', HomePageView.as_view(), name='series'),
]
