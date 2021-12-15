from django.http import HttpResponse
from django.utils import timezone
from .models import Category
from .models import Product

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

products = [
    {
        "sku": "UGG-BB-PUR-06",
        "title": "Samsung Galaxy A12 (Blue, 64GB, 4GB RAM)",
        "slug": "samsung-galaxy-a12-blue-64gb-4gb-ram",
        "description": "Samsung Galaxy A12 (Blue, 64GB, 4GB RAM)",
        "price": "500",
        "created_at": timezone.now()
    },
    {
        "sku": "UGG-BB-PUR-07",
        "title": "Redmi 8 64GB (Sapphire Blue, 4GB RAM)",
        "slug": "redmi-8-64gb-sapphire-blue-4gb-ram",
        "description": "Redmi 8 64GB (Sapphire Blue, 4GB RAM)",
        "price": "450",
        "created_at": timezone.now()
    },
    {
        "sku": "UGG-BB-PUR-06",
        "title": "Samsung Galaxy A12 (Blue, 64GB, 4GB RAM)",
        "slug": "samsung-galaxy-a12-blue-64gb-4gb-ram",
        "description": "Samsung Galaxy A12 (Blue, 64GB, 4GB RAM)",
        "price": "500",
        "created_at": timezone.now()
    },
    {
        "sku": "UGG-BB-PUR-07",
        "title": "Redmi 8 64GB (Sapphire Blue, 4GB RAM)",
        "slug": "redmi-8-64gb-sapphire-blue-4gb-ram",
        "description": "Redmi 8 64GB (Sapphire Blue, 4GB RAM)",
        "price": "450",
        "created_at": timezone.now()
    }
]

def seeders(request):
    """
    query = Category(title="For Men", image_id=1, description="For Men blah blah", created_at=timezone.now())
    query.save()
    """
    return HttpResponse("Seeders saved into database")
