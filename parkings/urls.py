from django.urls import path
from .views.Parkings import ParkingsView
from .views.Configuration import ConfigurationView

urlpatterns = [
    path('parkings/', ParkingsView.parkings_list),
    path('parkings/<int:pk>/', ParkingsView.parking_detail),
    path('configuration/', ConfigurationView.configuration_list),
    path('configuration/<str:pk>/', ConfigurationView.configuration_detail)
]