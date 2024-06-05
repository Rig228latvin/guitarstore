# shop/serializers.py
from rest_framework import serializers
from .models import User, Order, Guitar, GuitarCategory, OrderGuitar, ShoppingCart

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id', 'first_name', 'last_name', 'email', 'role')

class GuitarCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GuitarCategory
        fields = ('category_id', 'category_name')

class GuitarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guitar
        fields = '__all__'

class OrderGuitarSerializer(serializers.ModelSerializer):
    guitar = GuitarSerializer()

    class Meta:
        model = OrderGuitar
        fields = ['guitar', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    order_date = serializers.DateField(format="%Y-%m-%d", read_only=True)
    order_guitars = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['order_id', 'order_date', 'order_status', 'total_price', 'order_guitars']
        read_only_fields = ['order_id', 'order_date', 'total_price', 'order_guitars']

    def get_order_guitars(self, obj):
        order_guitars = OrderGuitar.objects.filter(order=obj)
        return OrderGuitarSerializer(order_guitars, many=True).data

class ShoppingCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCart
        fields = ['cart_id', 'guitars_count', 'guitar', 'user']
