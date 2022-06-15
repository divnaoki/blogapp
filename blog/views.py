from configparser import InterpolationMissingOptionError
from operator import itemgetter
from django.shortcuts import redirect, render
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
      return redirect("/blog")
    else:
      print(form.errors)
  context = {
    "form": form
  }
  return render(request, "blog/create.html", context)

def update_view(request, pk):
  item = Blog.objects.get(id=pk)
  form = BlogForm(instance=item)
  if request.method == "POST":
    form = BlogForm(request.POST, instance=item)
    if form.is_valid():
      form.save()
      return redirect("/blog")
    else:
      print(form.errors)
  context = {
    "form": form
  }
  return render(request, "blog/update.html", context)

def detail_view(request, pk):
  item = Blog.objects.get(id=pk)
  context = {
    "item": item
  }
  return render(request, "blog/detail.html", context)

def delete_view(request, pk):
  item = Blog.objects.get(id=pk)
  if request.method == "POST":
    item.delete()
    return redirect("/blog")
  context = {
    "item": item
  }
  return render(request, "blog/delete.html", context)