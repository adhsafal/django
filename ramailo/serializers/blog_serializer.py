from rest_framework import serializers
from ramailo.models.blog import Post, Category, Comment, PostImage

from ramailo.models.user import User


class PostSerializer(serializers.Serializer):
    idx = serializers.UUIDField(read_only=True)
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    author = serializers.CharField()
    is_published = serializers.BooleanField(default=False)
    created_at = serializers.DateTimeField(read_only=True)
    category = serializers.PrimaryKeyRelatedField(many=True, queryset=Category.objects.all(), source='categories')
    

class CatgegorySerializer(serializers.Serializer):
    name = serializers.CharField()
    
class CommentSerializer(serializers.Serializer):
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    content = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
    
class PostImageSerializer(serializers.Serializer):
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    url = serializers.URLField()
    created_at = serializers.DateTimeField(read_only=True)