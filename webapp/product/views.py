from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Category

def seeders(request):
    query = Category(title="For Men", description="For Men blah blah", created_at=timezone.now())
    query.save()

    query = Category(title="For Women", description="For Women blah blah", created_at=timezone.now())
    query.save()
    
    query = Category(title="Accessories", description="Accessories blah blah", created_at=timezone.now())
    query.save()
    
    query = Category(title="Cosmetic", description="Cosmetic blah blah", created_at=timezone.now())
    query.save()

    return HttpResponse("Seeders saved into database")
