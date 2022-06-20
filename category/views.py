from django.shortcuts import render, redirect
from .models import Category
from .forms import CategoryForm
# Create your views here.
def category_index_view(request):
  items = Category.objects.all()
  context = {
    "items" : items
  }
  return render(request, "category/index.html", context)

def category_create_view(request):
  form = CategoryForm()
  if request.method == "POST":
    form = CategoryForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect("/category")
    else:
      print(form.errors)
  context = {
    "form": form
  }
  return render(request, "category/create.html", context)

def category_update_view(request, pk):
  item = Category.objects.get(id=pk)
  form = CategoryForm(instance=item)
  if request.method == "POST":
    form = CategoryForm(request.POST, instance=item)
    if form.is_valid():
      form.save()
      return redirect("/category")
    else:
      print(form.errors)
  context = {
    "form": form
  }
  return render(request, "category/update.html", context)

def category_delete_view(request, pk):
  item = Category.objects.get(id=pk)
  if request.method == "POST":
    item.delete()
    return redirect("/category")
  context = {
    "item": item
  }
  return render(request, "category/delete.html", context)