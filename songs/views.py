from itertools import product
from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SongSerializer

@api_view(['GET', 'POST'])
def song_list(request):
    if request.method == 'GET':
        songs = songs.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SongSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def song_detail(request, pk):
    songs = get_object_or_404(songs, pk=pk)
    if request.method == 'GET':
        serializer = SongSerializer(songs)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SongSerializer(songs, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        songs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# Create your views here.
