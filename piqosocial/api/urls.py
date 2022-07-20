from django.urls import path
from rest_framework.routers import SimpleRouter
from articles.views import ArticleViewSet
from articleComments.views import CommentViewSet
from likes.views import LikeViewSet



router = SimpleRouter()
router.register('articles', ArticleViewSet, basename = 'articles')
router.register('comments', CommentViewSet, basename = 'comments')
router.register('likes', LikeViewSet, basename = 'likes')

urlpatterns = router.urls