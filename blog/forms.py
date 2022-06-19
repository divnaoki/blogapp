from django import forms
from .models import Blog
from category.models import Category

class BlogForm(forms.ModelForm):
  title = forms.CharField(
    label="Title",
    widget=forms.TextInput(
      attrs={
        "placeholder": "input title"
        }
      )
    )
  content = forms.CharField(
    label="Content",
    widget=forms.Textarea(
      attrs={
        "placeholder": "input content"
      }
    )
  )
  category = forms.ModelChoiceField(
    label='category',
    queryset=Category.objects.all(),
    empty_label="select your category",
    to_field_name="name",
    required=False
  )
  class Meta:
    model = Blog
    fields = [
      "title",
      "content",
      "category"
    ]