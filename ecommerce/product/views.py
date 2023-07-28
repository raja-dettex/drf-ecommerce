from django.db.models import Q
from django.shortcuts import render
from django.http import JsonResponse, request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from .serilizer import ProductSerializer

# Create your views here.


@api_view(['GET'])
def endpoints(request):
    data = ['/products', 'products/:username']
    return Response(data)


@api_view(['GET'])
def product_list(request):
    # data = ['smartphone', 'tablet', 'earpods']
    query = request.GET.get('query')
    if query == None:
        query = ''
    advocates = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    serializer = ProductSerializer(advocates, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def product_details(request, name):
    # data = name
    product = Product.objects.get(name = name)
    serializer = ProductSerializer(product)
    return Response(serializer.data)

