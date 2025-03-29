from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Notification
from posts.serializers import PostSerializer, CommentSerializer
from accounts.serializers import UserSerializer  # Assuming UserSerializer is in accounts

# start task 3
class NotificationSerializer(serializers.ModelSerializer):
    recipient = UserSerializer(read_only=True)
    actor = UserSerializer(read_only=True)
    target_post = serializers.SerializerMethodField()
    target_comment = serializers.SerializerMethodField()
    target_user = serializers.SerializerMethodField()  # For follow notifications

    class Meta:
        model = Notification
        fields = ('id', 'recipient', 'actor', 'verb', 'target_post', 'target_comment', 'target_user', 'timestamp', 'read')
        read_only_fields = ('id', 'recipient', 'actor', 'verb', 'target_post', 'target_comment', 'target_user', 'timestamp')

    def get_target_post(self, obj):
        if obj.target_content_type and obj.target_content_type.model == 'post' and obj.target:
            return PostSerializer(obj.target, read_only=True).data
        return None

    def get_target_comment(self, obj):
        if obj.target_content_type and obj.target_content_type.model == 'comment' and obj.target:
            return CommentSerializer(obj.target, read_only=True).data
        return None

    def get_target_user(self, obj):
        if obj.verb == 'started following you' and obj.actor:
            return UserSerializer(obj.actor, read_only=True).data
        return None
    #end task 3