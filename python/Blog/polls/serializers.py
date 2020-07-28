from rest_framework import serializers
from .models import Comment

class CommetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields=('id', 'Title', 'Pub_date', 'Content', 'Image')