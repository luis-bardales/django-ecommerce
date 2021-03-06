from django.db import models

class Product(models.Model):
    sku = models.CharField(max_length=160, unique=True)
    title = models.CharField(max_length=160)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=15, decimal_places=2)
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sku