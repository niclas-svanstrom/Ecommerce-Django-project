from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from django.conf import settings

# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def update_total(self):
        self.total = sum(item.subtotal() for item in self.items.all())
        self.save()

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.price = self.product.price
        super().save(*args, **kwargs)

    def subtotal(self):
        if self.price is not None:
            return self.quantity * self.price
        else:
            return 0

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity
        self.save()
        self.cart.update_total()