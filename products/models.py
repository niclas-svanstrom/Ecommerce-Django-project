from django.db import models
import os
from uuid import uuid4

# Create your models here.
def get_product_image_filename(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'product_{instance.id}.{ext}'
    return os.path.join('static/products/static/media', filename)

class Category(models.Model):
    name = models.CharField(max_length=50)
  
    @staticmethod
    def get_all_categories():
        return Category.objects.all()
  
    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(upload_to=get_product_image_filename, blank=True, null=True)

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)
  
    @staticmethod
    def get_all_products():
        return Product.objects.all()
  
    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()

    def save(self, *args, **kwargs):
        if self.pk is None:
            saved_image = self.image
            self.image = None
            super().save(*args, **kwargs)
            self.image = saved_image

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
