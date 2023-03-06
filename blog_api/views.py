# from django.shortcuts import render
from rest_framework import generics, viewsets
from blog.models import Post
from .serializers import PostSerializer, ProductSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
class PostList(generics.ListCreateAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer 
class PostDetail(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

@api_view(['GET'])
def UserList(request):
    user = User.objects.all()
    serializer = ProductSerializer(user,many=True)
    return Response(serializer.data)

