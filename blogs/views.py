from django.shortcuts import render
from rest_framework import viewsets, filters, status
from .models import Blogs, categories, Rating
from author.models import author
from .serializers import BlogsSerializer,CategorySerializer, RatingSerializer
from .permissions import IsAuthor, IsAdmin
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# Create your views here.
class CategoryViewset(viewsets.ModelViewSet):
    queryset = categories.objects.all()
    serializer_class = CategorySerializer

class BlogForSpecificCategory(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        categories_id = request.query_params.get("categories_id")
        if categories_id:
            return queryset.filter(categories_id=categories_id)
        return queryset

class BlogsViewsets(viewsets.ModelViewSet):
    queryset = Blogs.objects.all()
    serializer_class = BlogsSerializer

    filter_backends = [BlogForSpecificCategory]
    
    def perform_create(self, serializer):
        users = self.request.user
        print("User are: ",users.username)
        serializer.save(author=self.request.user)
        


class RatingApiView(viewsets.ModelViewSet):
    
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data) 
        if serializer.is_valid(): 
            rating = serializer.save()
            return Response({"message": "Rating submitted successfully"})
        return Response(serializer.errors, status=400)