from rest_framework import serializers
from .models import Post, Comment
from accounts.serializers import UserSerializer

#start task 1
class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    comment_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at', 'comment_count']
        read_only_fields = ['id', 'author', 'created_at', 'updated_at']

    def get_comment_count(self, obj):
        return obj.comments.count()

class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at', 'updated_at']
        read_only_fields = ['id', 'author', 'created_at', 'updated_at']

class PostCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content']

class CommentCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content']
# end task 1

#start task 2
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Comment, Like

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class LikeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all(), write_only=True)

    class Meta:
        model = Like
        fields = ('id', 'post', 'user', 'created_at')
        read_only_fields = ('id', 'user', 'created_at')

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    comments = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    user_liked = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'content', 'created_at', 'updated_at', 'comments', 'likes_count', 'user_liked')
        read_only_fields = ('created_at', 'updated_at')

    def get_comments(self, instance):
        serializer = CommentSerializer(instance.comments.all(), many=True, read_only=True)
        return serializer.data

    def get_likes_count(self, instance):
        return instance.likes.count()

    def get_user_liked(self, instance):
        user = self.context['request'].user
        if user.is_authenticated:
            return instance.likes.filter(user=user).exists()
        return False

class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all(), write_only=True)
    post_detail = PostSerializer(source='post', read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'post', 'post_detail', 'author', 'content', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at', 'author', 'post_detail')

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)
# end task 2