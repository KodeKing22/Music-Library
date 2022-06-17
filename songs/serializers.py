from dataclasses import field
from rest_framework import serializers
from .models import Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        field = ['id', 'title', 'artist', 'album', 'genre', 'release_date']