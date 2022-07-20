from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CommentSerializer
from .models import articleComment
# Create your views here.

class CommentViewSet(viewsets.ModelViewSet):
    queryset = articleComment.objects.all()
    serializer_class = CommentSerializer