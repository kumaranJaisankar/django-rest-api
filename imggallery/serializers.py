from rest_framework import serializers 
from imggallery.models import Gallery


class ImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'