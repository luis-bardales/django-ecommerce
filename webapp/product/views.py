from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Category

def seeders(request):
    query = Category(title="For Men", image_id=1, description="For Men blah blah", created_at=timezone.now())
    query.save()

    query = Category(title="For Women", image_id=2, description="For Women blah blah", created_at=timezone.now())
    query.save()
    
    query = Category(title="Accessories", image_id=3, description="Accessories blah blah", created_at=timezone.now())
    query.save()
    
    query = Category(title="Cosmetic", image_id=4, description="Cosmetic blah blah", created_at=timezone.now())
    query.save()

    return HttpResponse("Seeders saved into database")
