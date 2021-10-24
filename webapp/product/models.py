from django.db import models

# Create your models here.
class Product(models.Model):
    sku = models.CharField(max_length=160, unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)
