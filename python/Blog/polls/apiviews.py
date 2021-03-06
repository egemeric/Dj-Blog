
from django.http import HttpResponse, Http404, JsonResponse
from django.utils import timezone
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from rest_framework import status
from .models import Comment
from .permissions import IsOwnerOrReadOnly
from .serializers import CommentSerializer, UserSerializer, CommentSerializer_upload_only_file
from .models import Comment
from rest_framework.decorators import api_view

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CommentList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(Owner=self.request.user)

    def get(self, request, format=None):
        cmt = Comment.objects.all()
        serializer = CommentSerializer(cmt, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]
    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        cmt = self.get_object(pk)
        serializer = CommentSerializer(cmt)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
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
    

class Upload_File(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    parser_class = (FileUploadParser,MultiPartParser, FormParser)
    
    def perform_create(self, serializer):
        serializer.save(Owner=self.request.user)
    
    def put(self, request, format=None):
        serializer = CommentSerializer_upload_only_file(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




