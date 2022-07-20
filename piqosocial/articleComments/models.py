from django.db import models
from django.contrib.auth.models import User
from articles.models import Article

# Create your models here.

# Create your models here.


# Create your models here.
class articleComment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank = False)
    author = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    article = models.ForeignKey(Article, related_name="comments", on_delete=models.CASCADE  )

    class Meta:
        ordering = ['created_at']