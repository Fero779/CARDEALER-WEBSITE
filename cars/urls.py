from django.urls import path
from . import views

urlpatterns = [
    path('', views.cars, name='cars'),  # List all cars
    path('<int:id>/', views.car_detail, name='car_detail'),  # Car details based on ID
    path('search/', views.search, name='search'),  # Search functionality
    path('create/', views.car_create, name='car_create'),  # Create a new car
    path('<int:car_id>/edit/', views.car_edit, name='car_edit'),  # Edit car details
    path('<int:car_id>/delete/', views.car_delete, name='car_delete'),  # Delete car
]
