from rest_framework.serializers import ModelSerializer
from .models import Product, User


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class UserSerializer(ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = User
        fields = '__all__'

