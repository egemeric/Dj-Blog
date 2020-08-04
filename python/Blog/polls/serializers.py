from rest_framework import serializers
from django.contrib.auth.models import User, Group
from django.utils import timezone
from rest_framework import viewsets
from .models import Comment



class CommentSerializer(serializers.ModelSerializer):
    Owner = serializers.ReadOnlyField(source='Owner.username')
    class Meta:
        model=Comment
        fields=('Owner', 'id', 'Title', 'Pub_date', 'Content', 'Image')

class CommentSerializer_upload_only_file(serializers.ModelSerializer):
    Owner = serializers.ReadOnlyField(source='Owner.username')
    Title=serializers.CharField(default=str(timezone.now()))
    class Meta:
        model = Comment
        
        fields=('Owner', 'id','Title','Pub_date','File')


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Comment.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']




