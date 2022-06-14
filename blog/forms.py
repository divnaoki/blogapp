from turtle import width
from attr import attr, field
from django import forms
from .models import Blog

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
  class Meta:
    model = Blog
    fields = [
      "title",
      "content"
    ]