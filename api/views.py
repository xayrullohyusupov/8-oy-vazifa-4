from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics,status
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from rest_framework.authtoken.models import Token
from Goods.models import Cart, Product, CartProduct,Banner, NavbarInfo, FooterInfo, ProductEnter
from .serializers import (
    UserRegistrationSerializer,
    CartSerializer,
    ProductSerializer,
    BannerSerializer,
    NavbarInfoSerializer,
    FooterInfoSerializer,
    ProductEnterSerializer,
    WishListSerializer,
    CategorySerializer,
    OrderSerializer
    )

from Goods.models import Banner, Category, Order, NavbarInfo, FooterInfo, WishList


class BannerCreateAPIView(generics.CreateAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

class BannerUpdateAPIView(generics.UpdateAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

class BannerDeleteAPIView(generics.DestroyAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

class BannerListAPIView(generics.ListAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer


class CategoryCreateAPIView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryUpdateAPIView(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDeleteAPIView(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class OrderCreateAPIView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderUpdateAPIView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDeleteAPIView(generics.DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class NavbarInfoCreateAPIView(generics.CreateAPIView):
    queryset = NavbarInfo.objects.all()
    serializer_class = NavbarInfoSerializer

class NavbarInfoUpdateAPIView(generics.UpdateAPIView):
    queryset = NavbarInfo.objects.all()
    serializer_class = NavbarInfoSerializer

class NavbarInfoDeleteAPIView(generics.DestroyAPIView):
    queryset = NavbarInfo.objects.all()
    serializer_class = NavbarInfoSerializer

class NavbarInfoListAPIView(generics.ListAPIView):
    queryset = NavbarInfo.objects.all()
    serializer_class = NavbarInfoSerializer


class FooterInfoCreateAPIView(generics.CreateAPIView):
    queryset = FooterInfo.objects.all()
    serializer_class = FooterInfoSerializer

class FooterInfoUpdateAPIView(generics.UpdateAPIView):
    queryset = FooterInfo.objects.all()
    serializer_class = FooterInfoSerializer

class FooterInfoDeleteAPIView(generics.DestroyAPIView):
    queryset = FooterInfo.objects.all()
    serializer_class = FooterInfoSerializer

class FooterInfoListAPIView(generics.ListAPIView):
    queryset = FooterInfo.objects.all()
    serializer_class = FooterInfoSerializer


class WishListCreateAPIView(generics.CreateAPIView):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer

class WishListUpdateAPIView(generics.UpdateAPIView):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer

class WishListDeleteAPIView(generics.DestroyAPIView):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer

class WishListListAPIView(generics.ListAPIView):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response({"message": "Logged out successfully"}, status=204)

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(username=response.data['username'])
        token, created = Token.objects.get_or_create(user=user)
        print(token.key)
        return Response({"token": token.key}, status=201)
        

class CartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart, created = Cart.objects.get_or_create(author=request.user, is_active=True)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

class AddProductToCartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        product_code = request.data.get('product_code')
        try:
            product = Product.objects.get(generate_code=product_code)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=404)

        cart, _ = Cart.objects.get_or_create(author=request.user, is_active=True)
        cart_product, created = CartProduct.objects.get_or_create(cart=cart, product=product)

        if not created:
            cart_product.quantity += 1
            cart_product.save()

        return Response({"message": f"Product {product_code} added to cart"})
    
class MainAPIView(APIView):
    def get(self, request, *args, **kwargs):
        banners = Banner.objects.filter(is_active=True)[:5]
        navbar_info = NavbarInfo.objects.get()
        footer_info = FooterInfo.objects.get()

        data = {
            'banners': BannerSerializer(banners, many=True).data,
            'navbar_info': NavbarInfoSerializer(navbar_info).data,
            'footer_info': FooterInfoSerializer(footer_info).data
        }
        return Response(data)

class SignupAPIView(APIView):
    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.data)
        if form.is_valid():
            user = form.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = ProductEnter.objects.all()
    serializer_class = ProductEnterSerializer

class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductEnter.objects.all()
    serializer_class = ProductEnterSerializer

