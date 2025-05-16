import os
from datetime import date
from django.db import models
from django_resized import ResizedImageField

class Brand(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Sub_Category(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name

def product_upload(instance, filename):
    ext = filename.split('.')[-1]
    today = date.today()
    filename = f'{today}.{ext}'
    return os.path.join('Products', f'{instance.name}', filename)

class Condition(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    image = ResizedImageField(size=[1080, 1080], crop=['middle', 'center'], upload_to=product_upload, null=True, blank=True)
    image_link = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=250)
    details = models.TextField()
    price = models.IntegerField(default=0)
    discounted_price = models.IntegerField(default=0)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Sub_Category, on_delete=models.CASCADE)
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE)
    wishlist = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    

    
