from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.decorators import api_view,authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .serializers import ProductSerializer, ShopSerializer
from .models import Product, Shop
from pytz import unicode


@api_view(['GET'])
def getAllProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getShops(request):
    shops = Shop.objects.all()
    serializer = ShopSerializer(shops, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addProduct(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['Get'])
def get_product(request, pk):
    products = Product.objects.get(id = pk)
    serializer = ProductSerializer(products, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def example_view(request, format=None):
    content = {
        'user': unicode(request.user),  # `django.contrib.auth.User` instance.
        'auth': unicode(request.auth),
        'is_authenticated': unicode(request.user.is_authenticated)  # None
    }
    return Response(content)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def another_view(request, format=None):
    
    name = request.query_params.get("name", None)
    if name is not None:
        user = User.objects.create_user(name, "user@gmail.com", "1234")
        user.save()
        return Response("OK")

    return Response("ERROR")
    


