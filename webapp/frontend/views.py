from django.shortcuts import render
from product.models import Category

def homepage(request):
    categories = Category.objects.all()
    return render(request, 'home.html', {'categories': categories})
