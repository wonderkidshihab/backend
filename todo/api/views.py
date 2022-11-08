from urllib import response
from rest_framework import generics, permissions, status, views
from todomanager.models import TodoItem

from .serializers import TodoSerializer


# Create your views here.
class TodoView(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    queryset = TodoItem.objects.all()
    
class TodoModelView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    queryset = TodoItem.objects.all()
    
