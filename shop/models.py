from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    name=models.CharField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    image=models.ImageField()
    stock=models.IntegerField(default=0)

    def __str__(self):
        return self.name

class CartItem(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def get_total_item_price(self):
        return self.quantity * self.product.price

    def __str__(self):
        return f'{self.quantity} of {self.product.name}'