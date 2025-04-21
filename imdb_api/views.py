from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, HttpResponse
from .models import WatchList, StreamPlateform, Review
from .serializers import WatchListSerializer, StreamPlateformSerializer, ReviewSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from django.http import Http404
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework.serializers import ValidationError
from rest_framework.permissions import (IsAuthenticated, 
                                        IsAdminUser, 
                                        IsAuthenticatedOrReadOnly
)
from .permissions import ReviewUserOrReadOnly
from .permissions import AdminOrReadOnly

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'watchlist': reverse('movie-list', request=request, format=format),
        'streamplatform': reverse('stream-plateform', request=request, format=format)
    }) 


class StreamPlateformViewSet(viewsets.ModelViewSet):
    queryset = StreamPlateform.objects.all()
    serializer_class = StreamPlateformSerializer


class ReviewCreate(generics.CreateAPIView):
    permission_classes = [ReviewUserOrReadOnly]
    
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.all()
   
    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        movie = WatchList.objects.get(pk=pk)
        review_user = self.request.user
        review_queryset = Review.objects.filter(review_user=review_user, watchlist=movie)
        if review_queryset:
            raise ValidationError("Can not review multiple time")
        
        if movie.number_rating == 0:
            movie.avg_rating = serializer.validated_data['rating']
        
        else:
            movie.avg_rating = (movie.avg_rating + serializer.validated_data['rating'])/2
        
        movie.number_rating += 1
        movie.save()

        serializer.save(watchlist = movie, review_user=review_user)

class ReviewListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)

class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [ReviewUserOrReadOnly]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

# class StreamPlateformList(generics.ListCreateAPIView):
#     queryset = StreamPlateform.objects.all()
#     serializer_class = StreamPlateformSerializer



# class StreamPlateformDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = StreamPlateform
#     serializer_class = StreamPlateformSerializer







# class StreamPlateformList(mixins.ListModelMixin,
#                           mixins.CreateModelMixin,
#                           generics.GenericAPIView
#                           ):
#     queryset = StreamPlateform.objects.all()
#     serializer_class = StreamPlateformSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self. create(request, *args, **kwargs)


# class StreamPlateformDetail(mixins.RetrieveModelMixin,
#                             mixins.UpdateModelMixin,
#                             mixins.DestroyModelMixin,
#                             generics.GenericAPIView):
    
#     queryset = StreamPlateform.objects.all()
#     serializer_class = StreamPlateformSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
    


# class StreamPlateformList(APIView):
#     def get(self, request, format=None):
#         stream_list = StreamPlateform.objects.all()
#         serialized = StreamPlateformSerializer(stream_list, many=True)
#         return Response(serialized.data)

#     def post(self, request, format=None):
#         data = request.data
#         serialized = StreamPlateformSerializer(data=data)
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data, status=status.HTTP_201_CREATED)
#         return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


# class StreamPlateformDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return StreamPlateform.objects.get(pk=pk)
#         except StreamPlateform.DoesNotExist:
#             raise Http404
        
#     def get(self, request, pk, format=None):
#         stream_plateform = self.get_object(pk=pk)
#         serializer = StreamPlateformSerializer(stream_plateform)
#         return Response(serializer.data)
    
#     def put(self, request, pk, format=None):
#         stream_plateform = self.get_object(pk)
#         data = request.data
#         serializer = StreamPlateformSerializer(stream_plateform, data=data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     def delete(self, request, pk, format=None):
#         stream_plateform = self.get_object(pk=pk)
#         stream_plateform.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)







@api_view(['GET'])
def movie_list(request):

    movie_list = WatchList.objects.all()
    serialized = WatchListSerializer(movie_list, many=True)
    return Response(serialized.data)


@api_view(['GET'])
def movie_detail(request, pk):

    movie = WatchList.objects.get(pk=pk)
    serialized = WatchListSerializer(movie)
    return Response(serialized.data)

# @api_view(['GET', 'POST'])
# def stream_list(request, format=None):
#     if request.method == 'GET':
#         stream_list = StreamPlateform.objects.all()
#         serialized = StreamPlateformSerializer(stream_list, many=True)
#         return Response(serialized.data)
    
#     elif request.method == 'POST':
#         data = request.data
#         serialized = StreamPlateformSerializer(data=data)
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data, status=status.HTTP_201_CREATED)
#         return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def stream_detail(request, pk, format=None):

#     try:
#         stream_plateform = StreamPlateform.objects.get(pk=pk)
#     except StreamPlateform.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = StreamPlateformSerializer(stream_plateform)
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#         data = request.data
#         serializer = StreamPlateformSerializer(stream_plateform, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         stream_plateform.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



