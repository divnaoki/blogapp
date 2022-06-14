from configparser import InterpolationMissingOptionError
from operator import itemgetter
from django.shortcuts import render
from .models import Blog
from .forms import BlogForm
# Create your views here.
def index_view(request):
  items = Blog.objects.all()
  context = {
    "items": items
  }
  return render(request, "blog/index.html", context)

def create_view(request):
  form = BlogForm()
  if request.method == "POST":
    form = BlogForm(request.POST)
    if form.is_valid():
      form.save()
      
    else:
      print(form.errors)
  context = {
    "form": form
  }
  return render(request, "blog/create.html", context)
  