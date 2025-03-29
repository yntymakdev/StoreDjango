from tkinter.constants import CASCADE

from django.db import models
from django.db.models import TextField


class Product(models.Model):
    title = models.CharField(max_length=14)
    description = models.TextField()
    price=  models.PositiveIntegerField()

class Comment(models.Model):
    comment_text = models.TextField()
    orm = models.ForeignKey(Product, on_delete=CASCADE)