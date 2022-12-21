from rest_framework import serializers

from applications.feedback.models import Comment

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField()
    class Meta:
        model = Comment
        fields = '__all__'