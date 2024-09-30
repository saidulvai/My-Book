
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .import views
router = DefaultRouter()

router.register('',views.AccountViewset)

urlpatterns = [
    path('list/', include(router.urls)),
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('login/', views.UserLoginApiView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('userprofile/', views.UserProfileAPIView.as_view(), name='userprofile'),
    path('active/<uid64>/<token>/', views.activate, name='active'),
]
