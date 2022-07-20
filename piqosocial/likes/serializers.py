from turtle import up
from .models import Like
from rest_framework import serializers


class LikesSerializer(serializers.Serializer):
    up_vote_by = serializers.ReadOnlyField(source = 'up_vote_by.username')
    down_vote_by = serializers.ReadOnlyField(source = 'down_vote_by.username')

    class Meta:
        model = Like
        fields = ('id', 'article', 'up_vote_by', 'down_vote_by')