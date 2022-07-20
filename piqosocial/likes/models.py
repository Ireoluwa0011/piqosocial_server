from turtle import down
from django.db import models
from articles.models import Article
from django.contrib.auth.models import User


# Create your models here.

class Like(models.Model):
    article = models.ForeignKey(Article, related_name = 'likes', on_delete = models.CASCADE)
    up_vote_by = models.ForeignKey(User, related_name = 'up_vote_user', on_delete = models.CASCADE)
    down_vote_by = models.ForeignKey(User, related_name = 'down_vote_user', on_delete = models.CASCADE)


    def __str__(self):
        return self