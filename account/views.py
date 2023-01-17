from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Author
from .serializers import AuthorSerializer


class AuthorRegisterAPIView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
