from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .import views

routers = DefaultRouter()
routers.register('', views.FavoritesViewSet)
urlpatterns = [
    path('', include(routers.urls)),
]
