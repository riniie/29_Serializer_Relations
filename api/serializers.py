from rest_framework import serializers
from .models import Song, Singer


class SingerSerializer(serializers.ModelSerializer):
    # songs = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # songs = serializers.StringRelatedField(many=True, read_only=True)
    # songs = serializers.SlugRelatedField(many=True, read_only=True, slug_field='duration')
    # songs = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='song-detail')
    songs = serializers.HyperlinkedIdentityField(view_name='song-detail')

    class Meta:
        model = Singer
        fields = ['id', 'name', 'gender', 'songs']


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'duration', 'singer']
