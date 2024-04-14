from django.shortcuts import render
from django.http import HttpResponse
from .models import DishCategory

# Create your views here.

def index(request):
    categories = DishCategory.objects.all()
    # categories = DishCategory.objects.filter(is_visible=True)
    # categories = DishCategory.objects.get(id=1)


    return HttpResponse("\n".join(map(str,categories)))
     