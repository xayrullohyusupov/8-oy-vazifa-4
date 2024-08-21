from django.urls import path, include
from django.contrib.auth import views as auth_views
from Goods import views
from . import views


urlpatterns = [
    path('', views.main, name='index'),
    path('shop/', views.shop, name='shop'),
    path('shop_list/',views.shop_list, name='shop_list'),
    path('shop_detail/',views.shop_detail, name='shop_detail'), 
    path('authentication/', include('Goods.authentication.urls')),
    path('back-office/', include('Goods.back-office.urls')),
    path('user/', include('Goods.user.urls')),
]