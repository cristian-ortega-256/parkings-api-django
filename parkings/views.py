from rest_framework import status
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.response import Response
from .models import Parkings
from .serializers import ParkingsSerializer

@api_view(['GET', 'POST','PUT'])
def parkings_list(request):
    if request.method == 'GET':
        parkings = Parkings.objects.all()
        serializer = ParkingsSerializer(parkings, many=True)
        return JsonResponse(serializer.data,safe=False)
        
    elif request.method == 'POST' and not 'parkings' in request.data:
        serializer = ParkingsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'POST' and 'parkings' in request.data:
        data = request.data['parkings']
        for parking in data:
            print(parking)
            serializer = ParkingsSerializer(data=parking)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def parking_detail(request, pk):
    try:
        parking = Parkings.objects.get(pk=pk)
    except Parkings.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ParkingsSerializer(parking)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ParkingsSerializer(parking, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        parking.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)