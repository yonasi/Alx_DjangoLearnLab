
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from .views import PostViewSet, CommentViewSet, FeedView
from .views import PostViewSet, CommentViewSet, FeedView, LikeToggleView
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', FeedView.as_view(), name='post-feed'),
    path('posts/<int:pk>/like/', LikeToggleView.as_view(), name='post-like'),
    path('posts/<int:pk>/unlike/', LikeToggleView.as_view(), name='post-unlike'),

]