from tracemalloc import get_object_traceback
from turtle import down
from winreg import QueryInfoKey
from django.shortcuts import get_object_or_404,render
from rest_framework import viewsets,status,serializers
from .serializers import LikesSerializer
from articles.models import Article
from .models import Like


# Create your views here.
class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikesSerializer

    def perform_create(self,serializer):
        article_instance = get_object_or_404(Article,pk = self.request.data['article'])

        if self.request.data['up_vote']:
            already_up_voted = Article.filter(article = article_instance, up_vote_by = self.request.user).exists()
            if already_up_voted:
                raise serializers.ValidationError({"message": "Article already up-voted"})
            else:
                serializer.save(up_vote_by = self.request.user, article = article_instance)
        else:
            already_down_voted = Article.objects.filter(article = article_instance,down_vote_by = self.request.user).exists()
            if already_down_voted:
                raise serializer.ValidationError({"message": "Article already down-voted"})
        # return super().perform_create(serializer)


        