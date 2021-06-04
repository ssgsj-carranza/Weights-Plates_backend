from django.urls import path
from . import views

urlpatterns = [
    path('nutrients/', views.NutrientsList.as_view()),
    path('nutrients/<int:pk>/', views.NutrientsDetail.as_view())
 ]