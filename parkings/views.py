from rest_framework import generics
from .models import Parkings
from .serializers import ParkingsSerializer


class ListparkingsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Parkings.objects.all()
    serializer_class = ParkingsSerializer