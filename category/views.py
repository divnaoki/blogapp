from django.shortcuts import render
from .models import Category
# Create your views here.
def category_index_view(request):
  items = Category.objects.all()
  context = {
    "items" : items
  }
  return render(request, "category/index.html", context)