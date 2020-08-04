from rest_framework import serializers
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .models import Comment



class CommentSerializer(serializers.ModelSerializer):
    Owner = serializers.ReadOnlyField(source='Owner.username')
    class Meta:
        model=Comment
        fields=('Owner', 'id', 'Title', 'Pub_date', 'Content', 'Image')


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Comment.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']




