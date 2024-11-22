from django.views.generic import CreateView, ListView, DetailView
from gpu.models import Gpu
from gpu.forms import CreateUpdateGpuForm
from django.shortcuts import redirect

from .serializers import GpuSerializer
from rest_framework import generics



class CreateGpuView(CreateView):
    model = Gpu
    form_class = CreateUpdateGpuForm
    success_url = ""


from .serializers import GpuSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class GpuListAPIView(APIView):
    def get(self, request):
        articles = Gpu.objects.all()
        serializer = GpuSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GpuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GpuDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gpu.objects.all()
    serializer_class = GpuSerializer