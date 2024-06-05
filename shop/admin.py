from django.contrib import admin
from .models import User, Guitar, GuitarCategory, Order, OrderGuitar, ShoppingCart

admin.site.register(User)
admin.site.register(Guitar)
admin.site.register(GuitarCategory)
admin.site.register(Order)
admin.site.register(OrderGuitar)
admin.site.register(ShoppingCart)
