# shop/models.py
from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=100)

class GuitarCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)

class Guitar(models.Model):
    guitar_id = models.AutoField(primary_key=True)
    guitar_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    manufacturer = models.CharField(max_length=100)
    country_of_origin = models.CharField(max_length=100)
    year_of_production = models.IntegerField()
    image_url = models.URLField()
    category = models.ForeignKey(GuitarCategory, on_delete=models.CASCADE)

class Order(models.Model):
    ORDER_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    order_id = models.AutoField(primary_key=True)
    order_date = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=10, choices=ORDER_STATUS_CHOICES)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class OrderGuitar(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    guitar = models.ForeignKey(Guitar, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

class ShoppingCart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    guitars_count = models.PositiveIntegerField()
    guitar = models.ForeignKey(Guitar, on_delete=models.CASCADE)
