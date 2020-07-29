
from django.http import HttpResponse, Http404, JsonResponse
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from .models import Comment
from .serializers import CommetSerializer
from rest_framework.decorators import api_view


class CommentList(APIView):

    def get(self, request, format=None):
        cmt = Comment.objects.all()
        serializer = CommetSerializer(cmt, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = CommetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetail(APIView):
    def get_object(self, pk):
        try:
            return Comment.objects(pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        cmt = self.get_object(pk)
        serializer = CommetSerializer(cmt)
        return Response(serializer.data)
    def put(self, request, format=None):
        cmt = self.get_object(pk)
        serializer = CommetSerializer(cmt, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        cmt=self.get_object(pk)
        cmt.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

