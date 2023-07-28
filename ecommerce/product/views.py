from django.db.models import Q
from django.shortcuts import render
from django.http import JsonResponse, request, Http404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import Product, User
from .serilizer import ProductSerializer, UserSerializer

# Create your views here.


@api_view(['GET'])
def endpoints(request):
    data = ['/products', 'products/:username']
    return Response(data)


# @api_view(['GET', 'POST'])
# def product_list(request):
#     # data = ['smartphone', 'tablet', 'earpods']
#     if request.method == 'GET':
#         query = request.GET.get('query')
#         if query == None:
#             query = ''
#         advocates = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
#         serializer = ProductSerializer(advocates, many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         product = Product.objects.create(
#             name = request.data['name'],
#             description = request.data['desc']
#         )
#         print(product)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def product_details(request, name):
#     product = Product.objects.get(name=name)
#     # data = name
#     if request.method == 'GET':
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)
#     if request.method == 'PUT':
#         product.name = request.data['name']
#         product.description = request.data['desc']
#         product.save()
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)
#     if request.method == 'DELETE':
#         deletedId = product.name
#         product.delete()
#         return Response(f'product has been deleted with name: {deletedId}')


class ProductView(APIView):

    def get_object(self, name):
        try:
            products = Product.objects.get(name=name)
            return products
        except Product.DoesNotExist:
            raise Http404

    def create(self, name, description):
        try:
            product = Product.objects.create(
                name = name,
                description = description
            )
            return product
        except RuntimeError as e:
            raise e

    def get(self, request, name):
        products = self.get_object(name)
        serializer = ProductSerializer(products)
        return Response(serializer.data)

    def put(self, request, name):
        products = self.get_object(name)
        serializer = ProductSerializer(products, data=request.data)
        return Response(serializer.data)

    def delete(self, request, name):
        products = self.get_object(name)
        productName = products.name
        products.delete()
        return Response(f'product has been deleted with id {productName} ')

    def post(self, request):
        name = request.data['name']
        description = request.data['desc']
        product = self.create(name, description)
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def user_list(request):

    if request.method == 'GET':
        users = User.objects.all()
        print(users)
        userSerializer = UserSerializer(users, many=True)
        return Response(userSerializer.data)
    if request.method == 'POST':
        productData = request.data['product']
        if productData == None:
            user = User.objects.create(
                name=request.data['name'],
                email=request.data['email'],
                product=productData
            )
            userSerializer = UserSerializer(user, many=False)
            return Response(userSerializer.data)
        else:
            product = Product.objects.create(
                name=productData['name'],
                description=productData['desc']
            )
            productData = ProductSerializer(product, many=False).data
            user = User.objects.create(
                name=request.data['name'],
                email=request.data['email'],
                product = product
            )
            userSerializer = UserSerializer(user, many=False)
            return Response(userSerializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def user_details(request, name):
    user = User.objects.get(name=name)

    if request.method == 'GET':
        userSerializer = UserSerializer(user, many=False)
        return Response(userSerializer.data)

    if request.method == 'PUT':
        user.name = request.data['name']
        user.email = request.data['email']
        userSerializer = UserSerializer(user, many=False)
        return Response(userSerializer.data)

    if request.method == 'DELETE':
        username = user.name
        user.delete()
        return Response(f'user deleted with name: {username}')


