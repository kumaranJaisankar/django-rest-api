from django.shortcuts import render
from django.contrib.auth.models import User,auth
from rest_framework import status,generics

from rest_framework.response import Response
from rest_framework.decorators import api_view ,permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import ProductSerializer
from .models import Product


# Create your views here.

"""@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/product-list/',
        'Detail View': '/product-detail/<int:id>/',
        'Create': '/product-create/',
        'Update': '/product-update/<int:id>/',
        'Delete': '/product-detail/<int:id>/',
    }
    return Response(api_urls);
"""

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def ShowAll(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def ViewProduct(request, pk):
    try:
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product, many=False)
        if serializer is not None:
            return Response(serializer.data)
        else :
            return Response({'error':'ivalid id'})
    except :
        return Response({'message':'Product does not exist'})


@api_view(['POST'])
def CreateProduct(request):
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)



@api_view(['POST'])
def updateProduct(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=product, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()

    return Response('Items delete successfully!')

@api_view(['POST'])
def userRegister(request):
    username = request.data['username']
    email = request.data['email']
    password = request.data['password']
    if User.objects.filter(username=username).exists():
        return Response({'message':'Username already taken, plz Enter different username'},status=status.HTTP_406_NOT_ACCEPTABLE)
    elif User.objects.filter(email=email).exists():
        return Response({'message':'Email ID already taken, plz Enter different Email ID'},status=status.HTTP_406_NOT_ACCEPTABLE)
    else:
        user = User.objects.create_user(username=username,email=email,password=password)
        user.save()
        return Response({'message':'success'})


@api_view(['POST'])
def userLogin(request):
    username = request.data['username']
    password = request.data['password']
    user = auth.authenticate(username=username,password=password)
    
    if user is not None:
        refresh = RefreshToken.for_user(user)
        auth.login(request,user)
        return Response({
        'username':str(username),
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    })
    else:
       
        return Response({'message':'Wrong Username or Password'},status=status.HTTP_401_UNAUTHORIZED)
   

