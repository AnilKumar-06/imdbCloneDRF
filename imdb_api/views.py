from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, HttpResponse
from .models import WatchList, StreamPlateform
from .serializers import WatchListSerializer, StreamPlateformSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.


def movie_list(request):

    movie_list = WatchList.objects.all()
    serialized = WatchListSerializer(movie_list, many=True)
    return JsonResponse(serialized.data, safe=False)

def movie_detail(request, pk):

    movie = WatchList.objects.get(pk=pk)
    serialized = WatchListSerializer(movie)
    return JsonResponse(serialized.data)

@api_view(['GET', 'POST'])
def stream_list(request, format=None):
    if request.method == 'GET':
        stream_list = StreamPlateform.objects.all()
        serialized = StreamPlateformSerializer(stream_list, many=True)
        return Response(serialized.data)
    
    elif request.method == 'POST':
        data = request.data
        serialized = StreamPlateformSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def stream_detail(request, pk, format=None):

    try:
        stream_plateform = StreamPlateform.objects.get(pk=pk)
    except StreamPlateform.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StreamPlateformSerializer(stream_plateform)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        data = request.data
        serializer = StreamPlateformSerializer(stream_plateform, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        stream_plateform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



