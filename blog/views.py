from configparser import InterpolationMissingOptionError
from operator import itemgetter
from django.shortcuts import render
from .models import Blog
# Create your views here.
def index_view(request):
  items = Blog.objects.all()
  context = {
    "items": items
  }
  return render(request, "blog/index.html", context)