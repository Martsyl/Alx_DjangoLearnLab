from rest_framework import serializers
from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            'id',
            'author',
            'title',
            'content',
            'created_at',
            'updated_at',
            'comments_count'
        )

    def get_comments_count(self, obj):
        return obj.comments.count()


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    post = serializers.ReadOnlyField(source='post.id')

    class Meta:
        model = Comment
        fields = (
            'id',
            'post',
            'author',
            'content',
            'created_at',
            'updated_at'
        )