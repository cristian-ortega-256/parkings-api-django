from rest_framework import status
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.response import Response
from ..models.Configuration import Configuration
from ..serializers import ConfigurationSerializer

class ConfigurationView():

    @api_view(['GET'])
    def configuration_list(request):
        if request.method == 'GET':
            configurations = Configuration.objects.all()
            serializer = ConfigurationSerializer(configurations, many=True)
            return JsonResponse(serializer.data,safe=False)

    @api_view(['GET','PUT'])
    def configuration_detail(request,pk):
        try:
            configElement = Configuration.objects.get(pk=pk)
        except Configuration.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        if request.method == 'GET':
            serializer = ConfigurationSerializer(configElement)
            return Response(serializer.data)
        
        elif request.method == 'PUT':
            serializer = ConfigurationSerializer(configElement, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
