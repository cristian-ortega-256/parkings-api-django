from django.urls import path
from .views import ListparkingsView


urlpatterns = [
    path('parkings/', ListparkingsView.as_view(), name="parkings-all")
]