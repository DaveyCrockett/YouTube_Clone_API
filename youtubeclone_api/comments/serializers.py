from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['video_id', 'comment', 'comment_replys', 'likes', 'dislikes', 'create_date']