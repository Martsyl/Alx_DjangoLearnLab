from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PostViewSet, CommentViewSet
from .views import FeedView
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')

comment_list = CommentViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

comment_detail = CommentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns = [
    path('', include(router.urls)),

    path(
        'posts/<int:post_pk>/comments/',
        comment_list,
        name='comment-list'
    ),
    path(
        'posts/<int:post_pk>/comments/<int:pk>/',
        comment_detail,
        name='comment-detail'
    ),
     path('feed/', FeedView.as_view(), name='feed'),
]