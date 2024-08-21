from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from .views import (
    LogoutView,
    RegisterView,
    CartView, 
    AddProductToCartView,
    MainAPIView,
    SignupAPIView,
    ProductListCreateAPIView, 
    ProductDetailAPIView

    )

urlpatterns = [
    path('cart/', CartView.as_view(), name='get_or_create_cart'),
    path('add-product/', AddProductToCartView.as_view(), name='add_product_to_cart'),
    path('login/', obtain_auth_token, name='api_token_auth'),
    path('logout/', LogoutView.as_view(), name='api_token_logout'),
    path('register/', RegisterView.as_view(), name='api_register'),
    path('api/main/', MainAPIView.as_view(), name='main_api'),
    path('api/signup/', SignupAPIView.as_view(), name='signup_api'),
    path('api/products/', ProductListCreateAPIView.as_view(), name='product_list_create_api'),
    path('api/products/<int:pk>/', ProductDetailAPIView.as_view(), name='product_detail_api')
]