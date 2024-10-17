from django.urls import path
from .views import HomePageView


app_name = 'rdna'

urlpatterns = [
    path('', HomePageView.as_view(), name='rdna'),
]
