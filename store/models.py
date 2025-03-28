from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=16)
class Product(models.Model):
    product_name = models.CharField(max_length=16)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    created_date =  models.DateField(auto_now_add=True)
    have = models.BooleanField(default=True)

class Comment(models.Model):
    name  =  models.CharField(max_length=16)
    text =  models.TextField()
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
