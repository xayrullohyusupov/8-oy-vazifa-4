from rest_framework import serializers
from django.contrib.auth.models import User
from Goods.models import (
    Product,
    CartProduct,
    Cart,
    Order,
    Banner,
    NavbarInfo, 
    FooterInfo, 
    ProductEnter,
    WishList,
    Category
    )

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'generate_code', 'quantity', 'price', 'category', 'description']

class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProduct
        fields = ['product', 'quantity']

class CartSerializer(serializers.ModelSerializer):
    products = CartProductSerializer(source='cartproduct_set', many=True, read_only=True)
    author = serializers.StringRelatedField()

    class Meta:
        model = Cart
        fields = ['author', 'is_active', 'products', 'shopping_date']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class OrderSerializer(serializers.ModelSerializer):
    cart = CartSerializer()

    class Meta:
        model = Order
        fields = ['cart', 'full_name', 'email', 'phone', 'address', 'status']

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'

class NavbarInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavbarInfo
        fields = '__all__'

class FooterInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterInfo
        fields = '__all__'

class ProductEnterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductEnter
        fields = '__all__'

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'

# Category Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

# Order Serializer
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

# NavbarInfo Serializer
class NavbarInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavbarInfo
        fields = '__all__'

# FooterInfo Serializer
class FooterInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterInfo
        fields = '__all__'

# WishList Serializer
class WishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishList
        fields = '__all__'
