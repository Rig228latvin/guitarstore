# shop/views.py
from rest_framework import viewsets
from .models import User, Order, Guitar, GuitarCategory, ShoppingCart
from .serializers import UserSerializer, OrderSerializer, GuitarSerializer, GuitarCategorySerializer, \
    ShoppingCartSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class GuitarViewSet(viewsets.ModelViewSet):
    queryset = Guitar.objects.all()
    serializer_class = GuitarSerializer


class GuitarCategoryViewSet(viewsets.ModelViewSet):
    queryset = GuitarCategory.objects.all()
    serializer_class = GuitarCategorySerializer


class ShoppingCartViewSet(viewsets.ModelViewSet):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer
