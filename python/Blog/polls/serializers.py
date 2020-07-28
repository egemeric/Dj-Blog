from rest_framework import serializers
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .models import Comment


class CommetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Comment
        fields=('id', 'Title', 'Pub_date', 'Content', 'Image')







