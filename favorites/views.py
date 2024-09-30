from django.shortcuts import render
from rest_framework import viewsets
from .models import Favorites
from .serializers import FavoritesSerializer
from django.core.mail import send_mail
from blogs.models import Blogs
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class FavoritesViewSet(viewsets.ModelViewSet):
    queryset = Favorites.objects.all()
    serializer_class = FavoritesSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        instance = serializer.save(user=self.request.user)

        send_mail(
            'Blog Favorited',
            'You have favorited a blog post.','',
            [self.request.user.email],
        )
