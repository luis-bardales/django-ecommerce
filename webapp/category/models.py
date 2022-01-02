from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=160)
    slug = models.SlugField(max_length=200, unique=True)
    image_id = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title