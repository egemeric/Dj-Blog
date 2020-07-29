from rest_framework import serializers
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields=('Owner', 'id', 'Title', 'Pub_date', 'Content', 'Image')







