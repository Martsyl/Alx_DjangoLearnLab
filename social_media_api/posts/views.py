from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    filter_backends = [SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Comment.objects.filter(
            post_id=self.kwargs['post_pk']
        ).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post_id=self.kwargs['post_pk']
        )