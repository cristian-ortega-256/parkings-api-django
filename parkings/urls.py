from django.urls import path
from parkings import views


urlpatterns = [
    path('parkings/', views.parkings_list),
    path('parkings/<int:pk>/', views.parking_detail),
]