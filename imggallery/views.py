from django.shortcuts import render
from rest_framework import generics,viewsets
from .models import Gallery 
from .serializers import ImgSerializer
from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework_simplejwt.authentication import JWTAuthentication 
# from rest_framework.permissions import IsAuthenticated

# Create your views here.
class GalleryView(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = ImgSerializer
    # permission_classes = (IsAuthenticated,)
    

    def post(self, request, *args, **kwargs):
        title = request.data['title']
        image = request.data['image']
        Gallery.objects.create(title=title, img=image)
        return Response({'message': 'Book created'}, status=200)

# @api_view(['POST','GET'])
# def GalleryView(request):
#     if request.method== 'POST':
#         # data = Gallery.objects.all()
#         serializer = ImgSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()

#         return Response(serializer.data)
#     else:
#         data = Gallery.objects.all()
#         serializer = ImgSerializer(data,many=True)
#         return Response(serializer.data)