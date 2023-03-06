from rest_framework import serializers 
from blog.models import Post
from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post 
        fields = ('id','title','author','excerpt', 'content','status','published')

from django.contrib.auth.models import User


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'