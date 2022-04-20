from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category_name = models.CharField(max_length=255)
    category_image = models.ImageField(upload_to='category/image',null=True,blank=True)

    def __str__(self):
        return self.category_name

class Brand(models.Model):
    brand_name = models.CharField(max_length=255)
    brand_image = models.ImageField(upload_to='brand/image',null=True,blank=True)

    def __str__(self):
        return self.brand_name

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_price = models.IntegerField(null=True,blank=True)
    product_image = models.ImageField(upload_to='brand/product',null=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.product_name

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    address = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    image = models.ImageField(upload_to='profile/image',null=True)
    contact = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username


class ProductImages(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    images = models.ImageField(upload_to='brand/productImg',null=True)

    def __str__(self):
        return self.product.product_name

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    product_name = models.CharField(max_length=255)
    product_price = models.IntegerField(null=True,blank=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)
    brand_name = models.CharField(max_length=255,null=True)
    category_name = models.CharField(max_length=255,null=True)
