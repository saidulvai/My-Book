from django.shortcuts import render
from rest_framework import viewsets
from .models import author
from .serializers import AuthorSerializer
from .permissions import IsAuthor
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class AuthorViewsets(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated and IsAuthor]
    queryset = author.objects.all()
    serializer_class = AuthorSerializer

