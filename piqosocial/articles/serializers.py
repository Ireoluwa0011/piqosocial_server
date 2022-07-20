from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    comment = serializers.PrimaryKeyRelatedField(many = True, read_only = True)

    class Meta:
        fields = ('id', 'title', 'body', 'created_at', 'author')
        model = Article