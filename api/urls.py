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
    ProductDetailAPIView,
    BannerCreateAPIView, BannerUpdateAPIView, BannerDeleteAPIView, BannerListAPIView,
    CategoryCreateAPIView, CategoryUpdateAPIView, CategoryDeleteAPIView, CategoryListAPIView,
    OrderCreateAPIView, OrderUpdateAPIView, OrderDeleteAPIView, OrderListAPIView,
    NavbarInfoCreateAPIView, NavbarInfoUpdateAPIView, NavbarInfoDeleteAPIView, NavbarInfoListAPIView,
    FooterInfoCreateAPIView, FooterInfoUpdateAPIView, FooterInfoDeleteAPIView, FooterInfoListAPIView,
    WishListCreateAPIView, WishListUpdateAPIView, WishListDeleteAPIView, WishListListAPIView

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
    path('api/products/<int:pk>/', ProductDetailAPIView.as_view(), name='product_detail_api'),

    # Banner URLs
    path('banners/create/', BannerCreateAPIView.as_view(), name='banner-create'),
    path('banners/update/<int:pk>/', BannerUpdateAPIView.as_view(), name='banner-update'),
    path('banners/delete/<int:pk>/', BannerDeleteAPIView.as_view(), name='banner-delete'),
    path('banners/', BannerListAPIView.as_view(), name='banner-list'),

    # Category URLs
    path('categories/create/', CategoryCreateAPIView.as_view(), name='category-create'),
    path('categories/update/<int:pk>/', CategoryUpdateAPIView.as_view(), name='category-update'),
    path('categories/delete/<int:pk>/', CategoryDeleteAPIView.as_view(), name='category-delete'),
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),

    # Order URLs
    path('orders/create/', OrderCreateAPIView.as_view(), name='order-create'),
    path('orders/update/<int:pk>/', OrderUpdateAPIView.as_view(), name='order-update'),
    path('orders/delete/<int:pk>/', OrderDeleteAPIView.as_view(), name='order-delete'),
    path('orders/', OrderListAPIView.as_view(), name='order-list'),

    # NavbarInfo URLs
    path('navbar-info/create/', NavbarInfoCreateAPIView.as_view(), name='navbarinfo-create'),
    path('navbar-info/update/<int:pk>/', NavbarInfoUpdateAPIView.as_view(), name='navbarinfo-update'),
    path('navbar-info/delete/<int:pk>/', NavbarInfoDeleteAPIView.as_view(), name='navbarinfo-delete'),
    path('navbar-info/', NavbarInfoListAPIView.as_view(), name='navbarinfo-list'),

    # FooterInfo URLs
    path('footer-info/create/', FooterInfoCreateAPIView.as_view(), name='footerinfo-create'),
    path('footer-info/update/<int:pk>/', FooterInfoUpdateAPIView.as_view(), name='footerinfo-update'),
    path('footer-info/delete/<int:pk>/', FooterInfoDeleteAPIView.as_view(), name='footerinfo-delete'),
    path('footer-info/', FooterInfoListAPIView.as_view(), name='footerinfo-list'),

    # WishList URLs
    path('wishlists/create/', WishListCreateAPIView.as_view(), name='wishlist-create'),
    path('wishlists/update/<int:pk>/', WishListUpdateAPIView.as_view(), name='wishlist-update'),
    path('wishlists/delete/<int:pk>/', WishListDeleteAPIView.as_view(), name='wishlist-delete'),
    path('wishlists/', WishListListAPIView.as_view(), name='wishlist-list'),
]