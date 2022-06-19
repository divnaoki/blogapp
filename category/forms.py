from attr import fields
from django import forms
from category.models import Category

class CategoryForm(forms.ModelForm):
  name = forms.CharField(
    label="Category Name",
    widget=forms.TextInput(
      attrs={
        "placeholder" : "input category name"
      }
    )
  )
  class Meta:
    model = Category
    fields = [
      "name"
    ]