from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .import views

routers = DefaultRouter()
routers.register('load_blogs', views.BlogsViewsets, basename='load_blogs')
routers.register('categories', views.CategoryViewset, basename='categories')
routers.register('rating/',views.RatingApiView, basename='rating')
urlpatterns = [
    path('', include(routers.urls)),
    # path('load_blogs/', views.BlogsViewsets.as_view(), name='load_blogs'),
    # path('categories/', views.CategoryViewset.as_view(), name='categories'),
    # path('rating/', views.RatingApiView.as_view(), name='rating'),
]
