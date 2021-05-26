from django.urls import path
from . import views

urlpatterns = [
    path('supplements/', views.SupplementList.as_view()),
    path('supplements/<int:pk>/', views.SupplementDetail.as_view())
 ]