from pkg_resources import register_finder
from rest_framework import serializers
from .models import articleComment

class CommentSerializer(serializers.ModelSerializer):
    # author = serializers.ReadOnlyField()

    class Meta:
        model = articleComment
        fields = ['id','body', 'author', 'article']