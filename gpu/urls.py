from django.urls import path
from .views import GpuDetailView, GpuListAPIView
app_name = 'gpu'

urlpatterns = [
    path('gpu/', GpuListAPIView.as_view(), name='gpu-list-create'),
    path('gpu/<int:pk>/', GpuDetailView.as_view(), name='gpu-detail'),
]