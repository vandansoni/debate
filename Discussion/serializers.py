from rest_framework import serializers
from Discussion.models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')



class DiscussionSerializer(serializers.ModelSerializer):
    # school_count = serializers.SerializerMethodField()
    class Meta:
        model = Discussion
        exclude = ('created_date', 'modified_date')


class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        exclude = ('created_date', 'modified_date')   

class DiscssionSearchListSerializer(serializers.ModelSerializer):
    # school_count = serializers.SerializerMethodField()
    class Meta:
        model = Discussion
        exclude = ('created_date', 'modified_date')

#validate the title serializer
class validateDiscssionSearchListSerializer(serializers.Serializer):
    title = serializers.CharField(required=False)