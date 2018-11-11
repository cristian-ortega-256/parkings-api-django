from rest_framework import status
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.response import Response
from ..models.Configuration import Configuration
from ..serializers import ConfigurationSerializer
from ..helpers.formatters import format_data_array, format_element, formatConfigObject


class ConfigurationView():

    @api_view(['GET', 'POST', 'PUT'])
    def configuration_list(request):
        # GET ALL
        if request.method == 'GET':
            configurations = Configuration.objects.all()
            serializer = ConfigurationSerializer(configurations, many=True)
            formattedData = format_data_array(serializer.data)
            return JsonResponse(formattedData, safe=False)
        # POST ONE
        if request.method == 'POST' and not 'configurations' in request.data:
            formattedConfig = formatConfigObject(request.data)
            serializer = ConfigurationSerializer(data=formattedConfig)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # POST MULTIPLE
        if request.method == 'POST' and 'configurations' in request.data:
            # NOTE: This code repeated is REALLY BAD!!!
            # as an future improvement, check how to call external funcions with self as parameter
            for config in request.data['configurations']:
                formattedConfig = formatConfigObject(config)
                serializer = ConfigurationSerializer(data=formattedConfig)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(request.data, status=status.HTTP_201_CREATED)

        # PUT MULTIPLE
        if request.method == 'PUT' and 'configurations' in request.data:
            for config in request.data['configurations']:
                try:
                    configElement = Configuration.objects.get(
                        pk=list(config.keys())[0])
                except Configuration.DoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND)

                formattedConfig = formatConfigObject(config)
                serializer = ConfigurationSerializer(
                    configElement, data=formattedConfig)
                if serializer.is_valid():
                    serializer.save()
                    formattedResponse = format_element(serializer.data)
            return Response(request.data, status=status.HTTP_201_CREATED)

    @api_view(['GET', 'PUT'])
    def configuration_detail(request, pk):
        try:
            configElement = Configuration.objects.get(pk=pk)
        except Configuration.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # GET ONE
        if request.method == 'GET':
            serializer = ConfigurationSerializer(configElement)
            formattedData = format_element(serializer.data)
            return Response(formattedData)

        # PUT ONE
        elif request.method == 'PUT':
            formattedConfig = formatConfigObject(request.data)
            serializer = ConfigurationSerializer(
                configElement, data=formattedConfig)
            if serializer.is_valid():
                serializer.save()
                formattedResponse = format_element(serializer.data)
                return Response(formattedResponse)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
