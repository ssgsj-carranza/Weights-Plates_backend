from .views import RegisterAPI
from django.urls import path
from knox import views as knox_views
from .views import LoginAPI
from . import views


urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('user/<int:pk>/', views.UserDetail.as_view())
]