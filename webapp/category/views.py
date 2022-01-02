from django.shortcuts import render
from django.utils import timezone
from .models import Category

categories = [
    {
        "title": "Smartphones",
        "slug": "smartphones",
        "image_id": 1,
        "description": "Smartphones blah blah",
        "created_at": timezone.now()
    },
    {
        "title": "Laptops",
        "slug": "laptops",
        "image_id": 2,
        "description": "Laptops blah blah",
        "created_at": timezone.now()
    },
    {
        "title": "Televisions",
        "slug": "televisions",
        "image_id": 3,
        "description": "Televisions blah blah",
        "created_at": timezone.now()
    },
    {
        "title": "Watches",
        "slug": "watches",
        "image_id": 4,
        "description": "Watches blah blah",
        "created_at": timezone.now()
    }
]
